# Development Setup

Pro-One is an early-stage project. The repository currently focuses on documentation, project standards, safety principles, evaluation principles, and planning for future legal AI workflows.

This guide explains how to set up the repository locally and make small, reviewable contributions.

## Current project status

Pro-One does not currently include a production application, backend service, frontend app, database, or AI pipeline.

At this stage, contributors can work on:

- documentation
- source standards
- safety standards
- evaluation planning
- workflow planning
- issue templates
- future schema and corpus design

Application setup instructions should be added when the project includes runnable code.

## Prerequisites

Recommended tools:

- Git
- GitHub account
- code editor such as VS Code
- terminal such as PowerShell, Terminal, or a Unix shell

Future code contributions may require additional tools, but those should be documented when they are introduced.

## Clone the repository

Clone the repository from GitHub:

    git clone https://github.com/zeitcow/pro-one.git
    cd pro-one

Check the repository status:

    git status

Expected result:

    On branch main
    nothing to commit, working tree clean

## Configure Git identity

Use a Git identity that you are comfortable using for public open-source contributions.

Check your current Git configuration:

    git config user.name
    git config user.email

Set local repository identity if needed:

    git config user.name "Your Name"
    git config user.email "your-email@example.com"

Contributors who prefer not to expose a personal email address should consider using a GitHub-provided no-reply email address.

## Keep work on branches

Do not make changes directly on `main`.

Create a branch for each small contribution:

    git checkout main
    git pull origin main
    git checkout -b docs/example-change

Branch names should be short and descriptive.

Examples:

- `docs/development-setup`
- `docs/source-metadata`
- `schema/source-metadata`
- `tests/evaluation-fixtures`

## Make small changes

Pro-One should favor small, reviewable changes.

A good contribution should usually do one thing:

- add one focused document
- update one standard
- add one schema
- add one test fixture
- improve one workflow description
- fix one bug or inconsistency

Avoid mixing unrelated changes in the same pull request.

## Check changes before committing

Before committing, review the changed files:

    git status
    git diff

For Markdown and text changes, also check for whitespace issues:

    git diff --check

After staging files, check the staged diff:

    git add path/to/file.md
    git diff --staged --check
    git diff --staged --stat

## Commit messages

Use clear commit messages.

Examples:

- `docs: add development setup guide`
- `docs: update source standards`
- `schema: add source metadata schema`
- `tests: add retrieval evaluation fixtures`

Commit messages should describe what changed, not just that something was updated.

## Push and open a pull request

Push the branch:

    git push -u origin branch-name

Open a pull request on GitHub.

The pull request should explain:

- what changed
- why the change is useful
- whether it affects legal information, safety, privacy, evaluation, or source grounding
- how it was reviewed or tested

## After a pull request is merged

After a pull request is merged, update local `main`:

    git checkout main
    git pull origin main
    git status

Then delete the local branch:

    git branch -d branch-name

If the pull request was squash-merged and Git warns that the branch is not fully merged, it is usually safe to delete the local branch after confirming the PR was merged:

    git branch -D branch-name

Delete the remote branch if it is no longer needed:

    git push origin --delete branch-name

## Secrets and sensitive information

Do not commit:

- API keys
- credentials
- private user data
- legal documents from real users
- confidential business records
- private court papers
- sensitive prompts or outputs
- environment files containing secrets

Future code should use environment variables or a dedicated secret-management process for secrets.

## Windows and PowerShell notes

PowerShell may show warnings such as:

    LF will be replaced by CRLF

This is common on Windows and usually not a problem.

If a file already exists, PowerShell may show an error when using `ni` or `New-Item`. That is usually harmless if the file was already created intentionally.

## Guiding rule

Set up the project in a way that keeps contributions small, public, reviewable, and safe.

Pro-One should grow carefully, especially where changes affect legal information, privacy, source grounding, or user safety.
