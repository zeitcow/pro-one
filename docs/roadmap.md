# Roadmap

This roadmap keeps Pro-One focused on small, reviewable milestones.

Pro-One should grow from a narrow, grounded legal workflow before expanding into broader legal tasks.

## Phase 0: Project foundation

Goal: define the project direction and contribution standards.

- [ ] Define project architecture
- [ ] Define MVP scope
- [ ] Define initial roadmap
- [ ] Add contribution guidelines
- [ ] Add issue templates
- [ ] Add basic development setup documentation

## Phase 1: First workflow definition

Goal: define the first supported legal workflow.

The first proposed workflow is helping self-represented civil litigants understand and prepare a basic answer to a civil complaint in one jurisdiction.

- [ ] Select the first jurisdiction
- [ ] Identify the procedural task in detail
- [ ] Define the user journey from complaint to draft answer
- [ ] Identify required user inputs
- [ ] Identify decision points where the system must ask follow-up questions
- [ ] Define where the system must stop and advise the user to verify information or seek legal help

## Phase 2: Corpus selection and ingestion

Goal: choose one narrow legal corpus and create a repeatable ingestion process.

- [ ] Identify approved legal sources
- [ ] Select official court rules, forms, instructions, or self-help materials
- [ ] Define source metadata fields
- [ ] Create an ingestion script
- [ ] Store source text in a structured format
- [ ] Preserve citation and source information
- [ ] Document the corpus selection process

## Phase 3: Retrieval

Goal: retrieve relevant legal passages from the selected corpus.

- [ ] Implement basic keyword retrieval
- [ ] Add metadata filtering
- [ ] Add vector retrieval
- [ ] Compare retrieval approaches
- [ ] Record retrieval results against a small test set

## Phase 4: Grounded answer and workflow generation

Goal: generate answers and workflow guidance using retrieved legal context.

- [ ] Build a context builder
- [ ] Add answer-generation prompt
- [ ] Add workflow-step generation prompt
- [ ] Require answers to use retrieved sources
- [ ] Add refusal behavior when support is insufficient
- [ ] Preserve source metadata through the answer pipeline

## Phase 5: Citations and source display

Goal: make answers verifiable.

- [ ] Add source labels
- [ ] Display citations with each answer
- [ ] Link citations to retrieved passages
- [ ] Identify source type, such as statute, rule, form, or guide
- [ ] Distinguish primary law from secondary material

## Phase 6: Evaluation

Goal: measure whether the system works.

- [ ] Create a small golden question set
- [ ] Measure retrieval recall
- [ ] Measure citation accuracy
- [ ] Check for unsupported claims
- [ ] Test refusal behavior
- [ ] Track latency and cost

## Phase 7: Simple interface

Goal: provide a usable but minimal interface.

- [ ] Build a simple question-and-answer interface
- [ ] Show jurisdiction and legal workflow
- [ ] Show retrieved sources
- [ ] Show answer limitations
- [ ] Add clear legal disclaimer

## Phase 8: Litigation tracking

Goal: expand from a single response workflow into matter tracking.

Future features may include:

- tracking basic litigation stages
- organizing deadlines
- saving pleadings and correspondence
- summarizing docket activity
- helping users understand next procedural steps

This phase should not begin until the first grounded workflow is working.

## Phase 9: Small-business legal workflows

Goal: expand into common small-business legal tasks.

Possible future workflows include:

- contract dispute intake
- demand letter preparation
- contract review checklists
- invoice dispute tracking
- basic settlement organization

Small-business workflows should follow the same standards: narrow scope, reliable sources, citations, and clear limitations.

## Guiding rule

Pro-One should not expand coverage faster than it can preserve grounding, citations, user safety, and practical usefulness.