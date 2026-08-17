# Source Standards

Pro-One should be grounded in reliable legal sources.

The project should not rely on unsupported model output for legal information. Legal explanations, workflow steps, citations, and warnings should be connected to sources that users can inspect and verify.

## Core standard

Pro-One should prefer official, primary, and clearly attributable sources.

The system should not invent:

- cases
- statutes
- court rules
- forms
- deadlines
- filing requirements
- legal tests
- citations
- procedural steps

When Pro-One cannot find reliable support, it should say so clearly.

## Source hierarchy

Preferred source order:

1. official statutes, rules, and regulations
2. official court rules
3. official court forms and instructions
4. official court self-help materials
5. primary legal authority
6. legal aid or public-interest explainers
7. secondary sources, clearly labeled

Primary, official, and public legal sources should be preferred where available.

Secondary sources may be useful for plain-language explanation, but they should not replace official or primary sources when those sources are available.

## Required source metadata

Each source should preserve useful metadata where possible, including:

- source title
- source type
- jurisdiction
- issuing court, agency, or organization
- publication date
- last updated date, if available
- source URL
- citation or rule number, if available
- retrieval date
- license or reuse information, if known

This metadata helps users understand where information came from and whether it may be current.

## Jurisdiction metadata

Every legal source should be connected to a jurisdiction where possible.

Jurisdiction metadata may include:

- federal
- state
- county
- city
- court
- agency
- tribunal
- administrative body

Pro-One should avoid mixing sources from different jurisdictions without making that clear.

## Source freshness

Legal sources can become outdated.

Pro-One should track freshness where possible, including:

- publication date
- last updated date
- retrieval date
- source version
- whether the source comes from an official website

When a source may be outdated, the system should warn the user.

Pro-One should not treat old or undated sources as automatically reliable for current legal requirements.

## Official source preference

Where possible, Pro-One should link users back to official sources.

Official sources may include:

- court websites
- court rule pages
- official court forms
- government websites
- agency websites
- official self-help centers
- official filing instructions

Official sources should be preferred over summaries, blogs, or commercial explainers.

## Reuse and licensing

Before adding sources to a corpus, the project should consider whether the source can be reused.

Source review should consider:

- public availability
- terms of use
- copyright status
- attribution requirements
- scraping restrictions
- redistribution limits
- update frequency
- official source URLs

The project should avoid adding source material when reuse rights are unclear and the use would create legal or ethical risk.

## Citation behavior

User-facing answers should show the sources used.

Citations should help users understand:

- what source supports the answer
- what jurisdiction the source applies to
- whether the source is official, primary, or secondary
- whether the source supports a rule, form instruction, deadline, or general explanation

Pro-One should not display citations that do not actually support the answer.

## Unsupported claims

Pro-One should reject or limit answers when retrieved sources do not support the requested legal information.

The system should not fill gaps with guesses.

Unsupported claims are especially risky when they involve:

- deadlines
- filing requirements
- court rules
- required forms
- service requirements
- appeal rights
- default judgments
- settlement consequences
- admissions or denials
- jurisdiction-specific procedures

## Plain-language summaries

Plain-language summaries should stay faithful to the source.

A summary should not remove important exceptions, conditions, warnings, or limits.

When the source is complex, Pro-One should explain that the rule may have exceptions or may require legal review.

## Corpus approval

Before a source becomes part of a supported workflow, the project should ask:

- Is this source reliable?
- Is this source official or primary?
- What jurisdiction does it apply to?
- Is it current?
- Can users verify it?
- Can the project reuse it?
- Does it support the workflow being built?
- Does it create safety concerns?

## Guiding rule

Pro-One should be useful because it is grounded, not because it sounds confident.

A limited answer with reliable sources is better than a broad answer without support.
