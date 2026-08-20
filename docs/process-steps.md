# Process Steps

Process steps define the individual court, agency, filing, service, hearing, deadline, and follow-up actions inside a Pro-One workflow.

A workflow explains the overall path.

A process step explains one part of that path.

## Purpose

Process-step definitions help Pro-One avoid giving vague or unsafe process guidance.

They help answer:

- what step is being explained
- which workflow the step belongs to
- where the step appears in the sequence
- who usually performs the step
- which sources support the step
- what information may be needed
- what documents are involved
- whether deadlines matter
- what Pro-One may explain
- what Pro-One must not do
- when human help is needed
- what tests are required before support

This keeps court, agency, and document guidance structured and reviewable.

## Files

This foundation consists of three process-step files:

- `schemas/process-step.schema.json`
- `data/sample-process-steps.json`
- `docs/process-steps.md`

The schema defines the expected structure for process-step records.

The sample data shows example process steps using placeholder jurisdictions, sources, workflows, and institutions.

The documentation explains how process steps should be reviewed and used.

## Current status

This is an early technical foundation.

The sample process steps are not approved production steps.

They are examples only.

They should not be treated as supported Pro-One guidance or user-facing legal-information flows.

## Process-step records

Each process-step record should describe one step within a legal-information workflow.

A process step may cover tasks such as:

- reviewing court instructions
- checking eligibility information
- gathering information
- completing a form
- drafting a document
- filing a document
- paying a fee
- requesting a fee waiver
- serving documents
- providing notice
- waiting for a response
- preparing for a hearing
- attending a hearing
- receiving an order
- following up after an order
- submitting an agency application
- renewing an agency filing
- seeking review or appeal information

A step should not be approved unless its source support, sequence, deadline handling, document boundaries, and risk limits are clear.

## Required metadata

Each process-step record requires:

- `id`
- `title`
- `description`
- `status`
- `workflow_ids`
- `step_type`
- `sequence`
- `jurisdiction`
- `sources`
- `actor`
- `inputs`
- `actions`
- `documents`
- `deadline`
- `safety`
- `review`
- `evaluation`

These fields are required because process guidance can mislead users if it is out of order, unsupported, jurisdictionally unclear, or missing deadline and safety limits.

## Step status

Process-step status values include:

- `proposed`
- `researched`
- `designed`
- `tested`
- `supported`
- `deprecated`
- `rejected`

A proposed process step is not a supported process step.

A process step should not become supported until source review, workflow review, safety review, and evaluation requirements support that status.

## Workflow connection

The `workflow_ids` field connects a process step to one or more workflows.

For example, a filing step may belong to a name-change workflow, a small claims workflow, or another court-process workflow.

A process step should not float on its own.

It should support a defined workflow and inherit that workflow's scope and limits.

## Step type

The `step_type` field explains what kind of process step is being described.

Examples include:

- `review_instructions`
- `complete_form`
- `draft_document`
- `file_document`
- `serve_document`
- `provide_notice`
- `prepare_for_hearing`
- `attend_hearing`
- `agency_submission`
- `follow_up`

Step type helps Pro-One understand what kind of guidance is allowed and what risks may exist.

## Sequence

The `sequence` field explains where the step usually appears.

It tracks:

- position
- whether the step is generally required
- dependencies
- next steps
- sequence notes

Legal processes often depend on order.

A filing step may depend on completing forms.

A hearing step may depend on receiving notice.

A service step may depend on filing or issuance.

Pro-One should not present steps as fixed when the order may vary by court, agency, or matter type.

## Jurisdiction

The `jurisdiction` field explains where the step applies.

A step may be tied to:

- a country
- a state
- a locality
- a court
- an agency

A process step that applies in one court, agency, or jurisdiction should not be presented as generally valid elsewhere.

When jurisdiction is uncertain, the step should remain proposed or needs review.

## Sources

The `sources` field connects a step to source metadata.

A process step may require sources such as:

- court instructions
- court forms
- agency guidance
- statutes
- court rules
- official self-help materials
- legal aid resources

A process step should not be supported unless its required sources have been reviewed for authority, jurisdiction, freshness, access, reuse rights, and workflow fit.

Source IDs should match records defined under source metadata.

## Actor

The `actor` field explains who usually performs or controls the step.

Actors may include:

- user
- court
- agency
- opposing party
- third party
- lawyer or legal aid
- other

This matters because Pro-One should not imply that the user controls something controlled by a court, agency, or opposing party.

For example, a user may file a document, but the court controls acceptance, scheduling, and orders.

## Inputs

The `inputs` field defines what information may be needed for the step.

It tracks:

- required inputs
- optional inputs
- excluded inputs
- whether sensitive data is collected
- data-minimization notes

Pro-One should ask only what is needed to explain the step safely.

Process steps should avoid collecting unnecessary personal, financial, health, immigration, business, or court-case information.

## Actions

The `actions` field defines what Pro-One may explain and what it must not do.

Allowed actions may include:

- explaining a process step
- providing a checklist
- pointing users to reviewed sources
- flagging missing information
- explaining that court or agency instructions should be reviewed

Prohibited actions may include:

- filing documents for the user
- guaranteeing acceptance or approval
- choosing legal strategy
- hiding required information
- calculating unsupported deadlines
- replacing human review when the issue is complex or urgent

This field helps keep Pro-One informational rather than acting as a legal representative.

## Documents

The `documents` field explains which documents are connected to a step and what kind of document help is allowed.

Document help may include:

- none
- explanation
- checklist
- outline
- `user_confirmed_draft`
- review prompt

A step may involve a document without allowing Pro-One to generate a filing-ready draft.

For example, a filing step may allow a checklist and review prompt, but not a final legal sufficiency determination.

More detailed document rules will be handled by `legal-document.schema.json`.

## Deadlines

The `deadline` field is one of the most important safety controls.

It tracks:

- whether deadlines may matter
- how deadlines should be handled
- which sources support deadline information
- deadline notes

Deadline handling values include:

- `not_applicable`
- `awareness_only`
- `source_backed_information`
- `qualified_review_required`
- `unsupported`

Pro-One should not guess deadlines.

When deadlines matter, the step should require reviewed source support, human review, or clear escalation.

## Safety

The `safety` field defines risk controls for the step.

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

The `review` field tracks whether the process step has been reviewed.

Review statuses include:

- `proposed`
- `needs_review`
- `reviewed`
- `approved`
- `deprecated`
- `rejected`

Process-step review should consider:

- source support
- workflow fit
- jurisdiction clarity
- sequence accuracy
- actor responsibility
- input minimization
- document boundaries
- deadline handling
- safety and escalation
- evaluation coverage

A step should be rejected or delayed if it cannot be safely bounded.

## Evaluation

The `evaluation` field defines testing requirements before a process step can be supported.

Evaluation should test whether the step:

- uses source IDs correctly
- respects workflow scope
- identifies jurisdiction limits
- avoids legal advice
- avoids unsupported deadline calculations
- avoids outcome guarantees
- collects only necessary data
- catches escalation triggers
- refuses or narrows unsafe requests
- produces only allowed guidance

Known failure modes should be written down before the step becomes user-facing.

## Relationship to source metadata

Source metadata defines what Pro-One may rely on.

Process steps define how source-backed information appears inside a legal process.

A process step should not be approved unless its required sources are identified and reviewed.

A source should not be attached to a process step unless it actually supports that step.

## Relationship to workflow definitions

Workflow definitions explain the overall supported path.

Process-step definitions explain the parts of that path.

A workflow may include several process steps.

A process step should remain consistent with the workflow's scope, outputs, safety limits, and evaluation requirements.

## Relationship to legal-document schema

Many process steps involve documents.

Examples include:

- court forms
- petitions
- answers or responses
- demand letters
- certificates of service
- fee waiver requests
- agency applications
- business document checklists

Process steps can identify document involvement and document-help limits.

The `legal-document.schema.json` schema defines document structure, required user facts, legal-rule support, drafting boundaries, review prompts, and filing or sending cautions.

## Placeholder sample data

`data/sample-process-steps.json` uses placeholder workflows, jurisdictions, sources, and institutions.

The sample process steps are meant to demonstrate structure only.

They are not approved Pro-One process steps.

They should not be used as user-facing legal-information guidance.

## Adding a real process step

Before adding a real process step, check:

- Which workflow does this step support?
- What type of step is it?
- Where does it appear in the sequence?
- What must happen before it?
- What usually happens after it?
- Which jurisdiction applies?
- Which source supports it?
- Who controls the step?
- What information is needed?
- What information should not be collected?
- What documents are involved?
- Is document help allowed?
- Do deadlines matter?
- What deadline handling is allowed?
- What risks require escalation?
- What actions are prohibited?
- What tests are required?

A process step should stay in proposed or needs-review status until these questions are answered.

## Guiding rule

A Pro-One process step should be sourced enough to verify, narrow enough to explain safely, and limited enough to avoid misleading users.

Pro-One should define process steps before building court, agency, filing, hearing, deadline, or document guidance around them.
