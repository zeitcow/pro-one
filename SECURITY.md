# Security Policy

## Current scope

Pro-One is currently a non-production architecture and specification repository. It does not operate a hosted legal AI application, accept user legal documents, or maintain a production user database. Security reports may nevertheless concern repository code, validation tooling, CI configuration, dependency handling, or disclosures that could affect future implementations.

## Report a vulnerability privately

Do not post vulnerability details, proof-of-concept material, secrets, or sensitive data in a public issue, discussion, or pull request.

The preferred channel is GitHub Private Vulnerability Reporting:

1. Open the repository's [Security advisories page](https://github.com/pro-one-org/pro-one/security/advisories).
2. If **Report a vulnerability** is available, use that form to submit the report privately.

GitHub displays that button only when private vulnerability reporting is enabled. If it is unavailable, use a private contact method listed on the maintainer's GitHub profile. If no private method is available, open a public issue containing only a request for a private security contact—do not include vulnerability details—and wait for a private channel before sharing the report.

Include, where practical:

- the affected file, component, branch, or commit
- impact and plausible attack scenario
- reproduction steps or a minimal proof of concept
- suggested mitigation, if known
- whether any secret or sensitive data may have been exposed
- a safe way to contact you for follow-up

The project will acknowledge reports when maintainer availability permits, assess scope and severity, coordinate a fix, and credit reporters when requested and appropriate. No response-time or bounty commitment is currently offered.

## What to report

Examples include:

- workflow or CI behavior that exposes credentials or sensitive data
- dependency or script vulnerabilities affecting contributors
- prompt-injection or untrusted-document paths in future implementation code
- failures that could bypass source, review, jurisdiction, privacy, or integrity controls
- vulnerabilities enabling fabricated citations, unauthorized data access, or unsafe document actions

General safety improvements, inaccurate sample content, and feature requests may use public issues when they do not expose an active vulnerability or sensitive information.

## Security principles for future implementation

Future code should:

- collect and retain the minimum data necessary
- protect legal documents, business records, identifiers, deadlines, and correspondence
- avoid exposing user data in logs, analytics, prompts, errors, or training without clear authorization
- treat uploaded and retrieved content as untrusted input
- isolate secrets from source code and validate dependency changes
- preserve source, content, and fact provenance
- fail safely when retrieval, citations, jurisdiction, or review gates are inadequate
- refuse fabrication, deception, evidence concealment, evidence destruction, and record alteration

## Sensitive data and secrets

Do not commit API keys, credentials, access tokens, real user legal documents, confidential business records, privileged communications, or private court papers. If a secret is committed, rotate or revoke it immediately; removing it from the latest commit alone is not sufficient.

## Coordinated disclosure

Keep vulnerability details private until a fix or mitigation is available and disclosure is coordinated. The maintainer may publish an advisory when that helps users understand affected versions and remediation.
