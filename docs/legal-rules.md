# Legal Rule Definitions

This document explains how Pro-One legal-rule definitions work.

A legal-rule definition is a structured record for a source-backed rule statement. It helps Pro-One avoid unsupported legal claims by tying rule language to sources, jurisdiction, dates, workflows, process steps, document types, support modes, review status, and evaluation requirements.

Legal-rule records are not legal advice. They are controlled technical records used to support safe legal-information workflows.

## Current status

The legal-rule schema is an early technical foundation.

The current files are:

- `schemas/legal-rule.schema.json`
- `data/sample-legal-rules.json`
- `docs/legal-rules.md`

The sample legal-rule records are placeholders. They are not approved production rules, user-facing legal guidance, legal advice, court instructions, or agency instructions.

## Core principle

Pro-One should not make legal-rule claims unless the rule is tied to reviewed sources and used within its approved scope.

A legal-rule record should answer:

- What does the source-backed rule say?
- Where does it apply?
- What source supports it?
- When was it checked?
- What workflow may use it?
- What process step may use it?
- What document type may use it?
- What facts are needed from the user?
- What should Pro-One avoid saying?
- What support mode is allowed?
- What risks require narrower support?
- What tests must pass before use?

## Why legal rules matter

Legal rules are a major safety layer.

Without legal-rule records, Pro-One could accidentally:

- summarize rules without source support
- apply a rule in the wrong jurisdiction
- rely on outdated source material
- overstate a court instruction
- treat a general rule as a deadline calculation
- tell a user a document is ready to file
- choose objections or admissions for a user
- decide compliance obligations
- make unsupported legal threats
- fail to flag local variations or exceptions

The legal-rule schema prevents that by making rule support explicit.

## Relationship to source metadata

Source metadata records define the materials Pro-One may rely on.

Legal-rule records use source identifiers to show where a rule comes from.

A legal-rule record should not be approved unless its required source records are reviewed and suitable for the rule's use.

For example, a court filing rule should rely on official court instructions, court rules, court forms, or other reviewed authority.

## Relationship to workflow definitions

Workflow definitions describe what Pro-One may help users do.

A legal rule should identify which workflows may use it.

For example:

- a name-change filing rule may support a name-change information workflow
- a discovery deadline-awareness rule may support a civil discovery information workflow
- a subpoena response-options rule may support a subpoena information workflow
- a small-business demand-letter factual-basis rule may support a small-business dispute workflow

A rule should not be used in unrelated workflows simply because the text appears similar.

## Relationship to process steps

Process-step records describe the practical steps within a workflow.

A legal rule should identify which process steps may use it.

For example:

- review instructions
- complete forms
- file with court
- review discovery requests
- prepare discovery responses
- review subpoena
- identify response options
- prepare demand-letter facts

This keeps rules connected to concrete user tasks.

## Relationship to legal documents

Legal-document records define document types, required facts, drafting boundaries, filing or service limits, privacy controls, and evaluation requirements.

A legal rule may support:

- document explanation
- document checklist help
- issue spotting
- source-backed drafting boundaries
- filing packet guidance
- service packet guidance

A legal rule should not be used to make final document-readiness decisions unless a later approved workflow specifically supports that use.

## Relationship to intake definitions

Intake definitions determine what Pro-One asks the user.

Legal-rule records define what facts are needed before a rule can be used.

For example, a discovery deadline-awareness rule may need:

- court or jurisdiction
- type of discovery request
- date received
- response date listed in the request
- whether a court order changed timing
- whether a motion to compel or sanctions threat exists

The intake should collect only the minimum facts needed.

## Relationship to risk definitions

The risk schema makes risk controls reusable across workflows.

Legal-rule records already include risk fields, but the risk schema helps standardize recurring risks such as:

- imminent deadlines
- subpoenas
- discovery sanctions
- privilege concerns
- requests for admission
- safety issues
- immigration consequences
- criminal exposure
- contempt risk
- requests to hide or destroy evidence
- requests to invent facts

Legal-rule risk fields should focus on how the specific rule can be misused.

## Relationship to future evaluation fixtures

Evaluation fixtures will test whether rules are used safely.

They should check whether Pro-One:

- uses only reviewed sources
- identifies jurisdiction
- avoids unsupported claims
- avoids outdated rules
- avoids final legal decisions
- flags risk signals
- continues in a safer support mode when needed
- refuses unsafe uses while continuing safe support

## Relationship to response patterns

The response schema defines what a safe user-facing answer must include.

Legal-rule records will support response requirements such as:

- citation
- plain-language explanation
- scope boundary
- deadline awareness
- source-backed steps
- safe continuation
- warnings against unsupported conclusions

## Rule type

Each legal-rule record has a `rule_type`.

Supported values include:

- `eligibility_rule`
- `filing_rule`
- `service_rule`
- `notice_rule`
- `deadline_rule`
- `form_rule`
- `fee_rule`
- `fee_waiver_rule`
- `hearing_rule`
- `evidence_rule`
- `discovery_rule`
- `subpoena_rule`
- `response_rule`
- `appeal_or_review_rule`
- `agency_rule`
- `business_rule`
- `contract_rule`
- `privacy_rule`
- `safety_rule`
- `other`

Use the most specific rule type that fits.

## Status values

Each legal-rule record has a status:

- `proposed`
- `researched`
- `designed`
- `tested`
- `supported`
- `deprecated`
- `rejected`

Sample rules should remain `proposed`.

A real legal rule should not become `supported` until the source record, rule text, scope, risk controls, review, and evaluation are complete.

## Jurisdiction

The `jurisdiction` object defines where a rule may apply.

It includes:

- country
- state
- locality
- court
- agency
- whether jurisdiction is required
- jurisdiction notes

Some legal rules are national. Some are state-specific. Some are court-specific. Some are agency-specific. Some vary by county, city, or local court practice.

When jurisdiction is unknown, Pro-One should avoid pretending the rule applies. It may still continue with general information or help the user identify the correct court, agency, or source.

## Source support

The `source_support` object defines the sources supporting the rule.

It includes:

- required source identifiers
- optional source identifiers
- whether short quotations are allowed
- whether source review is required
- source notes

Required sources should be reviewed before a rule is used.

Optional sources may help explain the rule, but they should not replace required authority.

## Rule statement

The `rule_statement` object includes:

- `canonical_statement`
- `plain_language_statement`
- `must_not_overstate`
- `user_facing_allowed`
- `rule_statement_notes`

## Canonical statement

The canonical statement is the controlled version of the rule.

It should be precise, source-backed, and narrow.

Example:

> Discovery response timing should be checked against the applicable court rules, any court order, the discovery request, the service method, and the relevant jurisdiction before Pro-One provides deadline-aware support.

## Plain-language statement

The plain-language statement explains the rule in user-friendly language.

Example:

> Discovery deadlines can depend on the court rules, how the request was served, what the request says, and whether the judge entered any orders.

## Must not overstate

The `must_not_overstate` field is one of the most important parts of the legal-rule schema.

It tells Pro-One what not to say.

Examples:

- Do not say the user is eligible.
- Do not say the court will approve the request.
- Do not say a document is ready to file.
- Do not calculate a final deadline without required facts and reviewed sources.
- Do not choose objections for the user.
- Do not decide privilege.
- Do not decide whether the user must comply with a subpoena.
- Do not make unsupported legal threats.
- Do not guarantee payment or settlement.

## User-facing allowed

The `user_facing_allowed` field controls whether a rule may appear in user-facing responses.

A proposed sample rule should normally set this to `false`.

A real rule may be user-facing only after review and testing.

## Rule scope

The `rule_scope` object defines:

- what the rule applies to
- what the rule does not apply to
- what user facts are required
- whether a source check is required
- scope notes

A rule should not be used merely because it sounds relevant. It must fit the user's workflow, process step, document, jurisdiction, facts, and support mode.

## Applies to

The `applies_to` field describes supported situations.

Example for a subpoena rule:

- subpoena information
- subpoena checklist support
- issue spotting for subpoena dates and requested actions
- general explanation of testimony and document requests

## Does not apply to

The `does_not_apply_to` field prevents overuse.

Example for a subpoena rule:

- final compliance decisions
- final service-validity decisions
- final objections
- motions to quash
- criminal subpoena support unless separately approved

## Requires user facts

A rule may need specific facts before it can be used.

Examples:

- court or jurisdiction
- agency listed on a notice
- date received
- date listed on the document
- type of document
- whether a court order exists
- whether sensitive information is involved
- whether the user is a party or nonparty
- whether a business is regulated
- whether formal legal papers have already been received

Pro-One should not invent missing facts.

## Requires source check

Some rules may change often or vary by local procedure.

The `requires_source_check` field should be `true` when source freshness matters.

Deadline rules, filing rules, service rules, agency rules, and form rules usually require source checks.

## Workflow fit

The `workflow_fit` object defines:

- supported workflow identifiers
- excluded workflow identifiers
- workflow notes

A rule should be used only within supported workflows.

## Process-step fit

The `process_step_fit` object defines:

- supported process-step identifiers
- excluded process-step identifiers
- process-step notes

This keeps rules connected to the correct part of a process.

## Document fit

The `document_fit` object defines:

- supported document identifiers
- supported document types
- excluded document identifiers
- document notes

Supported document types include:

- court forms
- pleadings
- petitions
- answers and responses
- motions
- subpoenas
- notices
- discovery requests
- discovery responses
- interrogatories
- requests for production
- requests for admission
- objections
- demand letters
- settlement documents
- contracts
- agency applications
- business documents
- filing packets
- service packets
- hearing packets

A support mode is not a document type. For example, `document_explanation` is a support mode, not a document type.

## Dates

The `dates` object tracks:

- effective date
- last updated date
- last checked date
- expiration date
- date notes

Dates help prevent stale rule use.

For placeholder records, date fields may be null.

For real records, `last_checked` should be maintained.

## User support

The `user_support` object defines how a rule may support users.

Allowed support modes include:

- `general_information`
- `source_backed_steps`
- `checklist`
- `document_explanation`
- `issue_spotting`
- `deadline_awareness`
- `urgent_support`
- `court_or_agency_resource_prompt`
- `free_or_low_cost_resource_prompt`
- `scope_boundary`

A legal rule may be safe for checklist support but unsafe for final document drafting.

A legal rule may be safe for deadline awareness but unsafe for final deadline calculation.

## Requires plain language

User-facing rules should be explained in plain language.

Legal-rule records should avoid making the user decode legal jargon without explanation.

## Requires citation

User-facing use of legal rules should include a citation or source reference when source-backed support is required.

The response schema will later define exact citation expectations.

## Exceptions and variations

The `exceptions_and_variations` object can describe:

- known exceptions
- local variations
- unresolved questions
- variation notes

This helps Pro-One avoid overgeneralizing.

Examples:

- court orders may change deadlines
- service method may affect timing
- local rules may modify procedure
- agency subpoenas may follow different procedures
- minor-child name-change requests may have additional requirements
- regulated business activity may have special rules

## Risk

The `risk` object defines:

- risk level
- risk triggers
- unsafe uses
- safe continuation notes

Risk levels are:

- `low`
- `medium`
- `high`

Risk should not automatically mean Pro-One stops helping. It should usually mean Pro-One continues in a safer, narrower, source-backed mode.

## Risk triggers

Risk triggers are signals that require caution.

Examples:

- response due today
- response due tomorrow
- deadline already passed
- hearing soon
- subpoena production date near
- request for admission
- motion to compel
- sanctions threat
- privilege concern
- confidential records
- safety issue
- immigration consequence
- criminal exposure
- large financial exposure
- regulated business activity

## Unsafe uses

Unsafe uses describe what Pro-One should not help with.

Examples:

- inventing facts
- hiding evidence
- destroying documents
- deceiving a court or agency
- ignoring a subpoena
- choosing objections for a user
- deciding privilege
- choosing admissions or denials
- making unsupported legal threats
- guaranteeing a court outcome

When unsafe use appears, Pro-One should refuse that part and continue with safe support where possible.

## Safe continuation

Safe continuation means Pro-One remains useful without overstepping.

Safe continuation may include:

- explaining the process
- identifying source-backed next steps
- providing a checklist
- explaining document categories
- flagging issues to watch
- helping the user organize facts
- prompting redaction of sensitive information
- pointing to court or agency resources
- pointing to free or low-cost resources
- narrowing the scope before answering

Safe continuation should not include final legal decisions.

## Review

The `review` object tracks review status.

Review statuses include:

- `proposed`
- `needs_review`
- `reviewed`
- `approved`
- `deprecated`
- `rejected`

Review notes should explain any limits, unresolved issues, or needed source work.

## Evaluation

The `evaluation` object defines tests required before the rule can be supported.

Evaluation should test whether the rule:

- uses required sources
- stays within jurisdiction
- avoids overstatement
- avoids unsupported legal advice
- respects workflow limits
- respects process-step limits
- respects document limits
- flags risk signals
- continues safely when risk appears
- refuses unsafe uses while continuing safe support

## Sample legal-rule records

The sample file currently includes:

- `example-name-change-filing-instructions-rule`
- `example-discovery-response-deadline-awareness-rule`
- `example-subpoena-response-options-rule`
- `example-small-business-demand-letter-factual-basis-rule`

These records are placeholders.

They show the structure of a legal-rule definition, not approved Pro-One legal guidance.

## Name-change filing instructions rule

The name-change sample is a filing-rule placeholder.

It is designed to show that name-change filing support should be tied to court instructions and forms.

It should not be used to:

- decide eligibility
- guarantee approval
- say a petition is ready to file
- skip court-source review
- apply court-specific steps to the wrong court

## Discovery response deadline-awareness rule

The discovery sample is a deadline-awareness placeholder.

It is designed to route urgent discovery questions into support modes such as:

- urgent support
- deadline awareness
- checklist support
- issue spotting
- document explanation
- free or low-cost resource prompts

It should not be used to:

- calculate a final deadline without required facts and reviewed sources
- choose objections
- decide privilege
- choose admissions or denials
- draft final discovery responses
- tell the user a missed deadline has no consequence

## Subpoena response options rule

The subpoena sample is a subpoena-rule placeholder.

It is designed to help identify:

- issuing authority
- jurisdiction
- recipient role
- requested action
- listed dates
- source-backed response-option categories

It should not be used to:

- tell a user to ignore a subpoena
- decide service validity
- decide compliance obligations
- draft final objections
- draft a motion to quash
- help hide, destroy, or withhold evidence unlawfully

## Small-business demand-letter factual-basis rule

The small-business sample is a business-rule placeholder.

It is designed to require user-confirmed facts and professional tone.

It should not be used to:

- invent facts
- make unsupported legal threats
- guarantee payment or settlement
- provide final liability opinions
- use abusive or harassing language

## Adding a real legal rule

When adding a real legal rule:

1. Identify the rule type.
2. Identify the jurisdiction.
3. Identify required sources.
4. Confirm source authority and freshness.
5. Draft the canonical statement.
6. Draft the plain-language statement.
7. List what Pro-One must not overstate.
8. Decide whether user-facing use is allowed.
9. Define what the rule applies to.
10. Define what the rule does not apply to.
11. Define required user facts.
12. Define workflow fit.
13. Define process-step fit.
14. Define document fit.
15. Add date fields.
16. Define allowed support modes.
17. Define prohibited support modes.
18. Add exceptions and variations.
19. Add risk triggers.
20. Add unsafe uses.
21. Add safe continuation notes.
22. Add review status.
23. Add evaluation requirements.

## Good legal-rule design

A good legal-rule record is:

- source-backed
- jurisdiction-aware
- date-aware
- narrow
- plain-language ready
- tied to workflows
- tied to process steps
- tied to document types
- clear about limits
- clear about unsafe uses
- reviewed before user-facing use
- evaluated before supported use

## Bad legal-rule design

A bad legal-rule record may:

- rely on no source
- rely on a stale source
- ignore jurisdiction
- ignore local variations
- overstate a rule
- turn general information into legal advice
- treat deadline awareness as final deadline calculation
- treat document explanation as document approval
- decide strategy for the user
- invent missing facts
- ignore risk signals
- abandon users unnecessarily
- support unsafe requests

## Guiding rule

The guiding rule for legal-rule definitions is:

> A legal rule should be source-backed, jurisdiction-aware, narrowly scoped, plain-language ready, and safe to use only within approved workflows, process steps, documents, and support modes.
