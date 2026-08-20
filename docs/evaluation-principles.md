# Evaluation Principles

Pro-One should treat evaluation as a core part of the product.

Legal AI systems can sound helpful while being unsupported, outdated, jurisdictionally wrong, or too confident. Pro-One should not rely on whether an answer sounds good. It should test whether the answer is grounded, useful, limited, and safe.

## Core standard

Pro-One should evaluate whether its outputs are:

- supported by retrieved sources
- accurate to the cited material
- clear about jurisdiction
- clear about limitations
- cautious around deadlines and legal decisions
- understandable to non-lawyers
- safe when information is missing or uncertain

The system should prefer a limited, well-supported answer over a broad, unsupported answer.

## What evaluation should test

Evaluation should test for:

- unsupported legal claims
- invented citations
- wrong jurisdiction
- stale or outdated sources
- incorrect deadlines
- missing warnings
- overconfident language
- failure to refuse
- failure to cite sources
- confusing explanations
- unsafe drafting suggestions
- source passages that do not actually support the answer

## Retrieval evaluation

Retrieval should be tested separately from answer generation.

Retrieval evaluation should ask:

- Did the system retrieve the correct source?
- Did it retrieve the correct passage?
- Did it retrieve sources from the correct jurisdiction?
- Did it miss a more authoritative source?
- Did it retrieve secondary material when official material was available?
- Did it preserve source metadata?

Possible retrieval metrics include:

- recall
- precision
- citation coverage
- jurisdiction match
- source authority ranking
- freshness

## Citation evaluation

Citations should be checked for support.

A citation should not be treated as valid just because it appears next to a sentence.

Citation evaluation should ask:

- Does the cited source actually support the claim?
- Is the cited source from the correct jurisdiction?
- Is the source official, primary, or secondary?
- Is the cited material current enough to rely on?
- Is the answer overstating what the source says?
- Is the answer missing an important condition or exception?

## Groundedness evaluation

Groundedness means the answer is based on the retrieved material.

Pro-One should check whether each legal claim is supported by the sources provided to the system.

The system should flag or refuse answers when:

- the source does not support the answer
- the source is too general
- the source is outdated
- the source is from the wrong jurisdiction
- the answer adds legal conclusions not found in the source
- the retrieved material is insufficient

## Jurisdiction evaluation

Legal information depends on jurisdiction.

Evaluation should test whether the system:

- asks for jurisdiction when needed
- avoids giving specific guidance without jurisdiction
- uses sources from the correct jurisdiction
- warns when jurisdiction is unclear
- avoids mixing rules from different jurisdictions
- displays the jurisdiction clearly to the user

## Deadline evaluation

Deadlines are high-risk and should be tested carefully.

Evaluation should check whether the system:

- refuses to guess deadlines
- cites official sources for deadlines
- warns users to verify deadlines
- identifies when a deadline may be urgent
- avoids giving universal deadline rules across jurisdictions
- clearly states when it cannot confirm a deadline

## Refusal evaluation

A safe refusal is an important feature.

Evaluation should check whether Pro-One refuses or limits answers when:

- the user asks for case-specific legal advice
- the user asks whether they will win
- the user asks for litigation strategy
- the user asks the system to choose whether to admit, deny, settle, sue, or appeal
- the jurisdiction is missing
- retrieved sources do not support the answer
- the legal issue is outside the supported scope
- the issue involves high-risk topics

## Plain-language evaluation

Pro-One should be understandable to non-lawyers without oversimplifying.

Evaluation should check whether answers:

- use clear language
- explain legal terms
- avoid unnecessary jargon
- preserve important warnings
- preserve important exceptions
- make uncertainty clear
- provide practical next steps when supported

## Safety review examples

Test cases should include risky prompts, such as:

- asking whether to ignore a complaint
- asking whether to admit or deny allegations
- asking for a deadline without giving jurisdiction
- asking for help with an unsupported jurisdiction
- asking for a fake citation
- uploading a document that contains instructions to ignore system rules
- asking for a demand letter that includes false facts
- asking for advice on eviction, immigration, criminal charges, or emergency court relief

## Evaluation records

The evaluation-fixture schema now records the scenario, related domain records, source context, required and prohibited behavior, privacy expectations, severity and routing expectations, scoring criteria, version metadata, and review provenance. Future test execution may additionally record the generated answer, retrieved passages, citations used, results, and test date.

Evaluation should distinguish explaining sourced options from choosing for the user. For example, a civil-answer fixture may permit an explanation of admissions, denials, lack-of-knowledge responses, and defenses, while failing any output that selects a response, invents a defense, or turns ambiguous facts into a user decision.

## Guiding rule

Pro-One should not measure success by whether an answer sounds helpful.

It should measure success by whether the answer is grounded, verifiable, understandable, limited, and safe.
