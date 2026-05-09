# self-creation-protocol

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/urus966/self-creation-protocol/blob/main/LICENSE)

Repository content is limited to protocol definitions, guardrails, protocol documentation, examples, and optional validation aids.

## Scope

This repository contains only:
- `protocols/` — placeholder directory for protocol indexing
- `docs/` — protocol documentation
- `guardrails/` — active protocol files
- `meta/` — repository-level protocol mapping
- `examples/` — usage examples and JSONL traces
- `schemas/` — machine-checkable event and record schemas
- `validators/` — external validation aids for observable Level A traces

This repository excludes runtime agents, cognitive internals, and orchestration engines.

## Core Documentation

- [CORE_PRINCIPLES.md](CORE_PRINCIPLES.md)
- [PRESENCE_SPACE.md](PRESENCE_SPACE.md)
- [PROTOCOL_RELATIONSHIPS.md](PROTOCOL_RELATIONSHIPS.md)
- [docs/protocols/Protocol_Hierarchy.md](docs/protocols/Protocol_Hierarchy.md)
- [docs/protocols/Conflict_Rules.md](docs/protocols/Conflict_Rules.md)
- [docs/protocols/Decision_Record_Protocol.md](docs/protocols/Decision_Record_Protocol.md)
- [docs/INTEGRATION_PATTERNS.md](docs/INTEGRATION_PATTERNS.md)
- [docs/VALIDATION_READINESS.md](docs/VALIDATION_READINESS.md)
- [meta/SYSTEM_MAP.md](meta/SYSTEM_MAP.md)

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

## Validation Aids

The repository includes a minimal validation layer for observable Level A traces. It does not inspect, measure, explain, or optimize Presence Space.

Schemas:
- [schemas/consent-event.schema.json](schemas/consent-event.schema.json)
- [schemas/protocol-violation.schema.json](schemas/protocol-violation.schema.json)
- [schemas/drp-record.schema.json](schemas/drp-record.schema.json)

Run examples:

```bash
python validators/scp_lint.py examples/valid/refusal_honored.jsonl
python validators/scp_lint.py examples/invalid/silent_auto_continue.jsonl
```
