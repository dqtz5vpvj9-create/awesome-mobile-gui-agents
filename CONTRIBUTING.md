# Contributing

Thanks for helping keep this catalog small, accurate, and useful.

## Suggesting a new agent

Open a Suggest an agent issue. Do not start with a catalog pull request.

The issue must provide:

- official project and code links;
- release date and evidence for that date;
- root software license;
- exact runnable entrypoint and installation guide;
- supported mobile platforms;
- perception and action interfaces;
- benchmark or real-device demo evidence;
- paper and venue, if one exists;
- a concise reason the project is a complete agent rather than a model, dataset, training recipe, or environment;
- known limitations.

A maintainer will classify the proposal as main-list candidate, associated resource, qualification pending, code pending, or out of scope. Once the issue is accepted, a data pull request can be prepared.

## Corrections

Corrections to an existing entry, schema, generator, tests, or documentation are welcome. Link the pull request to an issue when the change affects inclusion, license status, paper identity, audit level, or substantive capability claims.

Do not manually edit generated README tables. Update structured data or templates and run:

~~~bash
python scripts/catalog.py render
python scripts/catalog.py validate
python scripts/catalog.py check
pytest
~~~

## Evidence style

- Prefer official repositories, papers, publisher pages, and benchmark artifacts.
- Avoid promotional superlatives unless clearly attributed to a project source.
- Separate verified facts from interpretation.
- Never infer an open-source license from public code alone.
- Never promote an audit level without performing the required work.
- Treat recovery, safety, planning, memory, and grounding as distinct capabilities.

## Metric updates

Routine GitHub and OpenAlex metric changes come through the scheduled refresh pull request. Do not hand-edit a snapshot. If a paper identity is incomplete, correct its curated OpenAlex IDs first and create a new dated snapshot.

## Review expectations

Catalog changes require human review because automated checks can confirm structure and links but cannot decide whether an implementation is a complete Mobile GUI Agent. Maintainers may keep a project in a pending section until licensing, runtime completeness, or official ownership is unambiguous.
