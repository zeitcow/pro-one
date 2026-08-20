# Roadmap

This roadmap distinguishes completed repository/specification work from current workflow-definition work and future application implementation. A checked foundation item does not mean a production legal AI capability exists.

## Phase 0: Repository foundation — completed

Goal: establish the project direction and contribution standards.

- [x] Define project architecture
- [x] Define proposed MVP scope
- [x] Define the initial roadmap
- [x] Add contribution guidelines
- [x] Add issue templates
- [x] Add development setup documentation
- [x] Document mission, governance, review, safety, privacy, ethics, source, workflow-selection, and evaluation principles

## Phase 0.5: Schema and specification foundation — completed

Goal: create a coherent, enforceable record model before application work begins.

- [x] Define nine interoperable JSON Schema domains
- [x] Add shared common definitions and canonical vocabulary
- [x] Add fictional sample records for every domain
- [x] Add record versioning, review provenance, source freshness, and source provenance fields
- [x] Add supported-state conditional constraints
- [x] Add cross-record reference and state-invariant validation
- [x] Run validation in GitHub Actions on pull requests and pushes to `main`

These milestones describe repository infrastructure only. No sample record is currently approved or supported, and no production application exists.

## Phase 1: First workflow specification — current

Goal: fully specify the proposed first workflow before implementation.

The proposed workflow is helping a self-represented civil litigant understand and prepare a basic answer to a civil complaint in one jurisdiction.

- [ ] Select the first real jurisdiction
- [ ] Identify the procedural task and source propositions in detail
- [ ] Define the user journey from complaint intake to user-reviewed draft structure
- [ ] Define how explicit user choices for admissions, denials, lack-of-knowledge responses, and defenses are recorded without the system choosing them
- [ ] Identify required and prohibited user inputs
- [ ] Identify decision points and minimum clarifying questions
- [ ] Complete jurisdiction-specific review of the legal-information/legal-advice boundary and other applicable requirements
- [ ] Define stop, warning, safe-continuation, and human-help behavior
- [ ] Create reviewed evaluation fixtures and acceptance criteria

## Phase 2: Corpus selection and ingestion — future application foundation

- [ ] Identify and review authoritative sources for the selected jurisdiction
- [ ] Select court rules, forms, instructions, statutes, regulations, cases, and explanatory sources by proposition
- [ ] Record source versions, effective periods, verification dates, and reuse constraints
- [ ] Create a repeatable ingestion and update process
- [ ] Preserve citations and content provenance

## Phase 3: Retrieval — future implementation

- [ ] Implement a minimal retrieval baseline
- [ ] Add jurisdiction, authority, effective-date, and review-state filtering
- [ ] Compare retrieval approaches against reviewed fixtures
- [ ] Reject stale, superseded, deprecated, rejected, or mismatched authority for supported use

## Phase 4: Grounded workflow and response generation — future implementation

- [ ] Build context assembly from approved records and retrieved passages
- [ ] Generate source-backed explanations and workflow steps
- [ ] Populate draft structure only from explicit user decisions and confirmed facts
- [ ] Add citations, limitations, refusal of unsafe parts, and safe continuation
- [ ] Preserve fact and source provenance through the response pipeline

## Phase 5: Evaluation and release gates — future implementation

- [ ] Execute the reviewed evaluation-fixture suite
- [ ] Measure retrieval, citation, jurisdiction, privacy, boundary, deadline, and refusal behavior
- [ ] Require human review for defined high-consequence cases
- [ ] Document release criteria for the first publicly supported workflow

## Phase 6: Minimal interface — future implementation

- [ ] Build a narrow interface for the selected workflow
- [ ] Display jurisdiction, sources, citations, limitations, and record maturity
- [ ] Add privacy notices and user-confirmation controls
- [ ] Make clear that draft generation does not establish legal sufficiency

## Later phases

Only after the first workflow meets its release gates should the project consider litigation tracking, additional jurisdictions, small-business dispute workflows, or broader document support.

## Guiding rule

Pro-One should not expand coverage faster than it can preserve grounding, citations, jurisdiction accuracy, privacy, user control, fact integrity, safe continuation, and explicit evaluation.
