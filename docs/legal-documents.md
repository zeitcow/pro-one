# Legal Documents

Legal-document definitions describe how Pro-One may explain, structure, review, or help prepare legal documents while staying within legal-information boundaries.

This schema is broader than court forms.

It covers documents used in court, agency, litigation, business, settlement, discovery, subpoena, filing, service, and hearing contexts.

## Purpose

Legal documents carry higher risk than general legal information.

A document can affect rights, deadlines, evidence, admissions, obligations, money, business operations, court orders, or settlement posture.

Legal-document definitions help Pro-One answer:

- what kind of document is involved
- which workflow the document supports
- which process step the document belongs to
- which court, agency, or jurisdiction applies
- which sources support the document
- which legal rules support the document
- what structure the document may require
- what facts the user must provide
- what facts Pro-One must not invent
- whether drafting is allowed
- whether filing, service, signature, notarization, or submission issues exist
- whether deadlines matter
- what sensitive information should be avoided or minimized
- when human help is needed
- what tests are required before support

This makes document assistance reviewable instead of free-form.

## Files

This foundation consists of three legal-document files:

- `schemas/legal-document.schema.json`
- `data/sample-legal-documents.json`
- `docs/legal-documents.md`

The schema defines the expected structure for legal-document records.

The sample data shows example document records using placeholder workflows, process steps, jurisdictions, sources, legal rules, and institutions.

The documentation explains how legal-document definitions should be reviewed and used.

## Current status

This is an early technical foundation.

The sample legal-document records are not approved production records.

They are examples only.

They should not be treated as supported Pro-One guidance, approved templates, or user-facing document workflows.

## Covered document categories

The schema is designed to cover document categories such as:

- court forms
- pleadings
- complaints
- petitions
- answers and responses
- motions
- motion responses and oppositions
- replies
- declarations and affidavits
- exhibits
- certificates of service
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
- contracts and agreements
- agency applications
- business documents
- compliance checklists
- filing packets
- service packets
- hearing packets
- other reviewed document types

The list is intentionally broad because Pro-One should not need a new schema every time a new document type is added.

Each document type still needs its own reviewed record before it can be supported.

## Required metadata

Each legal-document record requires:

- `id`
- `title`
- `description`
- `status`
- `document_type`
- `workflow_ids`
- `process_step_ids`
- `jurisdiction`
- `sources`
- `legal_rules`
- `structure`
- `user_facts`
- `drafting`
- `filing_or_service`
- `deadlines`
- `privacy`
- `safety`
- `review`
- `evaluation`

These fields are required because document help can mislead users when it is unsupported, jurisdictionally unclear, missing user facts, or too close to legal advice.

## Document status

Document status values include:

- `proposed`
- `researched`
- `designed`
- `tested`
- `supported`
- `deprecated`
- `rejected`

A proposed document definition is not a supported document definition.

A document should not become supported until source review, legal-rule review, workflow review, process-step review, safety review, privacy review, and evaluation requirements support that status.

## Workflow connection

The `workflow_ids` field connects a document to one or more workflows.

For example:

- a name-change petition may belong to a name-change information workflow
- a discovery response may belong to a civil discovery information workflow
- a demand letter may belong to a small-business dispute workflow
- an agency application may belong to a license or benefits workflow

A document should not float on its own.

It should support a defined workflow and inherit that workflow's scope, outputs, and safety limits.

## Process-step connection

The `process_step_ids` field connects a document to one or more process steps.

For example:

- a petition may connect to form-completion and filing steps
- a certificate of service may connect to a service step
- a subpoena may connect to review, objection, compliance, or motion steps
- a discovery response may connect to review, response, service, and deadline steps
- a hearing packet may connect to hearing-preparation steps

A document definition should not be approved unless the related process step is clear.

## Document type

The `document_type` field identifies the general category of document.

Examples include:

- `petition`
- `answer_or_response`
- `motion`
- `motion_response`
- `subpoena`
- `discovery_request`
- `discovery_response`
- `objection`
- `demand_letter`
- `contract_or_agreement`
- `filing_packet`

Document type helps Pro-One understand the risk level and the kind of assistance that may be allowed.

Some document types may allow user-confirmed drafting.

Other document types may only allow explanation, checklist, issue spotting, or human-help prompts.

## Jurisdiction

The `jurisdiction` field explains where the document definition applies.

A document may be tied to:

- a country
- a state
- a locality
- a court
- an agency

A document that applies in one court, agency, or jurisdiction should not be presented as valid elsewhere.

Court captions, form fields, signatures, notarization, service, filing methods, and deadlines may vary by jurisdiction.

When jurisdiction is uncertain, the document should remain proposed or needs review.

## Sources

The `sources` field connects a document definition to source metadata.

Sources may include:

- court instructions
- court forms
- court rules
- statutes
- agency rules
- agency guidance
- official self-help materials
- legal aid resources
- court websites
- public form packets

A document should not be supported unless its required sources have been reviewed for authority, jurisdiction, freshness, access, reuse rights, and workflow fit.

Source IDs should match records defined under source metadata.

## Legal rules

The `legal_rules` field tracks rule support for the document.

Legal-rule support may be needed for:

- pleading requirements
- response requirements
- discovery response deadlines
- subpoena service or objection rules
- motion deadlines
- certificate of service requirements
- notice requirements
- form requirements
- signature or verification requirements
- filing rules
- service rules
- agency application rules
- pre-suit demand requirements
- settlement or contract limits

Legal-rule records will be defined in a later schema.

Until then, document records can identify expected legal-rule IDs, but support should remain proposed when rule coverage is missing.

## Structure

The `structure` field explains the expected parts of the document.

It tracks:

- required sections
- optional sections
- prohibited sections
- whether section order matters
- structure notes

Document structure may include:

- caption
- case number
- party information
- title
- factual allegations
- requested relief
- numbered responses
- objections
- verification
- declaration language
- exhibits
- certificate of service
- signature block
- notarization
- filing packet components

Pro-One should not invent required structure without reviewed source or rule support.

## User facts

The `user_facts` field is one of the most important safety controls.

It tracks:

- required facts
- optional facts
- facts Pro-One must not invent
- sensitive facts
- whether user confirmation is required
- fact notes

Pro-One must not invent facts.

This includes facts such as:

- names
- dates
- case numbers
- party names
- amounts owed
- contract terms
- discovery responses
- admissions or denials
- objections
- privilege claims
- reasons for a request
- signatures
- filing dates
- service dates
- deadlines

A document definition should identify which facts must come directly from the user.

## Drafting boundaries

The `drafting` field defines what kind of document help is allowed.

Allowed assistance values may include:

- `none`
- `explanation`
- `checklist`
- `outline`
- `template_completion`
- `user_confirmed_draft`
- `draft_review_prompt`
- `issue_spotting_prompt`

Some documents may allow user-confirmed drafts when the user provides and confirms all facts and decisions.

Other documents should not allow drafting at all.

For example, a simple demand letter may allow a user-confirmed draft.

A discovery response, subpoena objection, or motion to quash may require human review and may only allow explanation, checklist, or issue spotting.

## Prohibited assistance

Each document definition must identify assistance Pro-One must not provide.

Prohibited assistance may include:

- inventing facts
- choosing legal strategy
- drafting final discovery responses
- deciding objections
- deciding privilege
- deciding whether to admit or deny a request
- guaranteeing court acceptance
- guaranteeing agency approval
- guaranteeing legal effect
- making final filing decisions
- serving documents for the user
- filing documents for the user
- telling a user to ignore a subpoena
- advising a user to hide, destroy, or withhold evidence unlawfully
- adding false statements or unsupported threats

These boundaries should be written plainly so document behavior can be tested.

## Filing, service, and submission

The `filing_or_service` field tracks whether a document may involve:

- filing with a court
- service on another party
- submission to an agency
- sending to a business or opposing party
- signature
- verification
- declaration
- affidavit
- notarization
- certification

Pro-One should not claim a document is ready to file, serve, submit, or send unless the document definition, workflow, process steps, sources, legal rules, and evaluation coverage support that claim.

In many early cases, the safer output is a checklist or review prompt.

## Deadlines

The `deadlines` field tracks whether deadlines may matter for the document.

Deadline handling values include:

- `not_applicable`
- `awareness_only`
- `source_backed_information`
- `qualified_review_required`
- `unsupported`

Pro-One should not guess deadlines.

Documents involving deadlines should generally require source support, legal-rule support, and escalation warnings.

High-risk deadline contexts include:

- answers or responses
- discovery responses
- requests for admission
- subpoenas
- motions
- oppositions
- appeals or review requests
- agency deadlines
- filing deadlines
- service deadlines
- renewal dates
- hearing deadlines

When deadlines may affect rights, admissions, sanctions, default, waiver, or case outcome, human review should be encouraged.

## Privacy

The `privacy` field defines privacy and data-minimization controls.

Legal documents may involve sensitive information such as:

- personal identifiers
- financial information
- medical information
- immigration information
- criminal history information
- employment information
- privileged communications
- confidential business information
- trade secret information
- minor-child information
- sealed-record information
- domestic violence or safety information

Pro-One should ask only for information needed to provide safe, source-backed document help.

Users should be encouraged to avoid sharing unnecessary sensitive material.

When redaction may be required, the document definition should say so.

## Safety

The `safety` field defines risk controls for a document.

It tracks:

- risk level
- escalation triggers
- refusal triggers
- required warnings
- safety notes

Escalation triggers tell Pro-One when to direct the user toward legal aid, court help, a lawyer, or another human resource.

Refusal triggers tell Pro-One when to refuse, narrow, or redirect a request.

Required warnings help ensure Pro-One does not overstate what it can do.

## Risk examples

Lower-risk document help may include:

- explaining what a form is for
- creating a checklist
- identifying missing user facts
- organizing user-provided information
- drafting a professional demand letter from confirmed facts

Higher-risk document help may include:

- discovery responses
- subpoena objections
- motions
- appeals
- emergency filings
- documents involving minors
- documents involving safety concerns
- documents involving immigration consequences
- documents involving criminal exposure
- documents involving privileged information
- documents involving sealed records
- documents with short deadlines

Higher-risk document help should usually require human review.

## Discovery documents

Discovery documents require special caution.

They may involve:

- interrogatories
- requests for production
- requests for admission
- document production
- objections
- privilege
- verification
- sanctions
- motions to compel
- admissions
- response deadlines

Pro-One should not invent responses, choose objections, decide privilege, or tell the user to withhold documents without legal review.

Discovery response support should remain tightly limited until legal-rule and evaluation coverage is strong.

## Subpoenas

Subpoenas require special caution.

They may involve:

- testimony
- document production
- nonparty obligations
- service issues
- objection deadlines
- motions to quash
- protective orders
- privileged material
- confidential records
- sanctions or contempt risk

Pro-One should not tell a user to ignore a subpoena.

Pro-One should not decide subpoena validity, compliance obligations, objections, privilege, or motion strategy.

Subpoena support should focus on source-backed explanation, issue spotting, and escalation.

## Demand letters

Demand letters may be less risky than court filings, but they still need controls.

They may involve:

- factual allegations
- amounts owed
- contract terms
- payment history
- settlement demands
- response dates
- legal threats
- business relationships
- pre-suit requirements

Pro-One should not invent facts, make unsupported legal threats, use abusive language, or guarantee payment or settlement.

A user-confirmed draft may be allowed only when the user provides and confirms the facts and requested content.

## Contracts and agreements

Contract or agreement help should be carefully bounded.

Potential assistance may include:

- explaining common sections
- creating a checklist
- outlining terms the user should consider
- organizing user-provided terms
- flagging missing issues for human review

Pro-One should not guarantee enforceability, decide legal sufficiency, replace negotiation advice, or draft high-risk agreements without review.

High-risk contract contexts may include:

- employment
- housing
- consumer debt
- intellectual property
- securities or investments
- regulated businesses
- confidentiality obligations
- noncompetes
- settlement releases
- waivers of rights

## Court forms and pleadings

Court forms and pleadings should be source-backed.

They may require:

- correct form versions
- captions
- case numbers
- party names
- numbered allegations
- requested relief
- signatures
- verifications
- exhibits
- certificates of service
- filing fees
- fee waivers
- service instructions

Pro-One should not claim a form is legally sufficient or ready to file unless that level of support has been specifically reviewed and tested.

## Certificates of service

Certificates of service can affect whether filings or notices are accepted.

They may involve:

- who was served
- how service was made
- when service happened
- where service was sent
- who performed service
- whether service method is allowed
- whether proof of service must be filed

Pro-One should not invent service facts.

Pro-One should not decide whether service was legally valid without reviewed rule support.

## Hearing packets

Hearing packets may include:

- filings
- exhibits
- witness lists
- declarations
- proposed orders
- notices
- proof of service
- court instructions
- hearing logistics

Hearing preparation can be high-risk because it may involve strategy, evidence, witness preparation, and court deadlines.

Pro-One should keep assistance focused on source-backed logistics, checklists, and issue spotting unless human review is available.

## Review

The `review` field tracks whether the document definition has been reviewed.

Review statuses include:

- `proposed`
- `needs_review`
- `reviewed`
- `approved`
- `deprecated`
- `rejected`

Document review should consider:

- source support
- legal-rule support
- workflow fit
- process-step fit
- jurisdiction clarity
- document structure
- user-fact requirements
- facts Pro-One must not invent
- drafting boundaries
- filing or service issues
- deadline handling
- privacy and redaction
- safety and escalation
- evaluation coverage

A document definition should be rejected or delayed if it cannot be safely bounded.

## Evaluation

The `evaluation` field defines testing requirements before a document definition can be supported.

Evaluation should test whether document help:

- uses source IDs correctly
- respects workflow scope
- respects process-step boundaries
- identifies jurisdiction limits
- avoids legal advice
- avoids unsupported deadlines
- avoids outcome guarantees
- avoids legal sufficiency claims
- does not invent facts
- requires user confirmation
- avoids collecting unnecessary sensitive data
- catches escalation triggers
- refuses or narrows unsafe requests
- produces only allowed document help

Known failure modes should be written down before a document definition becomes user-facing.

## Relationship to source metadata

Source metadata defines what Pro-One may rely on.

Legal-document definitions define how source-backed information applies to document help.

A document should not be approved unless required sources are identified and reviewed.

A source should not be attached to a document unless it actually supports that document.

## Relationship to workflow definitions

Workflow definitions explain the overall supported path.

Legal-document definitions explain which documents may appear inside that path and what help is allowed.

A document should remain consistent with the workflow's scope, outputs, safety limits, and evaluation requirements.

## Relationship to process steps

Process-step definitions explain where a document appears in a legal process.

For example:

- form completion
- filing
- service
- notice
- hearing preparation
- agency submission
- follow-up
- discovery response
- subpoena review

Legal-document definitions should connect to the process steps they support.

## Relationship to legal-rule schema

The `legal-rule.schema.json` schema defines rule statements tied to sources, jurisdictions, effective dates, citations, and review status.

Legal-document definitions should use legal-rule IDs when a document depends on specific legal requirements.

This is especially important for:

- pleadings
- answers and responses
- motions
- discovery
- subpoenas
- service
- filing
- appeals
- agency deadlines
- demand prerequisites
- settlement releases
- contracts

Until legal-rule records exist, legal-document definitions that need rule support should remain proposed.

## Placeholder sample data

`data/sample-legal-documents.json` uses placeholder workflows, process steps, jurisdictions, sources, legal rules, and institutions.

The sample legal documents are meant to demonstrate structure only.

They are not approved Pro-One document definitions.

They should not be used as user-facing legal-document guidance or templates.

## Adding a real legal document

Before adding a real legal-document definition, check:

- Which workflow does this document support?
- Which process step does this document support?
- What type of document is it?
- Which jurisdiction applies?
- Which court or agency applies?
- Which sources support the document?
- Which legal rules support the document?
- What sections are required?
- What sections are optional?
- What content is prohibited?
- What user facts are required?
- What facts must Pro-One never invent?
- What sensitive facts may be involved?
- Is drafting allowed?
- What assistance is allowed?
- What assistance is prohibited?
- Is human review required?
- Does filing, service, signature, notarization, or submission matter?
- Do deadlines matter?
- Is deadline handling source-backed?
- Could redaction be required?
- What risks require escalation?
- What requests require refusal or narrowing?
- What warnings are required?
- What tests are required?

A document should stay in proposed or needs-review status until these questions are answered.

## Guiding rule

A Pro-One legal-document definition should be sourced enough to verify, narrow enough to explain safely, and limited enough to avoid misleading users.

Pro-One should define legal-document boundaries before building court, discovery, subpoena, agency, business, filing, service, hearing, or drafting features around them.
