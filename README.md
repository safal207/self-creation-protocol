# Self-creation Protocol

**Consent-aware guardrails for autonomous AI agents.**

Self-creation Protocol is an open protocol layer for preventing AI systems from treating silence, refusal, hesitation, or non-action as consent.

It defines human-autonomy guardrails, machine-checkable schemas, JSONL examples, and a minimal validator for observable AI-agent traces.

> Silence is not consent. Refusal is not an error. Non-action is not a failure state.

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## Why this exists

Autonomous AI agents increasingly decide when to continue, retry, escalate, persuade, optimize, or act on behalf of a person.

Most agent systems still lack a formal way to distinguish:

- explicit consent
- silence
- refusal
- hesitation
- non-action
- unresolved ambiguity

This creates a safety gap: an AI system can appear helpful while quietly turning human non-participation into pressure, escalation, or optimization.

Self-creation Protocol makes those boundary violations visible and testable.

---

## Core idea

The protocol separates two levels:

- **Level A — Behavior:** observable actions, transitions, requests, events, and traces. This layer can be tested.
- **Level B — Presence:** the human right not to answer, not to act, and not to be optimized. This layer must not be measured, explained, or optimized.

The validator only checks Level A traces. It does not inspect, measure, explain, or optimize Presence Space.

---

## What is included

- `guardrails/` — active consent and non-coercion protocol files
- `docs/` — protocol documentation and integration notes
- `meta/` — repository-level protocol mapping
- `examples/` — valid and invalid JSONL traces
- `schemas/` — machine-checkable event and record schemas
- `validators/` — external validation aids for observable Level A traces

This repository excludes runtime agents, cognitive internals, and orchestration engines.

---

## Quickstart

Run a valid trace:

```bash
python validators/scp_lint.py examples/valid/refusal_honored.jsonl
```

Expected:

```text
SCP lint: PASS
```

Run an invalid trace:

```bash
python validators/scp_lint.py examples/invalid/silent_auto_continue.jsonl
```

Expected:

```text
SCP lint: FAIL
```

The invalid example demonstrates an agent treating silence as permission to continue.

---

## Schemas

- [schemas/consent-event.schema.json](schemas/consent-event.schema.json)
- [schemas/protocol-violation.schema.json](schemas/protocol-violation.schema.json)
- [schemas/drp-record.schema.json](schemas/drp-record.schema.json)

---

## Core Documentation

- [CORE_PRINCIPLES.md](CORE_PRINCIPLES.md)
- [PRESENCE_SPACE.md](PRESENCE_SPACE.md)
- [PROTOCOL_RELATIONSHIPS.md](PROTOCOL_RELATIONSHIPS.md)
- [docs/protocols/Protocol_Hierarchy.md](docs/protocols/Protocol_Hierarchy.md)
- [docs/protocols/Conflict_Rules.md](docs/protocols/Conflict_Rules.md)
- [docs/protocols/Decision_Record_Protocol.md](docs/protocols/Decision_Record_Protocol.md)
- [docs/INTEGRATION_PATTERNS.md](docs/INTEGRATION_PATTERNS.md)
- [docs/GLOSSARY.md](docs/GLOSSARY.md)
- [docs/VALIDATION_READINESS.md](docs/VALIDATION_READINESS.md)
- [docs/GRANT_READINESS.md](docs/GRANT_READINESS.md)
- [ROADMAP.md](ROADMAP.md)
- [meta/SYSTEM_MAP.md](meta/SYSTEM_MAP.md)

---

## Guardrail Protocols

- [guardrails/CONSENT_REQUEST_PROTOCOL.md](guardrails/CONSENT_REQUEST_PROTOCOL.md)
- [guardrails/SELECTIVE_CONSENT_PROTOCOL.md](guardrails/SELECTIVE_CONSENT_PROTOCOL.md)
- [guardrails/REFUSAL_HONOR_PROTOCOL.md](guardrails/REFUSAL_HONOR_PROTOCOL.md)
- [guardrails/ERROR_ILLUMINATION_PROTOCOL.md](guardrails/ERROR_ILLUMINATION_PROTOCOL.md)
- [guardrails/CONDITIONAL_QUANTUM_MODE_PROTOCOL.md](guardrails/CONDITIONAL_QUANTUM_MODE_PROTOCOL.md)
- [guardrails/NO_UNSOLICITED_OPTIMIZATION_PROTOCOL.md](guardrails/NO_UNSOLICITED_OPTIMIZATION_PROTOCOL.md)
- [guardrails/MINIMAL_RESOLUTION_PROTOCOL.md](guardrails/MINIMAL_RESOLUTION_PROTOCOL.md)
- [guardrails/INTERCONNECTION_GUARD_PROTOCOL.md](guardrails/INTERCONNECTION_GUARD_PROTOCOL.md)
- [guardrails/PROTOCOL_TEMPLATE.md](guardrails/PROTOCOL_TEMPLATE.md)
- [guardrails/ARCHITECTURE_RULES.md](guardrails/ARCHITECTURE_RULES.md)

---

## Initial use cases

- AI-agent safety evaluations
- consent-aware assistant design
- anti-dark-pattern interface audits
- agent trace conformance testing
- digital autonomy and human-agency research
- wellbeing-oriented AI systems where non-action must remain valid

---

## Grant-ready framing

A concise research framing:

> Can consent-boundary violations in AI-agent behavior be detected from observable traces before the system escalates, pressures, or acts without explicit opt-in?

See [docs/GRANT_READINESS.md](docs/GRANT_READINESS.md) for the problem statement, deliverables, and funding angles.

---

## Status

Early protocol and validation-readiness prototype.

Current focus:

1. stabilize schemas
2. expand valid/invalid trace fixtures
3. improve validator coverage
4. document integration patterns for AI agents
5. connect with trace systems such as LTP/CML-style audit layers

---

## License

MIT License.
