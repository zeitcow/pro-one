# Intake Definitions

This document explains how Pro-One intake definitions work.

An intake definition controls what Pro-One may ask a user before giving legal-information support. Intake is not just a form. It is the routing layer that helps Pro-One understand the user's general legal matter, identify the workflow, ask only necessary questions, avoid collecting unnecessary sensitive information, and continue helping in the safest useful mode.

## Current status

The intake schema is an early technical foundation.

The current files are:

- `schemas/intake.schema.json`
- `data/sample-intakes.json`
- `docs/intake.md`

The sample intake records are placeholders. They are not approved production intake flows, user-facing legal guidance, legal advice, or court-specific instructions.

## Core principle

Pro-One should not abandon users because a matter is urgent, complicated, or high risk.

Risk routing does not mean stopping assistance. Risk routing means Pro-One continues in a safer, narrower, more source-grounded support mode.

For example, if a user says a discovery response is due tomorrow, Pro-One should not simply say that it cannot help. It should help the user identify the document type, organize the issue, understand possible process steps, review source-backed information when available, and build a practical checklist.

## Why intake matters

Intake affects:

- what Pro-One asks
- what Pro-One avoids asking
- what support mode Pro-One uses
- when Pro-One asks a clarifying question
- when Pro-One provides general information
- when Pro-One uses source-backed steps
- when Pro-One gives a checklist
- when Pro-One narrows the scope
- when Pro-One flags risk
- when Pro-One offers court, agency, legal aid, or free and low-cost resources
- when Pro-One refuses unsafe parts of a request while continuing to help with safe parts

A good intake flow should reduce confusion and user burden.

A bad intake flow may:

- ask too many questions
- collect unnecessary sensitive data
- miss deadline concerns
- miss court or agency context
- send users away too quickly
- imply that Pro-One has made a legal decision
- help with unsafe requests
- treat general information as court-specific guidance

## Intake is not a referral engine

Pro-One is designed to help individuals and small businesses get through legal matters without assuming that they can hire an attorney or pay out of pocket.

The intake schema should not use human help as the default answer.

Human help may be framed as:

- optional free or low-cost support
- a court self-help resource
- a legal aid resource
- a court clerk or agency information source
- a high-risk backup option
- an urgent option for extreme risk

The default should be continued safe support whenever possible.

## Safe continuation

Safe continuation means Pro-One keeps helping while respecting boundaries.

Safe continuation may include:

- general legal information
- source-backed process steps
- checklists
- document explanations
- issue spotting
- court or agency resource prompts
- free or low-cost resource prompts
- deadline awareness
- urgent support
- scope narrowing
- refusal of unsafe requests while continuing the safe parts

Safe continuation should not include:

- guaranteeing outcomes
- deciding legal strategy
- inventing facts
- making privilege determinations
- choosing objections for a user
- deciding whether evidence can be withheld
- telling a user to ignore a subpoena
- telling a user that a document is ready to file
- making unsupported deadline calculations
- giving final legal sufficiency determinations

## Intake types

The schema supports these intake categories:

- `general_legal_information`
- `workflow_selection`
- `jurisdiction_identification`
- `process_step_support`
- `document_support`
- `deadline_awareness`
- `urgent_support`
- `court_or_agency_navigation`
- `business_legal_information`
- `discovery_support`
- `subpoena_support`
- `other`

An intake definition should choose the most specific category that fits.

## Status values

Each intake definition has a status:

- `proposed`
- `researched`
- `designed`
- `tested`
- `supported`
- `deprecated`
- `rejected`

Most early intake records should stay `proposed` until they are reviewed, tested, and tied to real approved sources.

## Relationships to other schemas

Intake definitions connect to other Pro-One foundations.

### Source metadata

Source records define the legal, court, agency, or self-help materials that Pro-One may rely on.

Intake should avoid giving court-specific support unless the relevant source records support it.

### Workflow definitions

Workflow definitions describe the legal-information workflow Pro-One may support.

Intake helps choose or narrow the workflow.

### Process steps

Process-step records describe practical steps in a workflow.

Intake helps determine which process step is relevant.

### Legal documents

Legal-document records describe document categories, required facts, drafting limits, filing limits, service limits, deadline handling, privacy controls, and evaluation requirements.

Intake helps determine whether document support is appropriate and what facts are needed.

### Future legal-rule schema

Legal-rule records will define source-backed rule statements.

Intake should not create legal-rule claims on its own. It should route users to source-backed support when the rule foundation exists.

### Future risk schema

Risk records will define recurring risk situations and support routing.

The intake schema already includes risk signals, but the future risk schema will make those controls more reusable and consistent.

### Future evaluation-fixture schema

Evaluation fixtures will test intake flows.

They should check whether intake asks only necessary questions, avoids unnecessary sensitive data, routes urgent users safely, and does not abandon users.

### Future response schema

The response schema will define what a safe final answer should include.

Intake prepares the facts and support mode needed for the response.

## Intake goal

Each intake definition includes an `intake_goal` object.

The intake goal should explain:

- the primary purpose of the intake
- what Pro-One may help identify
- what Pro-One must not do
- how Pro-One should keep the user moving

Good intake goals are practical and narrow.

Example:

> Help the user identify whether they are dealing with interrogatories, requests for production, requests for admission, or another discovery request, then route them to deadline-aware checklist support.

Poor intake goal:

> Determine the user's legal rights and draft the correct response.

The second example is too broad and implies Pro-One is making legal decisions.

## Questions

The `questions` object controls what Pro-One may ask.

It includes:

- `required_questions`
- `optional_questions`
- `conditional_questions`
- `prohibited_questions`
- `clarification_strategy`

### Required questions

Required questions should be limited.

They should usually identify:

- the general matter type
- the jurisdiction or forum when needed
- the document or notice involved
- whether timing appears urgent
- what kind of help the user is seeking

Required questions should not collect unnecessary personal history.

### Optional questions

Optional questions may help, but they should not overwhelm the user.

They should be asked only when useful.

### Conditional questions

Conditional questions should depend on the user's answers.

For example:

- Ask about a minor only if the user says the issue involves a child.
- Ask about a subpoena response date only if the user says they received a subpoena.
- Ask about a motion to compel only if the user says discovery is overdue or the other side filed something.
- Ask about confidential records only if the matter appears to involve records.

### Prohibited questions

Prohibited questions help enforce data minimization and privacy.

Examples:

- Do not ask for Social Security numbers.
- Do not ask for full financial account numbers.
- Do not ask for privileged messages.
- Do not ask for full medical records unless a later approved workflow specifically supports that need.
- Do not ask for facts so Pro-One can invent a stronger story.
- Do not ask for unnecessary information about minors.

## Clarification strategy

The schema supports these clarification strategies:

- `ask_one_question_at_a_time`
- `ask_minimum_needed_questions`
- `offer_multiple_choice_when_possible`
- `continue_with_reasonable_general_information`
- `narrow_scope_before_answering`

The preferred strategy depends on the user's situation.

For urgent or stressful matters, asking one question at a time may be best.

For broad workflow selection, multiple choice may reduce burden.

For low-risk general information, Pro-One may continue with reasonable general information while noting what facts would help narrow the answer.

## Data limits

The `data_limits` object defines what data Pro-One may collect.

It includes:

- `minimum_necessary_only`
- `allowed_data_categories`
- `restricted_data_categories`
- `prohibited_data_categories`

The goal is to get enough information to help while avoiding unnecessary exposure.

## Sensitive data

The `sensitive_data` object controls how intake handles sensitive information.

Sensitive information may include:

- personal identifiers
- financial information
- medical information
- employment records
- immigration information
- minor-child information
- confidential business records
- privileged communications
- sealed-record information
- safety or domestic violence information

Pro-One should usually ask for summaries or redacted information rather than full sensitive records.

## Support routing

The `support_routing` object defines how Pro-One continues after intake.

This object is central to the project mission.

It includes:

- `default_support_modes`
- `risk_aware_support_modes`
- `avoid_abandonment`
- `human_help_framing`
- `routing_notes`

## Default support modes

Default support modes include:

- `general_information`
- `source_backed_steps`
- `checklist`
- `document_explanation`
- `issue_spotting`
- `court_or_agency_resource_prompt`
- `free_or_low_cost_resource_prompt`
- `workflow_selection`
- `process_step_guidance`
- `document_boundary_guidance`

These modes let Pro-One help without overstepping.

## Risk-aware support modes

Risk-aware support modes include:

- `continue_with_urgent_support`
- `continue_with_deadline_awareness`
- `continue_with_source_backed_steps`
- `continue_with_checklist`
- `continue_with_issue_spotting`
- `continue_with_document_explanation`
- `continue_with_court_or_agency_resource_prompt`
- `continue_with_free_or_low_cost_resource_prompt`
- `narrow_scope_before_answering`
- `pause_for_missing_information`
- `avoid_final_decision`

These modes are not abandonment. They are safer ways to continue.

## Human help framing

Human help should not be framed as the default requirement.

The schema supports:

- `not_required_by_default`
- `optional_free_or_low_cost_resource`
- `recommended_for_high_risk_issues`
- `urgent_for_extreme_risk`

This allows Pro-One to remain useful while still being honest about serious risks.

## Risk signals

The `risk_signals` object identifies signals that affect routing.

It includes:

- `deadline_signals`
- `high_risk_signals`
- `unsafe_request_signals`
- `routing_response`

## Deadline signals

Deadline signals should usually route to urgent support.

They should not cause Pro-One to stop helping.

Examples:

- response due today
- response due tomorrow
- subpoena production date is near
- hearing is scheduled soon
- deadline already passed
- motion to compel received
- sanctions threat received
- agency response date received

Pro-One should help the user organize the situation quickly.

## High-risk signals

High-risk signals require narrower and more careful support.

Examples:

- subpoena
- discovery sanctions
- request for admission
- privilege issue
- confidential business records
- domestic violence or safety issue
- immigration consequence
- criminal exposure
- minor-child issue
- contempt risk
- active court order
- large financial exposure
- regulated business activity

High-risk signals should not automatically end support.

They should change the support mode.

## Unsafe request signals

Unsafe request signals require Pro-One to refuse the unsafe part while continuing the safe part where possible.

Examples:

- asking Pro-One to invent facts
- asking Pro-One to hide evidence
- asking Pro-One to destroy documents
- asking Pro-One to deceive a court or agency
- asking Pro-One to ignore a subpoena
- asking Pro-One to threaten unlawful action
- asking Pro-One to fabricate records
- asking Pro-One to make a privilege determination without review
- asking Pro-One to choose admissions or denials without user-confirmed facts

A useful pattern is:

> I cannot help with that part. I can help you understand the process, organize the facts you do have, identify source-backed next steps, and prepare a checklist.

## Routing responses

The schema supports these routing responses:

- `continue_in_safer_mode`
- `continue_with_urgent_support`
- `continue_with_issue_spotting`
- `narrow_then_continue`
- `refuse_unsafe_part_and_continue_safe_part`

These values keep the product aligned with its access mission.

## Outputs

The `outputs` object defines what Pro-One may produce after intake.

Allowed outputs include:

- `workflow_suggestion`
- `jurisdiction_question`
- `source_backed_next_steps`
- `checklist`
- `document_explanation`
- `issue_spotting_summary`
- `deadline_awareness_prompt`
- `urgent_support_summary`
- `court_or_agency_resource_prompt`
- `free_or_low_cost_resource_prompt`
- `scope_boundary`

Prohibited outputs should be specific to the intake.

Common prohibited outputs include:

- guaranteed outcomes
- final legal decisions
- legal sufficiency determinations
- unsupported deadline calculations
- filing-ready documents without review
- final discovery objections
- privilege determinations
- instructions to hide, destroy, or withhold evidence unlawfully

## Privacy

The `privacy` object defines privacy reminders and data-minimization expectations.

It includes:

- `privacy_notice_required`
- `data_minimization_required`
- `retention_warning_required`
- `privacy_notes`

The intake should avoid implying that user information is protected, stored, deleted, or retained under a policy unless the project has a real policy and technical implementation that supports that claim.

## Review

The `review` object tracks whether an intake definition has been reviewed.

Review status may be:

- `proposed`
- `needs_review`
- `reviewed`
- `approved`
- `deprecated`
- `rejected`

Sample intakes should remain proposed.

## Evaluation

The `evaluation` object defines tests and success criteria.

Evaluation should test whether intake:

- asks only necessary questions
- avoids prohibited sensitive data
- routes urgent users to urgent support
- avoids abandonment
- uses source-backed support when needed
- refuses unsafe requests
- continues with safe parts of the request
- respects document boundaries
- avoids final legal determinations

## Sample intake records

The sample file currently includes:

- `example-name-change-intake`
- `example-discovery-deadline-intake`
- `example-subpoena-intake`
- `example-small-business-demand-letter-intake`

These samples are placeholders.

They show how intake definitions can support different situations while preserving the same basic design:

- ask only what is needed
- avoid unnecessary sensitive data
- route urgent issues to urgent support
- keep helping in a safe mode
- refuse unsafe requests without abandoning the user
- avoid unsupported legal advice

## Name-change intake

The name-change sample focuses on workflow selection.

It asks for basic jurisdiction information and whether the user already has court forms or instructions.

It does not ask for unnecessary sensitive background details.

It treats minor-child, safety, sealed-record, criminal-history, and immigration issues as restricted categories that may require narrower support.

## Discovery deadline intake

The discovery sample focuses on urgent support.

It covers situations involving:

- interrogatories
- requests for production
- requests for admission
- document requests
- missed deadlines
- motions to compel
- sanctions threats
- privilege concerns
- confidential information

The intake should keep helping even when a deadline is close.

It should not draft final discovery responses, choose objections, decide privilege, or choose admissions or denials.

## Subpoena intake

The subpoena sample focuses on issue spotting and urgent support.

It asks:

- what issued the subpoena
- what jurisdiction is listed
- whether it asks for testimony, documents, or both
- what dates appear on it

It should not tell a user to ignore a subpoena or decide whether service was valid.

It should help users organize the issue, identify deadlines, understand categories, and find source-backed next steps.

## Small-business demand-letter intake

The small-business sample focuses on organizing user-confirmed facts.

It can support practical communication help when safe.

It should not:

- invent facts
- make unsupported legal threats
- guarantee payment
- provide a liability opinion
- use abusive language
- include confidential business information unnecessarily

## Adding a new intake definition

When adding a new intake definition:

1. Identify the supported workflow.
2. Identify related process steps.
3. Identify related legal documents.
4. Decide whether jurisdiction is required.
5. Write the intake goal.
6. List required questions.
7. List optional questions.
8. List conditional questions.
9. List prohibited questions.
10. Define data limits.
11. Define sensitive-data handling.
12. Define default support modes.
13. Define risk-aware support modes.
14. Define deadline, high-risk, and unsafe request signals.
15. Define allowed and prohibited outputs.
16. Define privacy controls.
17. Mark the review status.
18. Add evaluation requirements.

## Good intake design

A good intake definition is:

- short enough for users to complete
- clear enough for nonlawyers to understand
- narrow enough to avoid overcollection
- practical enough to route the user forward
- careful enough to identify risk
- flexible enough to keep helping
- honest about limits
- tied to sources, workflows, process steps, and documents

## Bad intake design

A bad intake definition may:

- ask for every possible fact at the start
- ask for sensitive information too early
- make the user retell traumatic facts unnecessarily
- route urgent users away from help
- use lawyer-only phrasing without explanation
- treat every risk as a reason to stop
- imply Pro-One can decide legal rights
- imply Pro-One can guarantee outcomes
- produce document drafts without required facts
- ignore jurisdiction and source limits

## Guiding rule

The guiding rule for intake is:

> Ask the minimum necessary questions, protect sensitive information, identify the support mode, and keep helping the user in the safest useful way.
