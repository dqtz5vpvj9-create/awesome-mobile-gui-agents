# Methodology

This document defines the catalog boundary, evidence requirements, audit vocabulary, and metric snapshot procedure. The goal is a small, defensible list rather than exhaustive paper coverage.

## Unit of inclusion

The main unit is a named, meaningfully runnable Mobile GUI Agent. An entry may be:

- an academic agent with official execution code;
- an open-source software agent or automation framework with a genuine agent loop;
- a runnable baseline embedded in a benchmark repository;
- a distinct released generation inside a shared agent-family repository.

Multiple generations can be separate entries when each has its own identifiable runtime path and materially different architecture. Repository stars are then marked family-level.

The following are not main entries by themselves:

- model weights or offline model inference;
- datasets or failure trajectories;
- supervised or reinforcement-learning recipes;
- benchmarks and environments without an agent implementation;
- closed-source systems;
- source-available projects whose terms are not an open-source software license;
- repositories that promise code but do not contain the implementation.

Those resources can appear in the associated-resource or pending sections.

## Main-list requirements

Every main entry needs:

1. an official public source repository;
2. an explicit open-source license detected at the repository root;
3. a documented runnable path whose file or directory exists;
4. Android, iOS, or HarmonyOS GUI operation;
5. benchmark evidence or a concrete real-device demo;
6. a release date and its provenance basis;
7. an audit status and date;
8. a concise inclusion rationale and limitation.

Star count is never an inclusion threshold. Small projects can qualify when the runtime and evidence are unusually relevant; popular repositories can fail when licensing or implementation completeness is unclear.

## Release dates

The catalog records one of three bases:

- paper-first-public: first public paper or preprint date for an academic agent;
- code-repository-created: official repository creation date when no earlier agent release is verifiable;
- official-release: a dated release announcement or tag.

The date determines Established versus Emerging placement. Established means at least 12 months old at the metric snapshot.

## Papers and citation identity

Papers are resolved to curated OpenAlex work IDs. A preprint and its published version can remain separate OpenAlex records, so the snapshot does not simply add their cited-by counts. It asks OpenAlex for the union of works citing any curated identity and records that union count.

This avoids double counting a citing paper that references both versions. It also preserves all component work metadata in the snapshot for inspection.

Entries without a paper show no citation count.

## GitHub identity

Only the official repository is used. Forks, mirrors, package registries, organization totals, and copied implementations are excluded from the star metric.

When several agent generations share a repository, every generation displays the same repository-level count with a family marker. The count must not be interpreted as adoption of one generation.

## Audit levels

Audit status is cumulative:

1. links-verified: official repository, root license, paper, evidence links, and runnable path were checked;
2. code-inspected: the relevant implementation files and agent loop were additionally inspected;
3. install-smoke-tested: documented installation and a minimal launch were executed successfully.

The boolean install_smoke_tested can only be true at the third level. An entry never inherits a stronger status from another generation in the same monorepository.

## Recovery vocabulary

Recovery is one field, not the catalog scope:

- none-documented: no dedicated recovery behavior is documented;
- retry: refreshed observation followed by another action or bounded retry;
- reflection: explicit outcome critique or action reflection;
- replanning: a failed or changed state can cause plan or subtask revision;
- backtracking: explicit return to an earlier branch or state is part of the mechanism;
- unknown: public evidence is insufficient to classify it.

These labels describe mechanisms, not comparable performance tiers. A reflection label does not imply successful state restoration, and UI navigation recovery does not imply rollback of irreversible external side effects.

## Snapshot procedure

The refresh command:

1. validates catalog structure;
2. fetches each unique repository from the official GitHub API;
3. verifies the detected SPDX license and every runnable path;
4. fetches curated OpenAlex work records;
5. computes union-deduplicated citations;
6. writes a dated immutable JSON snapshot;
7. renders English and Chinese READMEs from that snapshot.

The scheduled workflow opens a pull request once per month. A human checks unexpected license, path, identity, or metric changes before merging. Historical snapshots are never rewritten in normal operation.

## Known limitations

- OpenAlex can under-index recent or venue-specific citations.
- GitHub stars measure attention, not scientific validity or runtime quality.
- links-verified does not prove installation succeeds.
- Official demos and project-maintained benchmark pages are not independent replication.
- A repository can change after a snapshot; every count and audit claim is date-bound.
- The list is intentionally incomplete. A high-quality candidate remains outside the main list until all required evidence is verifiable.
