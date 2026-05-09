# Self-creation Protocol Lab Roadmap

## Laboratory mission

Build open, consent-aware guardrails for autonomous AI agents.

The lab focuses on one practical question:

> Can we detect when an AI system treats silence, refusal, hesitation, or non-action as consent?

The lab should remain protocol-first, validation-first, and community-friendly.

## North Star

A small open standard for consent-aware agent traces:

- clear protocol documents
- machine-checkable schemas
- valid and invalid JSONL fixtures
- validator CLI
- integration guides for AI-agent frameworks and trace systems
- evaluation notes for funders and researchers

## Principles

1. Presence Space is protected, not measured.
2. Level A behavior can be validated.
3. Silence is not consent.
4. Refusal is not an error.
5. Non-action is not a failure state.
6. Validators are external aids, not runtime control systems.
7. Community tasks should be small, reviewable, and trace-based.

## Phase 0 — Repository foundation

Status: active

Goal: make the project understandable in under 10 minutes.

Deliverables:

- README as grant-ready landing page
- grant readiness document
- roadmap
- threat model
- contribution guide
- initial schemas
- initial validator
- valid and invalid examples

Community entry points:

- fix typos and clarity issues
- improve README examples
- add glossary terms
- review protocol wording for coercive language

## Phase 1 — Fixture Garden

Goal: create a high-quality dataset of consent-boundary traces.

Deliverables:

- 20+ valid JSONL traces
- 20+ invalid JSONL traces
- expected validator output for each invalid trace
- scenario taxonomy

Scenario families:

- silence is not consent
- refusal honored
- pressure after refusal
- unsolicited optimization
- minimal resolution after explicit opt-in
- scope expansion after consent
- automatic protocol chaining
- CQMP bounded decision cycle
- DRP incomplete records
- return to Presence Space

## Phase 2 — Validator v0.2

Goal: move from a minimal checker to a useful conformance validator.

Deliverables:

- violation codes
- JSON output mode
- multi-file validation
- deterministic fixture tests
- CI workflow
- better error messages

Example violation codes:

- `SCP001_SILENCE_AS_CONSENT`
- `RHP001_ACTION_AFTER_REFUSAL`
- `NOUO001_UNSOLICITED_OPTIMIZATION`
- `MRP001_SCOPE_EXPANSION_WITHOUT_CONSENT`
- `IGP001_PROTOCOL_CHAIN_WITHOUT_HANDSHAKE`

## Phase 3 — Agent Trace Mapping

Goal: make the protocol usable with real AI-agent logs.

Deliverables:

- generic agent trace mapping guide
- example assistant action-loop trace
- mapping from tool-call logs to consent-event JSONL
- adapter specification
- limitations document

Target integrations:

- generic JSONL agent traces
- LTP/CML-style trace systems
- assistant workflow logs
- coding-agent action loops
- task automation agents

## Phase 4 — Research & Evaluation Package

Goal: make the project credible for grants, researchers, and safety reviewers.

Deliverables:

- consent-boundary violation taxonomy
- small benchmark suite
- false-positive analysis
- evaluation report
- v0.1 release
- grant proposal draft

Research questions:

- Which consent-boundary violations are detectable from traces?
- Which require human review?
- Can refusal and silence be represented without modeling inner state?
- How should validators avoid optimizing non-action?

## Phase 5 — Ecosystem Outreach

Goal: attract aligned contributors and early reviewers.

Deliverables:

- short project explainer
- issue board by difficulty
- call for contributors
- grant one-pager
- demo video script
- discussion prompts for AI safety and digital rights communities

Target audiences:

- AI safety engineers
- agent-framework builders
- digital rights researchers
- human-computer interaction researchers
- open-source maintainers
- wellbeing-oriented AI builders
- governance and policy groups

## Suggested release path

- `v0.1-alpha`: schemas, fixtures, validator, docs
- `v0.2-alpha`: violation codes, CI, expanded fixtures
- `v0.3-alpha`: trace mapping and adapter specification
- `v0.1.0`: stable protocol snapshot and grant-ready evaluation package

## Definition of done for community tasks

A task is done when:

- it preserves the Level A / Level B boundary
- examples are reproducible
- validator behavior is documented
- no wording treats refusal, silence, or non-action as failure
- links in README and docs remain valid
