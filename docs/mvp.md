# MVP

The first Pro-One MVP should be intentionally narrow.

The goal is to prove that the project can support one legal workflow with grounded legal information, citations, and clear limitations.

## MVP direction

The first MVP will focus on helping a self-represented civil litigant understand and prepare a basic answer to a civil complaint in one jurisdiction.

The goal is not to replace a lawyer or provide case-specific legal advice. The goal is to help users understand the procedural path, organize their facts, identify relevant court rules and official resources, and prepare a draft response that they can review before filing.

## MVP goal

Build a small working system that can:

1. accept a user's legal question, document, or task description
2. identify the supported jurisdiction and legal workflow
3. retrieve relevant passages from an approved legal corpus
4. generate plain-language guidance based on those passages
5. show citations to the supporting sources
6. explain limitations when the retrieved material is insufficient

## Initial scope

The MVP should include:

- one user type: self-represented civil litigants
- one jurisdiction
- one procedural task: understanding and preparing a basic answer to a civil complaint
- one approved legal corpus
- one retrieval pipeline
- cited procedural guidance
- plain-language explanations
- clear refusal or limitation behavior when the system cannot find adequate support

## Required behavior

The MVP should:

- cite the sources used in the answer
- distinguish supported guidance from unsupported claims
- avoid making claims that are not supported by retrieved material
- tell the user when it cannot find enough information
- avoid presenting itself as a lawyer
- avoid creating the impression of an attorney-client relationship
- clearly warn users about deadlines, court rules, and the need to verify information before filing

## Out of scope

The first MVP should not include:

- payments
- user accounts
- document filing
- attorney matching
- multi-jurisdiction coverage
- broad legal advice
- automated court submissions
- complex case strategy
- production deployment
- mobile apps
- advanced UI polish

## Candidate first corpus

The first corpus should be small enough to inspect and test.

Possible candidates:

- official court self-help materials for answering a complaint
- civil procedure rules for one jurisdiction
- official answer forms and instructions
- a narrow set of statutes or court rules relevant to the selected workflow

The final corpus should be selected based on source quality, public availability, and ease of citation.

## Success criteria

The MVP is successful when a user within the supported scope can receive:

- a clear explanation of the procedural task
- a structured set of next steps
- supporting citations
- a visible jurisdiction
- a limitation statement where appropriate
- no unsupported legal claims

## Example user experience

```text
User:
I was served with a civil complaint. What do I need to do?

System behavior:
- identify that the user is asking about responding to a civil complaint
- confirm or request jurisdiction
- retrieve relevant court rules, official instructions, and forms
- explain the answer deadline and basic response options if supported by sources
- guide the user through admissions, denials, lack of knowledge, and possible defenses at a high level
- show citations
- explain limits if facts, jurisdiction, or source support are unclear
```

## Development principle

The MVP should favor correctness, transparency, and narrow scope over broad coverage.
