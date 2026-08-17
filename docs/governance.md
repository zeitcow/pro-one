# Governance

Pro-One is an early-stage open-source project focused on free, practical legal access for self-represented individuals and small businesses.

This document explains how the project should make decisions, review changes, and protect the mission as the repository grows.

## Current governance status

Pro-One is currently maintained by its project maintainer.

As the project grows, governance may expand to include:

- additional maintainers
- subject-matter reviewers
- legal-source reviewers
- privacy and security reviewers
- community contributors
- advisory contributors

Until that happens, project decisions should remain documented, reviewable, and consistent with the repository's mission, safety standards, privacy principles, source standards, and evaluation principles.

## Mission control

The project mission should guide all major decisions.

Pro-One should prioritize:

- free access
- practical usefulness
- plain-language legal information
- support for self-represented individuals
- support for small businesses
- source grounding
- privacy protection
- careful limits around legal advice
- transparent project status

The project should not become:

- a paid legal advice product
- a tool that pretends to replace lawyers
- a system that gives unsupported legal conclusions
- a system that hides uncertainty from users
- a system that collects unnecessary sensitive information

## Decision principles

Project decisions should be based on:

1. user need
2. legal safety
3. source availability
4. privacy impact
5. evaluation feasibility
6. technical maintainability
7. mission fit

A feature that is useful but unsafe should be delayed, narrowed, or redesigned.

A feature that cannot be grounded in reliable sources should not be presented as reliable legal information.

## Maintainer responsibilities

Maintainers are responsible for:

- protecting the mission
- reviewing pull requests
- keeping `main` stable
- avoiding unsupported claims
- preserving safety boundaries
- protecting user privacy
- keeping documentation accurate
- deciding when a proposed workflow is ready to build
- deciding when extra review is needed

Maintainers should favor small, clear changes over large changes that are hard to review.

## Contributor responsibilities

Contributors should:

- follow the repository workflow
- keep pull requests focused
- avoid committing sensitive information
- avoid overstating project capabilities
- distinguish planned work from completed work
- respect legal advice boundaries
- support legal claims with reliable sources
- explain safety, privacy, and source-grounding impacts when relevant

Contributors do not need to be lawyers to contribute, but legal-information changes require careful review.

## Review roles

Different changes may need different kinds of review.

Documentation review checks whether the project is described clearly and accurately.

Source review checks whether legal sources are reliable, current, usable, and connected to the intended workflow.

Safety review checks whether a change could mislead users, create legal risk, guess deadlines, mishandle jurisdiction, or make the project appear more authoritative than it is.

Privacy review checks whether the project collects, stores, logs, or exposes more user information than necessary.

Security review checks whether the change creates technical risk, exposes secrets, or weakens safe handling of user data.

Evaluation review checks whether a workflow can be tested before it is treated as supported.

## Changes that need extra review

Extra review is required for changes involving:

- user-facing legal output
- AI prompts
- retrieval behavior
- legal-source ranking
- jurisdiction handling
- citations
- deadlines
- document uploads
- data retention
- privacy settings
- security-sensitive code
- high-risk legal topics
- supported workflow expansion

These changes should not be merged casually.

## Supported workflow decisions

Pro-One should not support a legal workflow only because it sounds useful.

Before adding a workflow, the project should consider:

- who the workflow helps
- what problem it solves
- what legal sources are required
- which jurisdictions are involved
- what users could misunderstand
- what harms could happen if the output is wrong
- how the workflow can be evaluated
- whether the project can explain limitations clearly

Workflow selection is covered in more detail in `docs/workflow-selection.md`.

## Roadmap decisions

Roadmap changes should be documented.

A roadmap item should explain:

- what the project intends to build
- why it matters
- what risks exist
- what sources are needed
- what evaluation is needed
- what is not included yet

Roadmap items should not be written as if they are already completed.

## Source decisions

Legal sources should be added carefully.

The project should prefer:

- official sources
- primary legal materials
- court or agency materials
- public legal aid materials where appropriate
- clearly labeled secondary sources

Source decisions should consider:

- jurisdiction
- authority
- freshness
- citation quality
- reuse rights
- workflow fit
- limitations

A source should not be treated as reliable only because it is easy to access.

## Privacy and data decisions

Pro-One should collect as little user information as possible.

Before adding any feature that collects, stores, logs, or transmits user information, the project should ask:

- Is this information necessary?
- Can the workflow function with less information?
- How long is the information retained?
- Who can access it?
- Is the user clearly informed?
- Could the information expose legal, financial, family, housing, immigration, employment, or business risk?

Privacy decisions should be conservative.

## Public claims

Public project claims should be accurate.

The repository, README, documentation, issues, and public descriptions should not imply that Pro-One currently has features that do not exist yet.

For example, if a feature is planned, describe it as planned.

If a system has not been evaluated, do not describe it as reliable.

If a workflow is not supported, do not imply that it is supported.

## Conflict resolution

If contributors disagree, the project should resolve disagreements by returning to:

- the mission
- user safety
- source grounding
- privacy protection
- evaluation principles
- practical maintainability

When uncertainty remains, the safer choice should usually control.

## Governance updates

This governance document may change as Pro-One grows.

Future updates may add:

- maintainer selection criteria
- advisory review roles
- decision logs
- release rules
- security response procedures
- community standards
- formal review requirements

Governance should remain lightweight while the project is small, but it should become more formal before the project handles real user data, user-uploaded documents, or user-facing legal outputs.

## Guiding rule

Pro-One should move carefully.

The project should grow only in ways that preserve trust, safety, source grounding, privacy, and free practical legal access.
