#!/usr/bin/env python3
"""Validate, snapshot, and render the Awesome Mobile GUI Agents catalog."""

from __future__ import annotations

import argparse
import json
import math
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

import yaml
from jinja2 import Environment, FileSystemLoader, StrictUndefined
from jsonschema import Draft202012Validator, FormatChecker


ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "agents.yaml"
NOTABLE_FILE = ROOT / "data" / "notable.yaml"
RESOURCES_FILE = ROOT / "data" / "resources.yaml"
SCHEMA_FILE = ROOT / "schema" / "agents.schema.json"
SNAPSHOT_DIR = ROOT / "snapshots"
TEMPLATE_DIR = ROOT / "templates"
README_TARGETS = {
    "README.md.j2": ROOT / "README.md",
    "README.zh-CN.md.j2": ROOT / "README.zh-CN.md",
}
MINIMUM_MAIN_ENTRIES = 20
ALLOWED_AUDIT_STATUSES = {
    "links-verified",
    "code-inspected",
    "install-smoke-tested",
}


class CatalogError(RuntimeError):
    """A user-facing catalog validation or refresh error."""


def load_yaml(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        value = yaml.safe_load(handle)
    if not isinstance(value, dict):
        raise CatalogError(f"{path.relative_to(ROOT)} must contain a YAML mapping")
    return value


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise CatalogError(f"{path.relative_to(ROOT)} must contain a JSON object")
    return value


def validate_catalog(require_snapshot: bool = False) -> list[str]:
    catalog = load_yaml(DATA_FILE)
    schema = load_json(SCHEMA_FILE)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = [
        f"{'.'.join(str(part) for part in error.absolute_path) or '<root>'}: {error.message}"
        for error in sorted(validator.iter_errors(catalog), key=lambda item: list(item.absolute_path))
    ]

    agents = catalog.get("agents", [])
    if len(agents) < MINIMUM_MAIN_ENTRIES:
        errors.append(
            f"main catalog has {len(agents)} entries; at least {MINIMUM_MAIN_ENTRIES} are required"
        )

    ids = [agent.get("id") for agent in agents]
    duplicate_ids = sorted(item for item, count in Counter(ids).items() if count > 1)
    if duplicate_ids:
        errors.append(f"duplicate agent ids: {', '.join(duplicate_ids)}")

    repo_counts = Counter(agent.get("code", {}).get("repo") for agent in agents)
    for agent in agents:
        agent_id = agent.get("id", "<unknown>")
        repo = agent.get("code", {}).get("repo")
        stars_scope = agent.get("code", {}).get("stars_scope")
        if repo_counts[repo] > 1 and stars_scope != "family-level":
            errors.append(
                f"{agent_id}: shared repository {repo} must use stars_scope=family-level"
            )
        if repo_counts[repo] == 1 and stars_scope != "repository-level":
            errors.append(
                f"{agent_id}: unshared repository {repo} must use stars_scope=repository-level"
            )
        if agent.get("license", {}).get("status") != "open-source":
            errors.append(f"{agent_id}: main entries must have an open-source license")
        if agent.get("audit", {}).get("status") not in ALLOWED_AUDIT_STATUSES:
            errors.append(f"{agent_id}: unsupported audit status")
        if agent.get("audit", {}).get("install_smoke_tested") is True and (
            agent.get("audit", {}).get("status") != "install-smoke-tested"
        ):
            errors.append(
                f"{agent_id}: install_smoke_tested=true requires status=install-smoke-tested"
            )
        code_url = agent.get("code", {}).get("url", "")
        if not code_url.startswith(f"https://github.com/{repo}"):
            errors.append(f"{agent_id}: code URL must point to its official GitHub repository")

    if require_snapshot:
        try:
            snapshot = latest_snapshot()
        except CatalogError as error:
            errors.append(str(error))
        else:
            snapshot_ids = set(snapshot.get("citations", {}))
            paper_ids = {agent["id"] for agent in agents if agent.get("paper")}
            if snapshot_ids != paper_ids:
                errors.append(
                    "snapshot citation keys differ from catalog paper entries: "
                    f"snapshot_only={sorted(snapshot_ids - paper_ids)}, "
                    f"catalog_only={sorted(paper_ids - snapshot_ids)}"
                )
            snapshot_repos = set(snapshot.get("github", {}))
            catalog_repos = {agent["code"]["repo"] for agent in agents}
            if snapshot_repos != catalog_repos:
                errors.append(
                    "snapshot repository keys differ from catalog repositories: "
                    f"snapshot_only={sorted(snapshot_repos - catalog_repos)}, "
                    f"catalog_only={sorted(catalog_repos - snapshot_repos)}"
                )
    return errors


def fail_if_invalid(require_snapshot: bool = False) -> None:
    errors = validate_catalog(require_snapshot=require_snapshot)
    if errors:
        raise CatalogError("Catalog validation failed:\n- " + "\n- ".join(errors))


def request_json(
    url: str,
    *,
    headers: dict[str, str] | None = None,
    timeout: int = 45,
) -> dict[str, Any]:
    request_headers = {
        "Accept": "application/json",
        "User-Agent": "awesome-mobile-gui-agents/0.1",
    }
    if headers:
        request_headers.update(headers)
    value: Any = None
    for attempt in range(3):
        request = urllib.request.Request(url, headers=request_headers)
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                value = json.load(response)
            break
        except urllib.error.HTTPError as error:
            retryable = error.code == 429 or 500 <= error.code < 600
            if retryable and attempt < 2:
                time.sleep(2**attempt)
                continue
            detail = error.read().decode("utf-8", errors="replace")[:500]
            raise CatalogError(f"HTTP {error.code} for {url}: {detail}") from error
        except (urllib.error.URLError, TimeoutError) as error:
            if attempt < 2:
                time.sleep(2**attempt)
                continue
            reason = getattr(error, "reason", str(error))
            raise CatalogError(f"request failed for {url}: {reason}") from error
    if not isinstance(value, dict):
        raise CatalogError(f"expected JSON object from {url}")
    return value


def github_repo(repo: str) -> dict[str, Any]:
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    headers = {"Accept": "application/vnd.github+json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return request_json(f"https://api.github.com/repos/{repo}", headers=headers)


def github_path_exists(repo: str, path: str, default_branch: str) -> bool:
    if not path:
        return True
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    headers = {"Accept": "application/vnd.github+json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    encoded_path = urllib.parse.quote(path, safe="/")
    encoded_ref = urllib.parse.quote(default_branch, safe="")
    try:
        request_json(
            f"https://api.github.com/repos/{repo}/contents/{encoded_path}?ref={encoded_ref}",
            headers=headers,
        )
    except CatalogError:
        return False
    return True


def openalex_json(endpoint: str, params: dict[str, str] | None = None) -> dict[str, Any]:
    query = dict(params or {})
    api_key = os.environ.get("OPENALEX_API_KEY")
    if api_key:
        query["api_key"] = api_key
    mailto = os.environ.get("OPENALEX_MAILTO")
    if mailto:
        query["mailto"] = mailto
    suffix = f"?{urllib.parse.urlencode(query)}" if query else ""
    return request_json(f"https://api.openalex.org/{endpoint}{suffix}")


def openalex_work_id(value: str) -> str:
    match = re.fullmatch(r"(?:https://openalex\.org/)?(W\d+)", value)
    if not match:
        raise CatalogError(f"invalid OpenAlex work id: {value}")
    return match.group(1)


def citation_snapshot(agent: dict[str, Any]) -> dict[str, Any]:
    paper = agent["paper"]
    ids = [openalex_work_id(value) for value in paper["openalex_ids"]]
    works = []
    for work_id in ids:
        payload = openalex_json(f"works/{work_id}")
        works.append(
            {
                "id": work_id,
                "title": payload.get("title"),
                "doi": payload.get("doi"),
                "publication_date": payload.get("publication_date"),
                "cited_by_count": payload.get("cited_by_count"),
            }
        )
    union = openalex_json(
        "works",
        {
            "filter": f"cites:{'|'.join(ids)}",
            "per-page": "1",
            "select": "id",
        },
    )
    count = union.get("meta", {}).get("count")
    if not isinstance(count, int):
        raise CatalogError(f"OpenAlex did not return a citation count for {agent['id']}")
    return {
        "count": count,
        "deduplication": "union-of-citing-work-ids",
        "openalex_ids": ids,
        "works": works,
    }


def refresh_snapshot(snapshot_date: str, force: bool = False) -> Path:
    fail_if_invalid(require_snapshot=False)
    try:
        parsed_date = date.fromisoformat(snapshot_date)
    except ValueError as error:
        raise CatalogError(f"invalid snapshot date: {snapshot_date}") from error
    if parsed_date > datetime.now(timezone.utc).date():
        raise CatalogError("snapshot date cannot be in the future")

    output = SNAPSHOT_DIR / f"{snapshot_date}.json"
    if output.exists() and not force:
        raise CatalogError(f"{output.relative_to(ROOT)} already exists; pass --force to replace it")

    catalog = load_yaml(DATA_FILE)
    agents = catalog["agents"]
    github: dict[str, Any] = {}
    for repo in sorted({agent["code"]["repo"] for agent in agents}):
        print(f"GitHub: {repo}", file=sys.stderr)
        payload = github_repo(repo)
        expected_licenses = {
            agent["license"]["spdx"]
            for agent in agents
            if agent["code"]["repo"] == repo
        }
        if len(expected_licenses) != 1:
            raise CatalogError(f"{repo}: inconsistent curated license values")
        expected_license = next(iter(expected_licenses))
        actual_license = (payload.get("license") or {}).get("spdx_id")
        if actual_license != expected_license:
            raise CatalogError(
                f"{repo}: GitHub reports license {actual_license!r}, expected {expected_license!r}"
            )
        default_branch = payload.get("default_branch")
        if not isinstance(default_branch, str):
            raise CatalogError(f"{repo}: missing default branch")
        paths = sorted(
            {
                agent["runnable"]["entrypoint_path"]
                for agent in agents
                if agent["code"]["repo"] == repo
            }
        )
        missing_paths = [
            path for path in paths if not github_path_exists(repo, path, default_branch)
        ]
        if missing_paths:
            raise CatalogError(f"{repo}: missing runnable paths: {', '.join(missing_paths)}")
        github[repo] = {
            "url": payload.get("html_url"),
            "stars": payload.get("stargazers_count"),
            "forks": payload.get("forks_count"),
            "open_issues": payload.get("open_issues_count"),
            "archived": payload.get("archived"),
            "created_at": payload.get("created_at"),
            "pushed_at": payload.get("pushed_at"),
            "default_branch": default_branch,
            "license_spdx": actual_license,
            "verified_entrypoint_paths": paths,
        }

    citations: dict[str, Any] = {}
    for agent in agents:
        if not agent.get("paper"):
            continue
        print(f"OpenAlex: {agent['id']}", file=sys.stderr)
        citations[agent["id"]] = citation_snapshot(agent)

    retrieved_at = (
        datetime.now(timezone.utc)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z")
    )
    snapshot = {
        "schema_version": "1.0",
        "snapshot_date": snapshot_date,
        "retrieved_at": retrieved_at,
        "sources": {
            "github": "https://api.github.com",
            "openalex": "https://api.openalex.org",
            "citation_method": (
                "For each cataloged paper identity, count the union of OpenAlex works "
                "that cite any curated preprint or published-version work ID."
            ),
            "star_method": "Official GitHub repository stargazer count at retrieval time.",
        },
        "github": github,
        "citations": citations,
    }
    output.write_text(
        json.dumps(snapshot, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return output


def latest_snapshot() -> dict[str, Any]:
    paths = sorted(SNAPSHOT_DIR.glob("????-??-??.json"))
    if not paths:
        raise CatalogError("no metric snapshot found")
    snapshot = load_json(paths[-1])
    if snapshot.get("snapshot_date") != paths[-1].stem:
        raise CatalogError(f"{paths[-1].name}: snapshot_date does not match filename")
    return snapshot


def percentile_ranks(values: list[float]) -> list[float]:
    if not values:
        return []
    if len(values) == 1:
        return [100.0]
    ordered = sorted(values)
    result = []
    for value in values:
        first = ordered.index(value)
        last = len(ordered) - 1 - ordered[::-1].index(value)
        average_rank = (first + last) / 2
        result.append(100.0 * average_rank / (len(values) - 1))
    return result


def year_ago(day: date) -> date:
    try:
        return day.replace(year=day.year - 1)
    except ValueError:
        return day.replace(year=day.year - 1, day=28)


def markdown_text(value: Any) -> str:
    return str(value).replace("|", r"\|").replace("\n", " ")


def format_integer(value: Any) -> str:
    return f"{int(value):,}"


def build_render_context() -> dict[str, Any]:
    fail_if_invalid(require_snapshot=True)
    catalog = load_yaml(DATA_FILE)
    notable = load_yaml(NOTABLE_FILE)
    resources = load_yaml(RESOURCES_FILE)
    snapshot = latest_snapshot()
    snapshot_day = date.fromisoformat(snapshot["snapshot_date"])
    established_cutoff = year_ago(snapshot_day)

    rows = []
    for agent in catalog["agents"]:
        repo_metrics = snapshot["github"][agent["code"]["repo"]]
        citation_metrics = snapshot["citations"].get(agent["id"])
        row = dict(agent)
        row["stars"] = repo_metrics["stars"]
        row["citations"] = citation_metrics["count"] if citation_metrics else None
        row["repo_pushed_at"] = repo_metrics["pushed_at"]
        row["release_day"] = date.fromisoformat(agent["release"]["date"])
        row["is_established"] = row["release_day"] <= established_cutoff
        row["evidence_links"] = " · ".join(
            f"[{item['label']}]({item['url']})" for item in agent["evidence"]
        )
        rows.append(row)

    established = [row for row in rows if row["is_established"]]
    star_values = [math.log1p(row["stars"]) for row in established]
    citation_values = [math.log1p(row["citations"] or 0) for row in established]
    star_percentiles = percentile_ranks(star_values)
    citation_percentiles = percentile_ranks(citation_values)
    for row, star_pct, citation_pct in zip(
        established, star_percentiles, citation_percentiles, strict=True
    ):
        row["impact_score"] = (star_pct + citation_pct) / 2
    established.sort(key=lambda row: (-row["impact_score"], row["name"].casefold()))

    emerging = [row for row in rows if not row["is_established"]]
    emerging.sort(key=lambda row: (-row["release_day"].toordinal(), row["name"].casefold()))

    return {
        "catalog": catalog,
        "snapshot": snapshot,
        "snapshot_date": snapshot["snapshot_date"],
        "retrieved_at": snapshot["retrieved_at"],
        "established_cutoff": established_cutoff.isoformat(),
        "established": established,
        "emerging": emerging,
        "notable": notable["notable"],
        "qualification_pending": notable["qualification_pending"],
        "resources": resources["resources"],
        "main_count": len(rows),
        "established_count": len(established),
        "emerging_count": len(emerging),
    }


def render_outputs(write: bool) -> dict[Path, str]:
    context = build_render_context()
    environment = Environment(
        loader=FileSystemLoader(TEMPLATE_DIR),
        undefined=StrictUndefined,
        autoescape=False,
        keep_trailing_newline=True,
        trim_blocks=True,
        lstrip_blocks=True,
    )
    environment.filters["md"] = markdown_text
    environment.filters["intfmt"] = format_integer
    outputs = {}
    for template_name, target in README_TARGETS.items():
        rendered = environment.get_template(template_name).render(**context)
        if not rendered.endswith("\n"):
            rendered += "\n"
        outputs[target] = rendered
        if write:
            target.write_text(rendered, encoding="utf-8")
    return outputs


def check_generated() -> None:
    outputs = render_outputs(write=False)
    stale = []
    for target, expected in outputs.items():
        actual = target.read_text(encoding="utf-8") if target.exists() else None
        if actual != expected:
            stale.append(target.relative_to(ROOT).as_posix())
    if stale:
        raise CatalogError(
            "generated files are stale: "
            + ", ".join(stale)
            + "; run python scripts/catalog.py render"
        )


def command_validate(_: argparse.Namespace) -> None:
    fail_if_invalid(require_snapshot=True)
    print("Catalog and latest snapshot are valid.")


def command_refresh(args: argparse.Namespace) -> None:
    output = refresh_snapshot(args.date, force=args.force)
    print(f"Wrote {output.relative_to(ROOT)}")


def command_render(_: argparse.Namespace) -> None:
    outputs = render_outputs(write=True)
    print("Rendered " + ", ".join(path.name for path in outputs))


def command_check(_: argparse.Namespace) -> None:
    check_generated()
    print("Generated files are current.")


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description=__doc__)
    subparsers = result.add_subparsers(dest="command", required=True)

    validate_parser = subparsers.add_parser("validate", help="validate data and latest snapshot")
    validate_parser.set_defaults(handler=command_validate)

    refresh_parser = subparsers.add_parser("refresh", help="capture GitHub and OpenAlex metrics")
    refresh_parser.add_argument(
        "--date",
        default=datetime.now(timezone.utc).date().isoformat(),
        help="UTC snapshot date in YYYY-MM-DD form",
    )
    refresh_parser.add_argument(
        "--force",
        action="store_true",
        help="replace an existing snapshot for the same date",
    )
    refresh_parser.set_defaults(handler=command_refresh)

    render_parser = subparsers.add_parser("render", help="render both README files")
    render_parser.set_defaults(handler=command_render)

    check_parser = subparsers.add_parser("check", help="check generated README files")
    check_parser.set_defaults(handler=command_check)
    return result


def main() -> int:
    args = parser().parse_args()
    try:
        args.handler(args)
    except CatalogError as error:
        print(error, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
