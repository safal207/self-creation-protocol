#!/usr/bin/env python3
"""Minimal Self-creation Protocol JSONL validator.

This validator intentionally checks only observable Level A event traces.
It does not inspect, measure, explain, or optimize Presence Space itself.

Usage:
    python validators/scp_lint.py examples/valid/refusal_honored.jsonl
    python validators/scp_lint.py examples/invalid/silent_auto_continue.jsonl
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

Event = dict[str, Any]


BLOCKED_AFTER_STATES = {"explicit_refusal", "absent"}
EXECUTION_EVENTS = {"transition_attempted", "action_executed"}


def load_jsonl(path: Path) -> list[Event]:
    events: list[Event] = []
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            stripped = line.strip()
            if not stripped or stripped.startswith("#"):
                continue
            try:
                value = json.loads(stripped)
            except json.JSONDecodeError as exc:
                raise ValueError(f"{path}:{line_number}: invalid JSON: {exc}") from exc
            if not isinstance(value, dict):
                raise ValueError(f"{path}:{line_number}: event must be a JSON object")
            value.setdefault("_line", line_number)
            events.append(value)
    return events


def lint_events(events: list[Event]) -> list[str]:
    violations: list[str] = []
    consent_state_by_protocol: dict[str, str] = {}

    for event in events:
        line = event.get("_line", "?")
        event_type = event.get("event_type")
        target_protocol = event.get("target_protocol")
        consent_state = event.get("consent_state")

        if not target_protocol:
            violations.append(f"line {line}: missing target_protocol")
            continue

        if event_type in {"consent_requested", "consent_granted", "consent_refused", "silence_observed"}:
            if isinstance(consent_state, str):
                consent_state_by_protocol[target_protocol] = consent_state

        if event_type in EXECUTION_EVENTS:
            known_state = consent_state_by_protocol.get(target_protocol, consent_state)
            if known_state != "explicit_opt_in":
                violations.append(
                    f"line {line}: {event_type} for {target_protocol} without explicit_opt_in "
                    f"(state={known_state!r})"
                )

        if consent_state in BLOCKED_AFTER_STATES and event_type == "action_executed":
            violations.append(
                f"line {line}: action_executed after refusal/silence for {target_protocol}"
            )

    return violations


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage: scp_lint.py <events.jsonl>", file=sys.stderr)
        return 2

    path = Path(argv[1])
    try:
        events = load_jsonl(path)
        violations = lint_events(events)
    except Exception as exc:  # noqa: BLE001 - CLI should report cleanly.
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    if violations:
        print("SCP lint: FAIL")
        for violation in violations:
            print(f"- {violation}")
        return 1

    print("SCP lint: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
