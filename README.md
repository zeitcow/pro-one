# Pro-One

**Free, open-source legal AI for people and small businesses handling legal matters on their own.**

Pro-One is an early-stage project exploring how AI and open-source software can help people understand, organize, and complete common legal tasks.

The goal is not to build a general-purpose legal chatbot. The goal is to build task-focused legal tools that are grounded in reliable sources, transparent about limitations, and useful to people who may not have easy access to legal help.

## Project status

Pro-One is in early development. The current work is focused on defining the project architecture, MVP scope, and contribution roadmap.

The repository does not yet contain a working legal AI application. The documents in this repository describe the direction of the project and the standards future features should meet.

## Principles

- **Free to use:** Core access should not depend on a user's ability to pay.
- **Open source:** The software can be inspected, improved, and built on by others.
- **Practical:** Tools should be designed around specific legal tasks and workflows.
- **Grounded:** AI responses should be based on retrieved legal sources rather than unsupported generation.
- **Transparent:** Users should be able to see the sources, jurisdiction, confidence, and limitations behind an answer.
- **Human-directed:** Users remain responsible for their legal decisions and should not be pushed into automated legal conclusions.

## Intended architecture

Pro-One is being designed around a grounded legal-information pipeline:

```text
user question
  -> jurisdiction and topic detection
  -> retrieval from approved legal sources
  -> context builder
  -> grounded answer
  -> citations
  -> confidence and limitations