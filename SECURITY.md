# Security

Pro-One is an early-stage project, but security should be part of the foundation from the beginning.

Because Pro-One may eventually handle legal questions, court papers, contracts, deadlines, business disputes, and other sensitive information, the project should treat privacy, security, and user safety as core requirements.

## Current status

Pro-One does not currently operate a production application or accept user legal documents.

This security policy describes the standards the project should follow as it develops.

## Reporting security issues

If you discover a security issue, please do not open a public GitHub issue with sensitive details.

Instead, report the issue privately to the project maintainer.

Until a dedicated security contact is added, security reports should be sent through the repository owner's available GitHub contact methods.

## Security principles

Pro-One should be designed around these principles:

- collect the least amount of user data necessary
- avoid storing sensitive legal facts unless required
- protect court documents, contracts, names, addresses, deadlines, and other sensitive information
- avoid exposing user data in logs, analytics, prompts, or error messages
- avoid using user legal facts for model training without clear consent
- make data retention and deletion practices clear
- design for safe failure when AI, retrieval, or source grounding does not work

## Threat model

Future versions of Pro-One should consider risks such as:

- accidental exposure of user legal documents
- storage of sensitive legal facts without a clear purpose
- prompt injection through uploaded documents
- leaked API keys or credentials
- model output that invents legal authority
- fake or unsupported citations
- wrong jurisdiction detection
- stale legal sources
- incorrect deadline guidance
- overconfident legal explanations
- malicious attempts to generate fraudulent or abusive documents

## Sensitive data

Pro-One should treat the following as sensitive:

- court documents
- contracts
- names and addresses
- financial information
- business records
- employment facts
- immigration facts
- family or housing facts
- medical information
- case deadlines
- correspondence with lawyers, courts, agencies, or opposing parties

The project should avoid collecting or storing this information unless it is necessary for a specific workflow and appropriate safeguards exist.

## AI-specific security risks

Legal AI systems have risks beyond ordinary web applications.

Pro-One should account for:

- prompt injection in uploaded documents
- retrieved text that tries to override system behavior
- unsupported model output
- invented citations
- jurisdiction mismatch
- hidden uncertainty
- unsafe instructions framed as legal guidance

The system should not treat model output as reliable unless it is supported by retrieved sources and appropriate safety checks.

## Dependency and secret management

Future code contributions should avoid:

- committing API keys
- committing credentials
- committing private user data
- logging sensitive user input
- storing secrets in source files
- adding unnecessary dependencies

Secrets should be stored through environment variables or a dedicated secret-management process.

## Responsible disclosure

Security issues should be handled carefully and privately until they are fixed.

Public issues may be appropriate for general security improvements, but not for active vulnerabilities or sensitive user data exposure.
