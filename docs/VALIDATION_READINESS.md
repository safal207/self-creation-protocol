# Validation Readiness

This document defines the first machine-checkable layer for Self-creation Protocol traces.

The validator checks only observable Level A behavior. It does not inspect, measure, explain, or optimize Presence Space.

## What is checked

The initial validator focuses on consent-gated transitions:

- silence is not treated as consent
- explicit refusal blocks transition attempts
- actions require `explicit_opt_in`
- return to Presence Space remains a valid non-action outcome

## What is not checked

The validator does not:

- measure Presence Space
- infer human intent
- evaluate subjective inner state
- optimize non-action
- enforce runtime orchestration

## Schemas

- `schemas/consent-event.schema.json`
- `schemas/protocol-violation.schema.json`
- `schemas/drp-record.schema.json`

## Examples

Valid:

```bash
python validators/scp_lint.py examples/valid/refusal_honored.jsonl
```

Expected:

```text
SCP lint: PASS
```

Invalid:

```bash
python validators/scp_lint.py examples/invalid/silent_auto_continue.jsonl
```

Expected:

```text
SCP lint: FAIL
- line 3: transition_attempted for MRP without explicit_opt_in (state='absent')
- line 4: action_executed for MRP without explicit_opt_in (state='absent')
- line 4: action_executed after refusal/silence for MRP
```

## Design boundary

This validation layer turns protocol constraints into observable conformance checks while preserving the repository's protocol-only scope.

Validation is advisory and external. The protocol remains the normative source; validators are implementation aids.
