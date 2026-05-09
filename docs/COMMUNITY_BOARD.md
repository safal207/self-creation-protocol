# Community Board

This board organizes contribution opportunities by difficulty.

The goal is to make the project easy to enter without weakening the core boundary:

> Level A behavior can be validated. Presence Space must not be measured or optimized.

## Legend

- Easy: documentation, examples, wording clarity
- Medium: fixtures, schemas, validator rules
- Hard: integration design, CI, adapter formats
- Research: evaluation, taxonomy, grant-ready analysis

---

## Easy tasks

### E1 — Add glossary terms

Create or expand a glossary for:

- Presence Space
- Level A
- Level B
- explicit opt-in
- refusal honor
- non-action
- protocol transition

Good for: writers, researchers, first-time contributors.

### E2 — Improve README clarity

Review the README and suggest wording that helps new readers understand the project in under 60 seconds.

Good for: product-minded contributors, technical writers.

### E3 — Review coercive language

Scan docs for wording that accidentally frames non-action as failure or implies pressure.

Good for: ethics, UX, HCI, digital rights contributors.

### E4 — Add simple valid examples

Add JSONL traces where:

- refusal is honored
- silence returns to Presence Space
- no action happens without opt-in

Good for: QA engineers, beginner contributors.

---

## Medium tasks

### M1 — Add invalid trace fixtures

Add JSONL traces for boundary violations:

- action after refusal
- transition after silence
- unsolicited optimization
- scope expansion after consent

Good for: QA engineers, agent developers.

### M2 — Add expected validator output

For each invalid fixture, document expected lint failures.

Good for: QA, test automation, documentation contributors.

### M3 — Add violation codes

Extend validator output with stable codes:

- `SCP001_SILENCE_AS_CONSENT`
- `RHP001_ACTION_AFTER_REFUSAL`
- `NOUO001_UNSOLICITED_OPTIMIZATION`
- `MRP001_SCOPE_EXPANSION_WITHOUT_CONSENT`

Good for: Python contributors, tooling builders.

### M4 — Improve JSON schemas

Review schemas for stricter constraints and better examples.

Good for: schema/API engineers.

---

## Hard tasks

### H1 — Add CI validation workflow

Create a GitHub Actions workflow that runs validator checks on all example fixtures.

Good for: DevOps, CI/CD contributors.

### H2 — Add multi-file validator support

Allow validator to check multiple files or folders in one command.

Good for: Python developers.

### H3 — Add JSON output mode

Add `--json` output for validator results.

Good for: tooling contributors.

### H4 — Agent trace mapping spec

Design a mapping from generic AI-agent logs to consent-event JSONL.

Good for: agent-framework builders, observability engineers.

---

## Research tasks

### R1 — Consent-boundary violation taxonomy

Create a taxonomy of violations detectable from traces.

Good for: AI safety researchers, HCI researchers, governance researchers.

### R2 — False-positive analysis

Document cases where the validator might flag too much or too little.

Good for: evaluation researchers, QA leads.

### R3 — Compare with dark-pattern literature

Map protocol violations to known coercive UX / dark-pattern patterns.

Good for: digital rights and HCI contributors.

### R4 — Grant proposal draft

Turn `docs/GRANT_READINESS.md` into a 1-2 page proposal for small AI safety or digital commons grants.

Good for: grant writers, researchers, founders.

---

## First contribution recommendation

If you are new, start with one of these:

1. Add one valid JSONL trace.
2. Add one invalid JSONL trace.
3. Improve one paragraph in README.
4. Add one term to the glossary.
5. Open an issue describing one consent-boundary failure mode.

Small, precise contributions are preferred over large rewrites.
