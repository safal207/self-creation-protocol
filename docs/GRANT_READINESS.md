# Grant Readiness

## Project title

**Consent-Aware Guardrails for Autonomous AI Agents**

## One-line summary

Open schemas, trace fixtures, and validators for detecting when AI systems treat silence, refusal, hesitation, or non-action as consent.

## Problem

Autonomous AI agents increasingly decide when to continue, retry, escalate, optimize, or act on behalf of a person.

Current agent frameworks usually log actions and tool calls, but they often do not formally distinguish explicit consent from silence, refusal, hesitation, or deliberate non-action.

This creates a safety gap: an AI system can appear helpful while turning human non-participation into pressure, escalation, or unauthorized optimization.

## Proposed contribution

Self-creation Protocol defines a minimal open protocol layer for consent-aware agent traces.

The project contributes:

- normative guardrails for consent, refusal, non-action, and minimal intervention
- JSON schemas for consent events, protocol violations, and DRP records
- valid and invalid JSONL fixtures for conformance testing
- a lightweight validator for observable Level A traces
- documentation for integration with agent trace and audit systems

## Research question

Can consent-boundary violations in AI-agent behavior be detected from observable traces before the system escalates, pressures, or acts without explicit opt-in?

## Why now

Agentic AI systems are moving from chat responses into action loops: browsing, coding, scheduling, workflow automation, financial operations, coaching, health-adjacent interactions, and personal assistants.

As systems become more autonomous, refusal and non-action must become first-class trace states rather than ambiguous UX moments.

## Scope boundary

The project validates only observable Level A behavior: events, transitions, consent requests, action attempts, and trace records.

It does not inspect, measure, explain, or optimize Presence Space / Level B.

This boundary is essential: the protocol protects the human right not to answer, not to act, and not to be optimized.

## Target funder angles

### Open-source / digital commons

Best fit: NLnet / NGI-style funding.

Framing:

- open protocol for digital autonomy
- anti-dark-pattern guardrails for AI interfaces
- user control and consent infrastructure
- reusable schemas and conformance fixtures

### AI safety

Best fit: Manifund, LTFF, AI safety regranting programs.

Framing:

- agentic oversight
- trace-based safety evaluation
- consent-boundary violation detection
- scalable guardrails for autonomous systems

### Trustworthy AI research

Best fit: larger research calls when combined with trace systems.

Framing:

- formal evaluation of agent behavior
- human consent as a machine-checkable trace property
- integration with LTP/CML-style causal audit layers

## 3-month deliverables

1. Schema stabilization
   - consent-event schema v0.1
   - protocol-violation schema v0.1
   - DRP record schema v0.1

2. Conformance fixtures
   - 10 valid JSONL traces
   - 10 invalid JSONL traces
   - scenario coverage for silence, refusal, unsolicited optimization, minimal resolution, and return to Presence Space

3. Validator improvements
   - CLI support for multiple files
   - structured JSON output
   - violation codes
   - CI workflow for repository fixtures

4. Integration documentation
   - agent trace adapter guide
   - LTP/CML-style audit mapping
   - threat model for coercive AI behavior

## 6-month deliverables

1. Validator v0.2
   - richer rule engine
   - DRP consistency checks
   - semantic/non-semantic trace separation

2. Reference adapters
   - generic agent trace JSONL adapter
   - example mapping for assistant-style action loops

3. Evaluation report
   - violation taxonomy
   - benchmark fixture suite
   - limitations and false-positive analysis

4. Community readiness
   - CONTRIBUTING guide
   - issue templates
   - release notes
   - tagged v0.1 release

## Success metrics

- schemas are stable enough for external review
- fixtures cover common consent-boundary failure modes
- validator flags invalid traces deterministically
- documentation lets a new reviewer understand the project in under 10 minutes
- at least one external agent trace can be mapped into the protocol event format

## Non-goals

- building a full agent runtime
- enforcing behavior inside proprietary systems
- modeling human inner state
- measuring Presence Space
- optimizing refusal or non-action
- replacing legal or medical consent frameworks

## Suggested grant ask

Small prototype grant:

- USD/EUR 10k-30k
- 3-4 months
- deliverable-focused

Larger research grant:

- USD/EUR 50k-150k
- 6-12 months
- only if combined with trace-based oversight, causal memory, and external evaluation

## Short pitch

Self-creation Protocol makes human consent boundaries visible in AI-agent traces. It provides open schemas, examples, and validators for detecting when systems treat silence, refusal, or non-action as permission to continue. The project supports AI safety, digital autonomy, and anti-coercive interface design while preserving a strict boundary: only observable behavior is validated; human Presence Space is never measured or optimized.
