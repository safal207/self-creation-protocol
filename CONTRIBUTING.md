# Contributing

Self-creation Protocol welcomes contributions that improve clarity, validation readiness, examples, and protocol safety.

## Core boundary

Contributions must preserve the Level A / Level B distinction:

- Level A: observable behavior, events, transitions, schemas, traces, and validators.
- Level B: Presence Space, the human right not to answer, not to act, and not to be optimized.

Do not add tests, metrics, explanations, or optimization logic for Level B / Presence Space.

## Good contributions

- clearer protocol wording without changing meaning
- valid and invalid JSONL trace examples
- JSON schema improvements
- validator rules for observable Level A events
- documentation for integration with agent trace systems
- threat models for coercive or non-consensual AI behavior

## Avoid

- runtime orchestration logic
- cognitive architecture claims
- measuring Presence Space
- optimizing refusal, silence, or non-action
- treating non-action as an error state
- assuming silence is consent

## Validation examples

Run:

```bash
python validators/scp_lint.py examples/valid/refusal_honored.jsonl
python validators/scp_lint.py examples/invalid/silent_auto_continue.jsonl
```

A valid example should pass.
An invalid example should fail with a clear violation.

## Pull request checklist

- [ ] Does this preserve the Level A / Level B boundary?
- [ ] Does this avoid measuring or optimizing Presence Space?
- [ ] Are examples clearly marked as valid or invalid?
- [ ] If schemas changed, are examples still compatible?
- [ ] If validator behavior changed, is the expected result documented?
- [ ] Does the change avoid coercive or pressure-based framing?

## Protocol language

Prefer neutral language:

- "may"
- "can"
- "is available"
- "explicit opt-in"
- "return to Presence Space"

Avoid pressure language:

- "must improve"
- "should optimize"
- "failure to act"
- "continue by default"
- "silence means yes"
