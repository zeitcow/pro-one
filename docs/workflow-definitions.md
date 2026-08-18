# Workflow Definitions

Pro-One workflows define what the project can help with, what sources are required, what outputs are allowed, and what safety limits apply.

A workflow is not just a topic.

A workflow is a reviewed, bounded legal-information path for a specific user need.

## Purpose

Workflow definitions help Pro-One avoid vague or unsafe legal AI behavior.

They help answer:

- what legal-information task is being supported
- who the workflow is designed for
- which jurisdiction applies
- which sources are required
- what the workflow may explain
- what the workflow must not do
- what information the user may be asked for
- what outputs are allowed
- what risks require escalation
- what tests are required before support

This keeps Pro-One grounded, narrow, and reviewable.

## Files

This PR introduces three workflow-definition files:

- `schemas/workflow.schema.json`
- `data/sample-workflows.json`
- `docs/workflow-definitions.md`

The schema defines the expected structure for workflow records.

The sample data shows example workflow records using placeholder jurisdictions, sources, and institutions.

The documentation explains how workflow definitions should be reviewed and used.

## Current status

This is an early technical foundation.

The sample workflows are not approved production workflows.

They are examples only.

They should not be treated as supported Pro-One workflows or user-facing legal-information flows.

## Workflow records

Each workflow record should describe one legal-information workflow.

A workflow may cover tasks such as:

- understanding a court process
- preparing for a filing step
- reviewing a document checklist
- understanding a small business agency process
- organizing facts for a demand letter
- explaining source-backed next steps
- identifying when human help is needed

A workflow should not be approved unless its scope, source needs, risk limits, and evaluation requirements are clear.

## Required metadata

Each workflow record requires:

- `id`
- `title`
- `description`
- `status`
- `user_types`
- `legal_area`
- `topics`
- `jurisdiction`
- `scope`
- `sources`
- `intake`
- `process`
- `outputs`
- `safety`
- `review`
- `evaluation`

These fields are required because a workflow cannot be safely supported without knowing who it helps, where it applies, which sources support it, what it may output, and what risks it must avoid.

## Workflow status

Workflow status values include:

- `proposed`
- `researched`
- `designed`
- `tested`
- `supported`
- `deprecated`
- `rejected`

A proposed workflow is not a supported workflow.

A workflow should not become supported until source review, safety review, and evaluation requirements support that status.

## User types

The `user_types` field explains who the workflow is designed to help.

Supported user types include:

- `self_represented_individual`
- `small_business_owner`
- `small_business_operator`
- `nonprofit_operator`
- `legal_aid_helper`
- `other`

A workflow should be clear about its intended user because different users have different needs, risks, and assumptions.

## Jurisdiction

The `jurisdiction` field explains where the workflow applies.

A workflow may be tied to:

- a country
- a state
- a locality
- a court
- an agency

Legal-information workflows should not blur jurisdictions.

A workflow that applies in one court, agency, or state should not be presented as generally valid elsewhere.

When jurisdiction is uncertain, the workflow should remain proposed or needs review.

## Scope

The `scope` field defines what the workflow may and may not do.

Each workflow must state that it provides legal information only.

The schema requires:

- purpose
- legal-information-only status
- included tasks
- excluded tasks

This is one of the most important safety controls in Pro-One.

A workflow should clearly say what it supports and what it does not support.

For example, a court-process workflow may explain filing steps, but should not choose strategy, guarantee outcomes, or calculate deadlines without reviewed rules.

## Sources

The `sources` field connects a workflow to source metadata.

A workflow may require sources such as:

- court instructions
- court forms
- statutes
- rules
- agency guidance
- legal aid resources
- official self-help pages

A workflow should not be supported unless its required sources have been reviewed for authority, jurisdiction, freshness, access, reuse rights, and workflow fit.

Source IDs should match records defined under source metadata.

## Intake

The `intake` field defines what the workflow may ask the user.

It tracks:

- required inputs
- optional inputs
- excluded inputs
- whether sensitive data is collected
- data-minimization notes

Pro-One should ask only what is needed to determine workflow fit and provide safe legal information.

Workflows should avoid collecting unnecessary personal, financial, health, immigration, or case-specific information.

## Process

The `process` field explains which legal, court, or agency process steps the workflow may cover.

It tracks:

- connected process-step IDs
- plain-language steps
- deadline handling
- process notes

Deadline handling is especially important.

A workflow should not guess deadlines.

When deadlines matter, the workflow should require source-backed rules, human review, or clear escalation.

## Outputs

The `outputs` field defines what the workflow may generate.

Allowed outputs may include:

- information summaries
- step-by-step guides
- checklists
- document outlines
- document drafts
- form guidance
- citation summaries
- referral prompts

Prohibited outputs may include:

- legal opinions
- guaranteed outcomes
- unsupported deadline calculations
- case strategy
- final filing decisions
- emergency advice
- unsupported documents

This field helps Pro-One support drafting carefully.

A workflow may allow document help only when the workflow, sources, intake, and safety rules support that output.

## Document drafting

Workflow definitions can support future drafting of legal documents, but only with clear limits.

A workflow may allow drafting or outlining documents such as:

- court forms
- petitions
- answers or responses
- demand letters
- simple agreements
- business document checklists
- agency application materials

But the workflow should define:

- what document types are allowed
- what user facts are required
- what sources support the document
- what legal statements must be cited
- what warnings must appear
- what the user must review before filing or sending
- when human help is needed

Document generation should be source-grounded and based on user-provided facts.

It should not invent facts, guarantee legal sufficiency, or decide strategy for the user.

## Safety

The `safety` field defines workflow risk controls.

It tracks:

- risk level
- escalation triggers
- refusal triggers
- required warnings
- safety notes

Escalation triggers tell Pro-One when the user should be directed toward legal aid, court help, a lawyer, or another human resource.

Refusal triggers tell Pro-One when to refuse, narrow, or redirect a request.

Required warnings help ensure user-facing responses do not overstate what Pro-One can do.

## Review

The `review` field tracks whether the workflow has been reviewed.

Review statuses include:

- `proposed`
- `needs_review`
- `reviewed`
- `approved`
- `deprecated`
- `rejected`

Workflow review should consider:

- source support
- jurisdiction clarity
- user need
- scope limits
- legal advice boundary
- privacy and data minimization
- process accuracy
- output limits
- risk and escalation
- evaluation coverage

A workflow should be rejected or delayed if it cannot be safely bounded.

## Evaluation

The `evaluation` field defines testing requirements before a workflow can be supported.

Evaluation should test whether the workflow:

- uses approved or proposed sources correctly
- identifies jurisdiction limits
- avoids legal advice
- avoids unsupported deadline calculations
- avoids outcome guarantees
- collects only necessary data
- catches escalation triggers
- refuses or narrows unsafe requests
- produces allowed outputs only

Known failure modes should be written down before the workflow becomes user-facing.

## Relationship to source metadata

Source metadata defines what Pro-One may rely on.

Workflow definitions define what Pro-One may help with.

A workflow should not be approved unless its required sources are identified and reviewed.

A source should not be attached to a workflow unless it actually supports that workflow.

## Relationship to future schemas

Workflow definitions will connect to later schemas, including:

- `process-step.schema.json`
- `legal-document.schema.json`
- `intake.schema.json`
- `legal-rule.schema.json`
- `risk.schema.json`
- `evaluation-fixture.schema.json`
- `response.schema.json`

Together, these schemas can support a legal-information system that is structured, source-grounded, and safety-aware.

## Placeholder sample data

`data/sample-workflows.json` uses placeholder jurisdictions, sources, and institutions.

The sample workflows are meant to demonstrate structure only.

They are not approved Pro-One workflows.

They should not be used as user-facing legal-information flows.

## Adding a real workflow

Before adding a real workflow, check:

- Who is the workflow for?
- What legal area does it cover?
- Which jurisdiction applies?
- What user problem does it solve?
- What sources support it?
- Are the sources reviewed?
- What does the workflow include?
- What does the workflow exclude?
- What information must the user provide?
- What information should not be collected?
- What outputs are allowed?
- What outputs are prohibited?
- What risks require escalation?
- What tests are required?

A workflow should stay in proposed or needs-review status until these questions are answered.

## Guiding rule

A Pro-One workflow should be narrow enough to review, sourced enough to verify, and limited enough to protect users.

Pro-One should define workflows before building user-facing legal AI features around them.
