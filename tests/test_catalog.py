from __future__ import annotations

import importlib.util
from collections import Counter
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("catalog", ROOT / "scripts" / "catalog.py")
assert SPEC and SPEC.loader
catalog = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(catalog)


def load_yaml(name: str):
    with (ROOT / "data" / name).open(encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def test_catalog_and_snapshot_validate():
    assert catalog.validate_catalog(require_snapshot=True) == []


def test_main_list_has_at_least_twenty_unique_agents():
    agents = load_yaml("agents.yaml")["agents"]
    ids = [agent["id"] for agent in agents]
    assert len(agents) >= 20
    assert len(ids) == len(set(ids))


def test_main_entries_are_open_runnable_and_audited():
    agents = load_yaml("agents.yaml")["agents"]
    for agent in agents:
        assert agent["license"]["status"] == "open-source"
        assert agent["license"]["spdx"]
        assert agent["runnable"]["entrypoint_path"]
        assert agent["runnable"]["entrypoint_url"].startswith("https://github.com/")
        assert agent["audit"]["date"]
        assert agent["audit"]["status"] in catalog.ALLOWED_AUDIT_STATUSES
        assert agent["evidence"]


def test_shared_repository_star_scope_is_explicit():
    agents = load_yaml("agents.yaml")["agents"]
    counts = Counter(agent["code"]["repo"] for agent in agents)
    for agent in agents:
        expected = "family-level" if counts[agent["code"]["repo"]] > 1 else "repository-level"
        assert agent["code"]["stars_scope"] == expected


def test_paper_aliases_are_unique_within_each_entry():
    agents = load_yaml("agents.yaml")["agents"]
    for agent in agents:
        if agent["paper"]:
            ids = agent["paper"]["openalex_ids"]
            assert len(ids) == len(set(ids))


def test_resources_are_not_counted_as_main_agent_names():
    main_names = {agent["name"] for agent in load_yaml("agents.yaml")["agents"]}
    resource_names = {item["name"] for item in load_yaml("resources.yaml")["resources"]}
    assert main_names.isdisjoint(resource_names)


def test_readmes_are_deterministically_generated():
    catalog.check_generated()


def test_emerging_entries_are_unranked_and_newest_first():
    context = catalog.build_render_context()
    emerging_dates = [row["release_day"] for row in context["emerging"]]
    assert emerging_dates == sorted(emerging_dates, reverse=True)
    assert all("impact_score" not in row for row in context["emerging"])
