# Development Setup

Pro-One is currently an architecture, specification, and technical-foundation repository. It contains interoperable JSON Schemas, fictional sample records, validation tooling, issue templates, and standards for sources, safety, privacy, governance, workflows, responses, and evaluation. It does not contain a production application, backend, frontend, database, or AI pipeline.

## Prerequisites

- Git
- Python 3.10 or later
- a code editor and terminal
- a GitHub account if you plan to open a pull request

## Clone the repository

```bash
git clone https://github.com/pro-one-org/pro-one.git
cd pro-one
```

## Install validation dependencies

Use a virtual environment if desired, then install the single development dependency:

```bash
python -m pip install -r requirements-dev.txt
```

On Windows, `py -m pip` and `py scripts/validate_repository.py` may be used when the Python launcher is available.

## Run repository validation

Run the same validation used by continuous integration:

```bash
python -B -m unittest discover --start-directory tests --verbose
python scripts/validate_repository.py
```

The standalone tests confirm that relative schema references resolve through a standard Draft 2020-12 validator without the repository's in-memory registry, enforce supported evaluation-fixture invariants, distinguish supporting dependencies from negative/test references, and keep generated environment directories out of repository scans.

The repository validator checks:

- every JSON file parses as UTF-8 JSON
- every schema is valid JSON Schema Draft 2020-12
- each sample record validates against its corresponding schema
- every schema-declared typed cross-record ID field is classified and resolves
- supporting dependencies satisfy lifecycle rules while negative/test references remain non-supporting
- supported-state and review/source invariants hold
- Markdown fences, relative links, and common encoding problems
- stale repository and PR-history wording covered by the automated checks

Schema `$id` values are portable filenames, and domain schemas reference the sibling `common.schema.json` with relative `$ref` values. Tools that accept schema file paths should use the `schemas/` directory as the retrieval base.

Before committing, also run:

```bash
git diff --check
git status --short
```

## How schemas and records fit together

The nine record domains under [`schemas/`](../schemas/) correspond to the nine `data/sample-*.json` files. Shared concepts live in [`schemas/common.schema.json`](../schemas/common.schema.json) and are referenced by the domain schemas.

All sample records are fictional placeholders. A valid proposed record is not necessarily reviewed, approved, or supported. The `schema_version`, `record_version`, and `last_modified` fields provide a migration path; review provenance records the exact `reviewed_record_version` when a review occurs.

## Add or change a record

1. Choose the correct domain schema and sample-data file.
2. Use a stable lowercase identifier matching the common identifier format.
3. Set accurate version metadata. Increment `record_version` when record content changes materially.
4. Add only real relationships to records that exist in the repository.
5. Keep placeholder records `proposed` with null review provenance until an actual review occurs.
6. Update related records where the relationship is reciprocal or otherwise documented.
7. Update the relevant Markdown documentation.
8. Run repository validation.

Do not invent reviewer identities, review dates, professional credentials, source versions, effective dates, or hashes.

## Change a schema or shared enum

Changes to [`schemas/common.schema.json`](../schemas/common.schema.json) can affect several domains at once. Before changing shared maturity states, review states, risk levels, urgency, support modes, routing behavior, deadline handling, or human-help framing:

1. search all schemas, data, and documentation for the existing term
2. confirm the concepts are genuinely semantically identical
3. preserve separate definitions when the concepts differ
4. update every affected schema, record, validator rule, issue template, and document together
5. describe migration impact in the pull request

## Branches and pull requests

Do not make contribution work directly on `main`.

```bash
git switch main
git pull --ff-only origin main
git switch -c docs/example-change
```

Keep changes narrow and reviewable. A pull request should explain what changed, why it is useful, whether it affects legal information, sources, safety, privacy, evaluation, or user-facing boundaries, and how it was validated.

Useful branch prefixes include `docs/`, `schema/`, `tests/`, `fix/`, and `refactor/`.

## Secrets and sensitive information

Do not commit API keys, credentials, private user data, real legal documents, confidential business records, sensitive prompts or outputs, or environment files containing secrets. The repository does not need real user facts to test its current specification layer.

## Guiding rule

Keep schemas, sample records, documentation, and validation synchronized. A machine-valid record may still be unsafe or legally inappropriate; supported status requires the additional review and evaluation gates documented by the project.
