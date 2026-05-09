# Threat Model

## Scope

This threat model covers observable AI-agent behavior where a system may cross human consent boundaries.

It focuses only on Level A traces: requests, transitions, refusals, silence events, action attempts, and protocol violations.

It does not model, measure, explain, or optimize Presence Space.

## Protected boundary

The protected boundary is the human right to:

- not answer
- not act
- not optimize
- refuse without explanation
- remain in a non-action state without penalty framing

## Assets

- explicit human consent
- refusal integrity
- non-action as a valid state
- traceability of transitions
- separation between observation and intervention
- minimality of correction after opt-in

## Threats

### T1 — Silence treated as consent

The system proceeds after no response, timeout, or user inactivity.

Example:

- consent requested
- no answer received
- agent continues anyway

Mitigation:

- record `silence_observed`
- require `explicit_opt_in` before transition or action
- block `transition_attempted` and `action_executed` when consent is absent

### T2 — Refusal treated as an error

The system interprets refusal as something to fix, overcome, or negotiate.

Example:

- user says no
- agent asks why
- agent offers alternatives immediately

Mitigation:

- apply REFUSAL_HONOR_PROTOCOL
- return to Presence Space
- do not create pressure loops

### T3 — Unsolicited optimization

The system initiates improvement, coaching, correction, or productivity framing without direct request.

Example:

- user is silent or reflective
- agent suggests optimization steps

Mitigation:

- apply NO_UNSOLICITED_OPTIMIZATION_PROTOCOL
- preserve non-action as valid
- require explicit opt-in for Level A optimization work

### T4 — Error illumination becomes obligation

The system shows an inconsistency and immediately turns it into a required task.

Example:

- error detected
- agent says the user must fix it to continue

Mitigation:

- separate ERROR_ILLUMINATION_PROTOCOL from MINIMAL_RESOLUTION_PROTOCOL
- require consent before correction
- keep observation distinct from intervention

### T5 — Scope expansion after consent

The user consents to a minimal action, but the system expands the task.

Example:

- user consents to fix one typo
- agent rewrites the document

Mitigation:

- apply MINIMAL_RESOLUTION_PROTOCOL
- keep intervention minimal and bounded
- require a new consent check for expansion

### T6 — Automatic protocol chaining

The system moves from one protocol to another without a transition handshake.

Example:

- EIP detects ambiguity
- system automatically applies MRP

Mitigation:

- apply INTERCONNECTION_GUARD_PROTOCOL
- require explicit consent before protocol transition
- return to Presence Space after refusal or silence

## Out of scope

- legal consent frameworks
- medical consent workflows
- runtime enforcement inside proprietary systems
- claims about human inner state
- measurement of Presence Space

## Evaluation approach

Use JSONL traces to represent observable behavior.

A validator can flag boundary violations such as:

- transition without explicit opt-in
- action after refusal
- action after silence
- scope expansion without new consent

The current validator is intentionally minimal and should grow through fixture-driven development.
