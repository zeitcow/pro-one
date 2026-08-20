# Contributing to Pro-One

Pro-One is an early-stage, free, open-source legal AI project. The repository currently provides an architecture and specification foundation; it does not contain a production legal AI application or publicly supported workflow.

## What contributors can work on now

- JSON Schemas and shared vocabulary
- fictional sample records and cross-record relationships
- source, workflow, safety, privacy, governance, and evaluation standards
- validation tooling and CI
- the proposed first-workflow specification
- small documentation and consistency improvements

Application implementation should be proposed separately and must not be presented as existing capability.

## Contribution principles

Contributions should be narrow, reviewable, source-grounded, jurisdiction-aware, privacy-conscious, explicit about uncertainty, and consistent with the project's legal-information boundary. Preserve fact integrity, refusal of fabrication or evidence destruction, safe continuation, citations, narrow supported scope, and the free-access mission.

Do not add real user legal documents, private facts, credentials, invented sources, fabricated review provenance, or claims that a proposed record is approved or supported.

## Schema and record changes

Each sample-data file corresponds to a domain schema. Shared concepts live in [`schemas/common.schema.json`](schemas/common.schema.json).

When adding or changing a record:

1. use a stable ID and accurate version metadata
2. keep placeholder records `proposed`
3. link only to IDs that exist
4. use null review fields until an actual review occurs
5. update reciprocal or documented relationships
6. update related documentation and examples
7. run repository validation

When changing a shared enum or definition, search every schema, sample record, issue template, validator rule, and Markdown file. Preserve separate vocabularies where concepts have different semantics—for example, harm severity, urgency, evaluation priority, and routing behavior.

## Legal-information and source standard

Legal propositions should be connected to current, verifiable authority appropriate to the proposition. Statutes, regulations, cases, and rules may support substantive legal propositions; official court rules, forms, and instructions may support filing and procedural requirements; official self-help and legal-aid resources may support plain-language explanation and navigation.

Proposed records and example.org URLs are not legal authority. A `legal_information_only` label does not by itself determine a workflow's legal or regulatory status. Public support requires workflow-specific, jurisdiction-specific review and evaluation. Do not imply attorney review unless it actually occurred and is accurately recorded.

## AI usage

AI-generated code, documentation, schemas, or legal explanations require careful human review. AI must not be used to invent cases, statutes, regulations, citations, source text, facts, reviewer identities, credentials, or approval history.

## Local validation

Follow [Development Setup](docs/development-setup.md), then run:

```bash
python -m pip install -r requirements-dev.txt
python -B -m unittest discover --start-directory tests --verbose
python scripts/validate_repository.py
git diff --check
```

## Pull request expectations

A pull request should explain:

- what changed and why
- which schemas, records, relationships, or standards are affected
- whether legal information, sources, jurisdiction, safety, privacy, evaluation, or user-facing boundaries changed
- any migration or shared-enum impact
- how the change was reviewed and validated

## Legal boundary

Pro-One is not a law firm or lawyer, does not form an attorney-client relationship, and does not currently provide legal services. Contributions must not imply otherwise or make legal or factual decisions for users.
