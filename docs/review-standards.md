# Review Standards

Pro-One should review contributions carefully because the project deals with legal information, privacy, source grounding, and AI safety.

This document explains what reviewers should check before approving or merging changes.

## Core review standard

A change should be:

- accurate about the project's current status
- aligned with Pro-One's mission
- narrow enough to review
- clear about limitations
- careful with legal information
- respectful of privacy and security
- grounded in reliable sources when legal claims are involved

A contribution should not make Pro-One appear more capable, complete, or legally authoritative than it is.

## General review checklist

Before merging, reviewers should check:

- Does the change do what the pull request says it does?
- Is the scope focused?
- Are unrelated changes avoided?
- Is the wording clear?
- Are planned features described as planned rather than already available?
- Does the change preserve the free and open legal-access mission?
- Does the change avoid unsupported legal claims?
- Does the change avoid exposing sensitive information?
- Does the change introduce any safety concerns?

## Documentation review

Documentation should be clear, accurate, and current.

Reviewers should check whether documentation:

- matches the current state of the repository
- avoids overstating features
- avoids implying Pro-One provides legal advice
- distinguishes legal information from legal advice
- explains limitations clearly
- uses plain language where possible
- stays consistent with existing mission, safety, privacy, source, and evaluation documents

Documentation-only changes should still be reviewed carefully because they define the project's public commitments and boundaries.

## Legal-information review

Changes involving legal information require extra care.

Reviewers should check whether the change:

- identifies the relevant jurisdiction
- cites or references reliable sources
- preserves source metadata
- avoids guessing deadlines
- avoids unsupported legal conclusions
- distinguishes official, primary, and secondary sources
- warns when information is incomplete or uncertain
- stays within the supported workflow

If a legal claim is not supported, it should be removed, limited, or rewritten.

## Source-grounding review

For source or corpus changes, reviewers should check:

- Is the source reliable?
- Is it official, primary, or clearly labeled as secondary?
- What jurisdiction does it apply to?
- Is it current?
- Can users verify it?
- Can the project reuse it?
- Is citation metadata preserved?
- Does the source support the workflow being built?
- Are any limitations or safety concerns documented?

Sources should not be added only because they are convenient.

## Privacy review

Reviewers should check whether a change collects, stores, exposes, logs, or transmits user information.

Extra caution is required for:

- names
- addresses
- court papers
- contracts
- business records
- financial information
- employment facts
- housing facts
- family facts
- immigration facts
- medical information
- deadlines
- user-uploaded documents
- communications with lawyers, courts, agencies, or opposing parties

A change should collect less data where possible.

## Security review

Reviewers should check whether a change could expose the project or users to security risks.

Do not merge changes that include:

- API keys
- credentials
- private user data
- real user legal documents
- sensitive logs
- environment files with secrets
- unnecessary dependencies
- unsafe handling of uploaded documents

Future code changes should also consider prompt injection, dependency risk, access controls, and safe handling of third-party services.

## AI safety review

Changes involving AI prompts, retrieval, generation, evaluation, or model behavior require extra review.

Reviewers should check whether the change:

- prevents unsupported legal answers
- avoids invented citations
- preserves jurisdiction awareness
- supports refusal behavior
- handles uncertainty clearly
- avoids overconfident language
- keeps users in control
- avoids pretending the system is a lawyer
- is testable through evaluation examples or fixtures

AI output should not be treated as reliable unless it is supported by sources and safety checks.

## Deadline and high-risk topic review

Deadline-related and high-risk legal topics require the most caution.

Reviewers should be especially careful with changes involving:

- court deadlines
- defaults
- appeals
- eviction
- foreclosure
- bankruptcy
- criminal matters
- immigration
- family law
- domestic violence
- child custody
- emergency court relief
- loss of housing, liberty, status, custody, or major financial rights

If a change cannot be made safely, it should be delayed or narrowed.

## Pull request review questions

Before approving a pull request, ask:

- Is this change accurate?
- Is it narrow?
- Is it grounded?
- Is it safe?
- Is it clear about limits?
- Does it protect user privacy?
- Does it avoid overstating Pro-One's capabilities?
- Does it move the project toward practical legal access?

## When to request changes

Request changes when a pull request:

- overstates the project
- implies legal advice
- lacks source support for legal claims
- guesses deadlines
- ignores jurisdiction
- exposes sensitive data
- weakens privacy or security standards
- removes important safety limitations
- combines too many unrelated changes
- is difficult to review

## Guiding rule

A careful review protects users and the project.

For Pro-One, accuracy, safety, and trust matter more than speed.
