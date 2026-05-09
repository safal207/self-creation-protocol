# Roadmap

## v0.1 — Validation readiness

Status: in progress

Goals:

- define initial JSON schemas
- add valid and invalid JSONL traces
- provide minimal validator for observable Level A behavior
- document protocol-only scope and grant-ready framing

Deliverables:

- `schemas/consent-event.schema.json`
- `schemas/protocol-violation.schema.json`
- `schemas/drp-record.schema.json`
- `validators/scp_lint.py`
- `examples/valid/refusal_honored.jsonl`
- `examples/invalid/silent_auto_continue.jsonl`
- `docs/VALIDATION_READINESS.md`
- `docs/GRANT_READINESS.md`

## v0.2 — Conformance fixtures

Goals:

- expand trace examples
- add violation codes
- support JSON output from validator
- add CI checks for all fixtures

Planned fixture coverage:

- silence is not consent
- refusal honored
- pressure after refusal
- unsolicited optimization
- minimal resolution after opt-in
- return to Presence Space
- protocol transition without consent
- CQMP bounded decision cycle
- DRP record completeness

## v0.3 — Agent trace integration

Goals:

- document mapping from generic agent traces to consent-event traces
- define adapter format for LTP/CML-style audit systems
- add example traces for action loops and tool-use agents

Planned docs:

- `docs/AGENT_TRACE_MAPPING.md`
- `docs/LTP_CML_MAPPING.md`
- `docs/THREAT_MODEL.md`

## v0.4 — Evaluation package

Goals:

- publish a small benchmark of consent-boundary violations
- document limitations, false positives, and unresolved cases
- prepare v0.1 tagged release for external review

Planned outputs:

- conformance report format
- benchmark fixture suite
- evaluation notes
- release checklist

## Long-term direction

Self-creation Protocol should remain a protocol and validation layer, not a runtime agent.

The project may support external implementations, adapters, and validators, but Presence Space must remain outside measurement and optimization.
