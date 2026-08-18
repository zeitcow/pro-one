# Source Metadata

Pro-One should treat legal sources as structured project assets, not loose links.

This document explains the purpose of `schemas/source.schema.json`, how source records should be reviewed, and how sample source metadata should be used.

## Purpose

Source metadata helps Pro-One track:

- what a source is
- where it comes from
- which jurisdiction it applies to
- how authoritative it is
- whether it is free to access
- whether it can be reused
- when it was last checked
- which workflows it may support
- what limits or risks apply

Legal AI workflows should not rely on sources that are vague, stale, unsupported, or difficult to verify.

## Files

This PR introduces three source-metadata files:

- `schemas/source.schema.json`
- `data/sample-sources.json`
- `docs/source-metadata.md`

The schema defines the expected structure for source records.

The sample data shows example records using placeholder URLs and placeholder institutions.

The documentation explains how source metadata should be reviewed and used.

## Current status

This is an early technical foundation.

The sample records are not approved production sources.

They are examples only.

They should not be treated as real legal authority, reliable legal information, or supported workflow inputs.

## Source records

Each source record should describe one source.

A source may be:

- a statute
- a court rule
- a court form
- court instructions
- agency guidance
- official self-help material
- public legal aid material
- a recognized secondary source
- a court opinion
- another legal-information source

The goal is to describe the source clearly enough that a reviewer can decide whether it belongs in a workflow.

## Required metadata

Each source record requires:

- `id`
- `title`
- `source_type`
- `url`
- `jurisdiction`
- `authority`
- `dates`
- `access`
- `rights`
- `review`
- `workflow_fit`
- `citation`

These fields are required because a legal source cannot be responsibly used without knowing what it is, where it applies, how authoritative it is, whether it is current, and how it may be used.

## Identifier

The `id` field is a stable project identifier.

Examples:

- `example-state-court-name-change-guide`
- `example-city-small-business-license-guide`

Identifiers should be lowercase and stable.

They should not change only because a source title changes.

## Jurisdiction

The `jurisdiction` field explains where the source applies.

A source may apply to:

- a country
- a state
- a locality
- a court
- an agency

Legal workflows should not use jurisdiction-specific sources without identifying the jurisdiction.

When jurisdiction is uncertain, the source should not be used for confident legal information.

## Authority

The `authority` field explains how authoritative the source is.

Authority levels include:

- `official_primary`
- `official_secondary`
- `public_legal_aid`
- `recognized_secondary`
- `community_reference`
- `unknown`

Primary legal materials and official sources should generally receive more weight than secondary commentary.

A source with unknown authority should not be used as a source of truth.

## Dates and freshness

The `dates` field tracks freshness.

At minimum, each source record must include `last_checked`.

Other useful dates include:

- `published`
- `effective`
- `last_updated`

Legal sources can change. A source that was reliable at one time may become outdated.

Source review should include checking whether the source is still current.

## Access

The `access` field explains whether the source is available to users.

It tracks:

- whether the source is free
- whether it requires login
- the source format
- access notes

Pro-One should prefer sources that users can access directly without payment or unnecessary barriers.

## Rights

The `rights` field tracks reuse status.

Reuse categories include:

- `public_domain`
- `open_license`
- `link_only`
- `permission_required`
- `unknown`

A source may be reliable but still have reuse limits.

When reuse rights are uncertain, Pro-One should be conservative.

## Review status

The `review` field tracks whether a source has been reviewed.

Review statuses include:

- `proposed`
- `needs_review`
- `reviewed`
- `approved`
- `deprecated`
- `rejected`

A proposed source is not the same thing as an approved source.

A source should not be treated as workflow-ready until review supports that use.

## Workflow fit

The `workflow_fit` field explains how the source may be used.

It tracks:

- topics
- supported workflows
- risk level
- limitations
- uses the source should not support

A source may be useful for one workflow but unsafe for another.

For example, a general court self-help page may be useful for explaining process steps, but not for calculating deadlines or choosing case strategy.

## Citation metadata

The `citation` field tracks how the source should be cited or labeled.

It includes:

- preferred citation
- retrieval date
- archive URL, if available

Source-grounded workflows should preserve citation metadata so users can understand where information came from.

## Placeholder sample data

`data/sample-sources.json` uses placeholder URLs and placeholder institutions.

The sample records are meant to demonstrate structure only.

They are not real approved Pro-One sources.

Do not use sample records as legal authority.

Do not treat sample records as supported workflow inputs.

## Adding a real source

Before adding a real source, check:

- Is the source official or otherwise reliable?
- Which jurisdiction does it apply to?
- Is it current?
- Is it free to access?
- Does it require login?
- What reuse rights apply?
- Which workflow would use it?
- What risks exist if the source is misunderstood?
- What should the source not be used for?
- Has the source been reviewed?

If these questions cannot be answered, the source should stay in `proposed` or `needs_review` status.

## Source review

Source review should consider:

- authority
- accuracy
- freshness
- jurisdiction
- access
- reuse rights
- workflow fit
- risk level
- citation quality
- limitations

A source should be rejected or delayed if it cannot be verified, is outdated, has unclear authority, or creates unacceptable risk for users.

## Relationship to workflow selection

Source metadata and workflow selection should work together.

A workflow should not be approved unless the project has reliable sources for that workflow.

A source should not be approved for a workflow unless the workflow has clear scope, limits, and evaluation criteria.

## Future improvements

Future PRs may add:

- source validation scripts
- source review checklists
- real source records
- workflow source maps
- evaluation fixtures tied to sources
- automated freshness checks
- archive capture rules

These should be added carefully and reviewed before source metadata is used in user-facing workflows.

## Guiding rule

A legal AI project is only as trustworthy as the sources it can explain, verify, and limit.

Pro-One should build from structured, reviewable source metadata before relying on sources in workflows.
