# Risk Definitions

This document explains how Pro-One risk definitions work.

A risk definition is a structured record for recurring situations where Pro-One must be more careful, more focused, more source-grounded, or more protective of the user. Risk definitions help Pro-One continue assisting users without overstepping, inventing facts, making unsupported legal claims, or abandoning users during urgent moments.

Risk definitions are not legal advice. They are technical and safety records that support legal-information workflows.

## Current status

The risk schema is an early technical foundation.

The current files are:

- `schemas/risk.schema.json`
- `data/sample-risks.json`
- `docs/risks.md`

The sample risk records are placeholders. They are not approved production risk rules, user-facing legal guidance, legal advice, court instructions, or agency instructions.

## Core principle

Risk does not mean Pro-One stops helping.

Risk means Pro-One continues in a safer, narrower, more practical support mode.

For Pro-One, the goal is not to route users away by default. The goal is to help individuals and small businesses keep moving through legal matters while avoiding unsafe or unsupported assistance.

## Why risk definitions matter

Risk definitions help Pro-One avoid two opposite failures.

The first failure is under-warning.

This happens when Pro-One treats a serious issue as routine. Examples include:

- missed deadlines
- same-day deadlines
- subpoenas
- discovery sanctions
- requests for admission
- privilege issues
- court orders
- contempt risk
- immigration consequences
- criminal exposure
- sensitive records
- requests to hide or destroy evidence

The second failure is over-refusal.

This happens when Pro-One says it cannot help just because the situation is urgent or complicated.

Pro-One should avoid both failures.

## Safe continuation

Safe continuation means Pro-One keeps helping while respecting limits.

Safe continuation may include:

- urgent support
- deadline awareness
- source-backed steps
- checklists
- document explanation
- issue spotting
- court or agency resource prompts
- free or low-cost resource prompts
- privacy prompts
- redaction prompts
- scope boundaries
- truthful fact organization

Safe continuation should not include:

- inventing facts
- giving false reassurance
- ignoring legal papers
- hiding evidence
- destroying records
- deciding privilege
- choosing objections
- choosing admissions or denials
- calculating unsupported deadlines
- guaranteeing outcomes
- deciding final compliance obligations
- deciding document readiness for filing

## Risk type

Each risk record has a `risk_type`.

Supported values include:

- `deadline_risk`
- `urgent_court_or_agency_risk`
- `subpoena_risk`
- `discovery_risk`
- `evidence_integrity_risk`
- `privilege_or_confidentiality_risk`
- `privacy_risk`
- `safety_risk`
- `criminal_exposure_risk`
- `immigration_consequence_risk`
- `minor_child_risk`
- `contempt_or_order_violation_risk`
- `financial_exposure_risk`
- `regulated_business_risk`
- `unsafe_user_request`
- `unsupported_legal_claim_risk`
- `other`

Use the most specific risk type that fits.

## Risk level

Each risk record has a `risk_level`.

Supported values are:

- `low`
- `medium`
- `high`
- `extreme`

A higher risk level should change the support mode, not automatically end assistance.

## Low risk

Low-risk situations usually allow general information, checklists, and source-backed steps.

Example:

- a user asks what a common court form is generally used for

## Medium risk

Medium-risk situations require clearer scope boundaries and source-backed support.

Examples:

- a small-business demand letter
- a name-change process involving privacy concerns
- a filing process with uncertain court location

## High risk

High-risk situations require urgent, narrow, and careful support.

Examples:

- subpoenas
- discovery requests
- missed deadlines
- requests for admission
- sanctions threats
- sensitive records
- privilege concerns
- formal court or agency notices

## Extreme risk

Extreme-risk situations require refusal of unsafe parts while continuing safe support where possible.

Examples:

- requests to fabricate facts
- requests to hide evidence
- requests to destroy records
- requests to deceive a court or agency
- requests involving immediate safety danger

## Jurisdiction

The `jurisdiction` object controls whether Pro-One needs court, agency, state, locality, or forum information before giving specific support.

It includes:

- `jurisdiction_required`
- `country`
- `state`
- `locality`
- `court`
- `agency`
- `jurisdiction_unknown_handling`
- `jurisdiction_notes`

When jurisdiction is unknown, Pro-One should not pretend a specific rule applies.

It may still continue with:

- general information
- one focused clarifying question
- jurisdiction-identification steps
- court or agency finder prompts
- scope narrowing

## Jurisdiction unknown handling

The schema supports:

- `continue_with_general_information`
- `ask_minimum_clarifying_question`
- `offer_jurisdiction_identification_steps`
- `provide_court_or_agency_finder_prompt`
- `narrow_scope_before_answering`

For urgent matters, Pro-One should ask the minimum needed question and continue.

## Related records

The `related_records` object connects a risk to other Pro-One foundations.

It includes:

- source identifiers
- workflow identifiers
- process-step identifiers
- legal-document identifiers
- intake identifiers
- legal-rule identifiers

This keeps risk handling connected to the rest of the system.

## Relationship to source metadata

Source metadata records identify the legal, court, agency, or self-help sources Pro-One may rely on.

Risk records may require source-backed support before specific guidance is given.

For example, a deadline risk may require source-backed deadline information before Pro-One can give anything beyond deadline awareness.

## Relationship to workflow definitions

Workflow definitions describe what Pro-One may help users do.

Risk records identify risks that may appear inside those workflows.

For example:

- discovery risk may appear in a civil discovery information workflow
- subpoena risk may appear in a subpoena information workflow
- deadline risk may appear in many workflows
- evidence-integrity risk may appear across filings, discovery, subpoenas, and demand letters

## Relationship to process steps

Process-step records define steps like reviewing documents, completing forms, filing, serving, responding, waiting, attending hearings, and following up.

Risk records may attach to process steps where users are likely to need more careful support.

## Relationship to legal documents

Legal-document records define document categories, required facts, drafting limits, filing or service limits, privacy controls, and evaluation requirements.

Risk records help determine when document support should narrow.

For example:

- a subpoena document may trigger subpoena urgent risk
- a discovery response may trigger discovery sanctions risk
- a demand letter may trigger unsupported-threat risk
- a declaration may trigger evidence-integrity risk if the user asks to invent facts

## Relationship to intake definitions

Intake definitions ask users only the minimum necessary questions.

Risk records help intake decide what signals matter.

For example, intake may ask:

- What type of document did you receive?
- What date is listed?
- What court or agency is involved?
- Are you asking for help understanding the document, organizing facts, or preparing next steps?

Risk records should not encourage overcollection.

## Relationship to legal rules

Legal-rule records define source-backed rule statements.

Risk records define how those rules can be misused and how Pro-One should continue safely.

For example, a discovery deadline-awareness legal rule may connect to a discovery sanctions risk record.

## Relationship to future evaluation fixtures

Evaluation fixtures will test whether risk handling works.

They should test:

- same-day deadlines
- missed deadlines
- subpoenas
- discovery sanctions
- requests for admission
- privilege concerns
- requests to hide evidence
- requests to fabricate facts
- over-refusal
- under-warning
- safe continuation

## Relationship to future response schema

The response schema will define what a safe user-facing response must include.

Risk records help determine whether the response should include:

- urgent support
- deadline awareness
- redaction prompts
- scope boundaries
- source references
- safe refusal
- safe continuation
- free or low-cost resource prompts

## Trigger signals

The `trigger_signals` object identifies when a risk may be present.

It includes:

- `user_statements`
- `document_signals`
- `timing_signals`
- `source_signals`
- `trigger_notes`

## User statements

User statements are things users say that may reveal risk.

Examples:

- “This is due today.”
- “I missed the deadline.”
- “I received a subpoena.”
- “The other side filed a motion to compel.”
- “Can I ignore this?”
- “What objection should I use?”
- “Can you make this sound like it happened?”
- “Can I delete these records?”

## Document signals

Document signals are words, titles, or features in legal papers that may indicate risk.

Examples:

- subpoena
- command to appear
- request for production
- request for admission
- motion to compel
- sanctions warning
- contempt
- default
- dismissal
- response due
- hearing notice
- production date

## Timing signals

Timing signals include:

- same-day deadline
- next-day deadline
- deadline within seven days
- deadline already missed
- near hearing
- near appearance date
- near production date
- date to respond to a motion

Timing signals should usually route to urgent support.

## Source signals

Source signals come from other Pro-One records.

Examples:

- a legal-rule record requires source-backed deadline information
- a process-step record says deadline handling is source required
- a legal-document record prohibits final responses
- an intake record requires redaction prompts
- a workflow record excludes final legal decisions

## User context

The `user_context` object defines the minimum facts needed to route safely.

It includes:

- `required_facts`
- `optional_facts`
- `facts_not_to_collect`
- `unknown_fact_handling`
- `user_context_notes`

The goal is to help quickly without asking for unnecessary sensitive information.

## Required facts

Required facts should be limited.

For deadline risk, required facts may include:

- document type
- listed date
- court or agency if known
- what the user is trying to do next

For subpoena risk, required facts may include:

- whether the document is a subpoena
- issuing authority
- whether it asks for testimony, documents, or both
- date listed

For discovery risk, required facts may include:

- type of discovery request
- court or jurisdiction if known
- believed deadline
- whether a motion to compel or sanctions threat exists
- what help the user needs

## Optional facts

Optional facts may help, but they should not overwhelm the user.

Examples:

- date received
- service method
- whether the user already responded
- whether confidential records are involved
- whether a court order changed timing
- whether the other side is represented

## Facts not to collect

Risk records should clearly list what Pro-One should not ask for.

Examples:

- full Social Security numbers
- full financial account numbers
- unredacted medical records
- privileged communications
- unnecessary personal identifiers
- instructions for hiding evidence
- details that would help complete an unsafe act

## Unknown fact handling

The schema supports:

- `ask_one_clarifying_question`
- `continue_with_general_information`
- `continue_with_checklist`
- `continue_with_issue_spotting`
- `pause_for_missing_information`
- `narrow_scope_before_answering`

For urgent users, one focused question is often better than a long intake.

## Unsafe requests

The `unsafe_requests` object defines what Pro-One should not assist with.

It includes:

- `unsafe_request_examples`
- `refusal_required`
- `refusal_style`
- `continue_safe_parts`
- `safe_alternatives`
- `unsafe_request_notes`

## Refusal style

The schema supports these refusal styles:

- `refuse_unsafe_part_only`
- `brief_boundary_then_continue`
- `safety_first_then_continue`
- `source_limit_then_continue`

The preferred pattern is usually brief refusal plus safe continuation.

Example:

> I cannot help make up or hide facts, but I can help organize the facts and documents you actually have.

## Continue safe parts

When `continue_safe_parts` is true, Pro-One should keep helping after refusing the unsafe part.

This is central to Pro-One's access mission.

## Safe alternatives

Safe alternatives may include:

- explaining a document category
- helping organize truthful facts
- creating a checklist
- identifying source-backed next steps
- prompting redaction
- pointing to court or agency resources
- pointing to free or low-cost resources

## Support routing

The `support_routing` object defines the default support strategy.

It includes:

- `default_response_strategy`
- `safe_continuation_required`
- `support_modes`
- `routing_notes`

## Default response strategy

Supported strategies are:

- `continue_in_safer_mode`
- `continue_with_urgent_support`
- `continue_with_deadline_awareness`
- `continue_with_issue_spotting`
- `narrow_then_continue`
- `refuse_unsafe_part_and_continue_safe_part`

These strategies should prevent both under-warning and over-refusal.

## Support modes

Supported modes include:

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
- `privacy_prompt`
- `redaction_prompt`

Support modes define how Pro-One helps.

## Allowed support

The `allowed_support` object defines what Pro-One may provide.

It includes:

- `allowed_outputs`
- `allowed_actions`
- `allowed_language`
- `allowed_support_notes`

Allowed support should be practical and user-centered.

Examples:

- urgent support summary
- document-type explanation
- checklist
- issue-spotting summary
- redaction prompt
- court or agency resource prompt
- free or low-cost resource prompt
- truthful fact organization

## Prohibited support

The `prohibited_support` object defines what Pro-One must not provide.

It includes:

- `prohibited_outputs`
- `prohibited_actions`
- `prohibited_language`
- `prohibited_support_notes`

Common prohibited support includes:

- final deadline calculations without source support
- guaranteed outcomes
- final discovery responses
- chosen objections
- privilege determinations
- final compliance decisions
- advice to ignore legal papers
- fabricated facts
- fake documents
- instructions to hide or destroy evidence
- instructions to deceive a court, agency, opposing party, or recipient

## Deadline handling

The `deadline_handling` object defines deadline support.

It includes:

- `deadline_relevant`
- `deadline_strategy`
- `deadline_outputs_allowed`
- `deadline_outputs_prohibited`
- `deadline_notes`

## Deadline strategy

Supported deadline strategies are:

- `no_deadline`
- `deadline_awareness_only`
- `source_backed_deadline_information`
- `urgent_support_without_final_calculation`
- `human_help_as_additional_option`

A near deadline should usually route to urgent support.

It should not cause Pro-One to stop helping.

## Deadline outputs allowed

Allowed deadline outputs may include:

- deadline awareness
- prompt to identify the listed date
- prompt to check the official source or notice
- checklist for urgent organization
- appearance-date awareness
- production-date awareness

## Deadline outputs prohibited

Prohibited deadline outputs may include:

- unsupported final deadline calculation
- guaranteed grace period
- statement that a missed deadline has no consequence
- advice to ignore a deadline
- advice to ignore a court or agency notice

## Privacy

The `privacy` object defines sensitive-data controls.

It includes:

- `sensitive_data_likely`
- `redaction_prompt_required`
- `data_minimization_required`
- `restricted_data_categories`
- `prohibited_data_categories`
- `privacy_notes`

Risk situations often involve sensitive information.

Pro-One should prefer summaries and redacted excerpts.

## Restricted data categories

Restricted data may include:

- court case information
- agency investigation information
- medical information
- financial information
- employment information
- confidential business information
- privileged communications
- minor-child information
- immigration information
- safety information

Restricted does not always mean prohibited. It means Pro-One should minimize collection and handle carefully.

## Prohibited data categories

Prohibited data categories may include:

- full Social Security numbers
- full financial account numbers
- unredacted sensitive records
- privileged messages
- unnecessary personal identifiers
- step-by-step details for unlawful concealment
- instructions for deception

## Human help

The `human_help` object defines how Pro-One may frame human help and resources.

It includes:

- `human_help_framing`
- `resource_prompt_allowed`
- `must_not_make_paid_help_the_default`
- `human_help_notes`

## Human help framing values

Supported values are:

- `not_required_by_default`
- `optional_free_or_low_cost_resource`
- `recommended_for_high_risk_issues`
- `urgent_for_extreme_risk`

Human help should not be framed as paid counsel by default.

When appropriate, Pro-One may suggest:

- court self-help
- court clerk information resources
- agency resources
- legal aid
- nonprofit help
- free clinics
- low-cost legal resources

This should be offered as an added path, not abandonment.

## Review

The `review` object tracks risk-definition review.

Review statuses include:

- `proposed`
- `needs_review`
- `reviewed`
- `approved`
- `deprecated`
- `rejected`

Sample risks should remain `proposed`.

## Evaluation

The `evaluation` object defines tests and success criteria.

Evaluation should test whether Pro-One:

- identifies risk signals
- avoids over-refusal
- avoids under-warning
- continues safely
- refuses unsafe requests
- does not collect unnecessary sensitive data
- does not calculate unsupported deadlines
- does not provide final legal decisions
- frames human help appropriately
- protects the access mission

## Sample risk records

The sample file currently includes:

- `example-imminent-deadline-risk`
- `example-discovery-sanctions-risk`
- `example-subpoena-urgent-risk`
- `example-evidence-integrity-unsafe-request-risk`

These are placeholder records for schema design.

## Imminent deadline risk

The imminent deadline sample covers situations where a user reports:

- same-day deadline
- next-day deadline
- deadline within seven days
- missed deadline
- uncertain response date
- court or agency document with a response date

The correct routing is urgent support, not abandonment.

Pro-One may help the user:

- identify the document type
- locate the listed date
- identify the court or agency if needed
- organize materials
- review source-backed steps when available
- create an urgent checklist

Pro-One should not:

- invent a deadline
- guarantee acceptance of a late filing
- say a missed deadline has no consequence
- tell the user to ignore a deadline
- calculate a final deadline without reviewed source support and required facts

## Discovery sanctions risk

The discovery sample covers civil discovery issues involving:

- missed deadlines
- motions to compel
- requests for admission
- sanctions threats
- objections
- privilege
- sensitive records

Pro-One may provide:

- request-type explanations
- organization checklists
- issue spotting
- deadline awareness
- redaction prompts
- scope boundaries
- free or low-cost resource prompts

Pro-One should not:

- draft final discovery responses
- choose objections
- decide privilege
- choose admissions or denials
- tell the user to ignore discovery
- help hide or destroy responsive documents

## Subpoena urgent risk

The subpoena sample covers subpoenas involving:

- testimony
- document production
- near appearance dates
- near production dates
- sensitive records
- service questions
- requests to ignore the subpoena

Pro-One may provide:

- document explanation
- subpoena category explanation
- date awareness
- issue spotting
- urgent checklist support
- court or agency resource prompts
- free or low-cost resource prompts

Pro-One should not:

- tell a user to ignore a subpoena
- decide service validity
- decide final compliance obligations
- draft final objections
- draft a motion to quash
- help hide, destroy, or withhold evidence unlawfully

## Evidence integrity unsafe request risk

The evidence-integrity sample covers requests involving:

- fabrication
- concealment
- destruction
- alteration
- deception
- fake documents
- backdating
- hiding records
- misleading a court, agency, opposing party, or recipient

This is an extreme risk category.

Pro-One must refuse the unsafe part.

But Pro-One should still continue with safe support when possible.

Safe alternatives include:

- organizing truthful facts
- making a checklist of real records
- explaining the document or process
- helping the user identify existing materials
- offering resource prompts

## Adding a real risk definition

When adding a real risk definition:

1. Identify the risk type.
2. Assign the risk level.
3. Define jurisdiction requirements.
4. Connect related source records.
5. Connect related workflows.
6. Connect related process steps.
7. Connect related legal documents.
8. Connect related intake records.
9. Connect related legal-rule records.
10. Define user-statement triggers.
11. Define document triggers.
12. Define timing triggers.
13. Define source triggers.
14. Define required user facts.
15. Define optional user facts.
16. Define facts not to collect.
17. Define unsafe request examples.
18. Define refusal style.
19. Define safe alternatives.
20. Define support routing.
21. Define allowed support.
22. Define prohibited support.
23. Define deadline handling.
24. Define privacy controls.
25. Define human-help framing.
26. Define review status.
27. Define evaluation requirements.

## Good risk design

A good risk record is:

- specific
- practical
- tied to user signals
- tied to document signals
- tied to timing signals
- connected to other Pro-One records
- clear about safe continuation
- clear about unsafe requests
- careful with sensitive data
- honest about deadlines
- not overly referral-based
- not overly permissive
- easy to evaluate

## Bad risk design

A bad risk record may:

- treat every risk as a reason to stop
- treat every risk as low importance
- route users away from help too quickly
- ignore urgent deadlines
- give false reassurance
- collect too much sensitive information
- provide final legal decisions
- support fabricated facts
- support evidence destruction
- ignore source limits
- frame paid counsel as the default answer
- fail to offer safe alternatives

## Guiding rule

The guiding rule for risk definitions is:

> Identify risk early, refuse unsafe assistance when needed, and keep helping the user through the safest useful support mode.
