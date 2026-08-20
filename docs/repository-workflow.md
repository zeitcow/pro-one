# Repository Workflow

This guide explains how work should move through the Pro-One repository.

The goal is to keep changes organized, reviewable, and aligned with Pro-One's mission, safety standards, privacy principles, and source-grounding requirements.

## Core workflow

Use this workflow for most contributions:

1. start from a clean `main` branch
2. create a focused feature branch
3. make a small change
4. review the diff locally
5. commit with a clear message
6. open a pull request
7. review the pull request before merging
8. squash merge into `main`
9. sync local `main`
10. delete old branches

## Start from clean main

Before starting work, run:

    git checkout main
    git pull origin main
    git status

Expected result:

    On branch main
    Your branch is up to date with 'origin/main'.
    nothing to commit, working tree clean

Do not start a new change from an old feature branch.

## Branch naming

Use short, descriptive branch names.

Recommended prefixes:

- `docs/` for documentation
- `schema/` for schemas
- `data/` for sample data or corpus metadata
- `tests/` for evaluation fixtures or tests
- `fix/` for bug fixes
- `chore/` for maintenance

Examples:

- `docs/repository-workflow`
- `docs/governance`
- `schema/source-metadata`
- `data/sample-sources`
- `tests/evaluation-fixtures`

## Pull request size

Pull requests should be small enough to review carefully.

A pull request should usually focus on one topic, such as:

- one documentation area
- one schema
- one sample dataset
- one evaluation fixture set
- one bug fix
- one safety improvement

Avoid combining unrelated changes.

## Pull request titles

Use clear pull request titles.

Examples:

- `docs: add repository workflow guide`
- `docs: add review standards`
- `docs: add workflow selection criteria`
- `schema: add source metadata schema`
- `data: add sample source metadata`
- `tests: add evaluation fixtures`

## Pull request description

Each pull request should explain:

- what changed
- why the change is useful
- whether it affects legal information, safety, privacy, evaluation, or source grounding
- how the change was reviewed or tested

For documentation-only changes, say that the pull request does not add application code.

## Review before merging

Before merging, check:

- the diff is limited to the intended files
- the change does not overstate project capabilities
- planned features are not described as existing features
- legal information standards are preserved
- privacy and security standards are preserved
- source-grounding expectations are clear
- Markdown formatting is not broken

For Markdown changes, run:

    python scripts/validate_repository.py
    git diff --check
    git diff --staged --check

## Merge style

Prefer squash merging.

Squash merging keeps `main` clean by turning a branch into one clear commit.

The squash commit title should usually match the pull request title.

Example:

    docs: add repository workflow guide

The extended description should briefly summarize the change.

## After merging

After a pull request is merged, sync local `main`:

    git checkout main
    git pull origin main
    git status

Delete the local branch:

    git branch -d branch-name

If the branch was squash-merged and Git warns that it is not fully merged, confirm the pull request was merged on GitHub, then delete the local branch:

    git branch -D branch-name

Delete the remote branch:

    git push origin --delete branch-name

## Issue workflow

Use issues to track planned work.

Issue templates should help separate:

- bugs
- feature requests
- source review
- safety review

Safety-sensitive issues should be labeled clearly and handled carefully.

Do not include sensitive user data, private legal documents, credentials, or active vulnerability details in public issues.

## Documentation workflow

Documentation should be accurate about the project's current status.

When writing documentation:

- distinguish current features from planned features
- avoid claiming Pro-One provides legal advice
- avoid claiming a production system exists before it does
- preserve the free and open legal-access mission
- connect legal AI features to source grounding, citations, privacy, and safety
- keep wording clear enough for non-lawyers where possible

## Source and corpus workflow

Source or corpus contributions should follow the source standards.

Before adding a source, consider:

- reliability
- jurisdiction
- source type
- freshness
- reuse rights
- citation metadata
- safety concerns
- workflow relevance

Legal sources should not be added casually.

## Safety-sensitive workflow

Some changes require extra caution.

Examples include changes that affect:

- legal advice boundaries
- deadlines
- jurisdiction handling
- citations
- source ranking
- privacy
- document uploads
- user data storage
- AI prompts
- refusal behavior
- high-risk legal topics

These changes should be reviewed more carefully than ordinary documentation or formatting changes.

## Guiding rule

The repository workflow should keep Pro-One careful, transparent, and reviewable.

Small, accurate changes are better than large changes that are difficult to verify.
