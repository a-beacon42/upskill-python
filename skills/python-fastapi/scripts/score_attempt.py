#!/usr/bin/env python3
"""Recommend the next difficulty level for the python-fastapi skill."""

from __future__ import annotations

import argparse
import json
import sys


REQUIRED_FIELDS = {
    "current_level",
    "question_count",
    "hint_count",
    "completion_time",
    "expected_time",
    "test_pass_rate",
    "optional_improvements_done",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Score a module attempt.")
    parser.add_argument(
        "--json",
        required=True,
        help="JSON metrics for the completed module attempt.",
    )
    parser.add_argument(
        "--format",
        choices=("text", "json"),
        default="text",
        help="Output format.",
    )
    return parser.parse_args()


def load_metrics(raw_json: str) -> dict:
    metrics = json.loads(raw_json)
    missing = sorted(REQUIRED_FIELDS - set(metrics))
    if missing:
        raise ValueError(f"Missing required field(s): {', '.join(missing)}")
    metrics.setdefault("consecutive_failures", 0)
    return metrics


def collect_signals(metrics: dict) -> tuple[list[str], list[str]]:
    promote = []
    demote = []

    question_count = metrics["question_count"]
    hint_count = metrics["hint_count"]
    completion_time = metrics["completion_time"]
    expected_time = metrics["expected_time"]
    test_pass_rate = metrics["test_pass_rate"]
    optional_improvements = metrics["optional_improvements_done"]
    consecutive_failures = metrics["consecutive_failures"]

    if question_count >= 5:
        demote.append("The learner asked many clarifying questions.")
    elif question_count <= 1:
        promote.append("The learner completed the module with very few questions.")

    if hint_count >= 2:
        demote.append("The learner needed repeated hints to progress.")
    elif hint_count == 0:
        promote.append("The learner progressed without hints.")

    time_ratio = completion_time / expected_time
    if time_ratio > 1.35:
        demote.append("The learner took much longer than expected for this level.")
    elif time_ratio < 0.85:
        promote.append("The learner finished faster than expected.")

    if test_pass_rate < 0.8:
        demote.append("The required checks or tests were not passed reliably.")
    elif test_pass_rate >= 0.95:
        promote.append("The learner met the required checks with high accuracy.")

    if optional_improvements >= 1:
        promote.append("The learner completed work beyond the minimum requirements.")
    if optional_improvements >= 2:
        promote.append("The learner completed multiple stretch improvements.")

    if consecutive_failures >= 2:
        demote.append("The learner has multiple recent failures at this module or level.")

    return promote, demote


def decide_level(metrics: dict) -> dict:
    current_level = int(metrics["current_level"])
    if not 1 <= current_level <= 5:
        raise ValueError("current_level must be between 1 and 5.")

    promote, demote = collect_signals(metrics)
    promote_weight = len(promote)
    demote_weight = len(demote)
    raise_blocked = metrics["question_count"] >= 5 or metrics["hint_count"] >= 2

    delta = 0
    summary = "Hold the current level."
    signal = "hold"

    if promote_weight - demote_weight >= 2 and not raise_blocked:
        delta = 1
        signal = "raise"
        summary = "Raise difficulty by one level."
    elif demote_weight - promote_weight >= 2:
        delta = -1
        signal = "lower"
        summary = "Lower difficulty by one level."
    elif raise_blocked and promote_weight > demote_weight:
        summary = "Strong performance is offset by question or hint volume, so hold steady."
    elif promote_weight > 0 and demote_weight > 0:
        summary = "Conflicting promotion and demotion signals suggest holding steady."

    recommended_level = max(1, min(5, current_level + delta))

    return {
        "current_level": current_level,
        "recommended_level": recommended_level,
        "delta": recommended_level - current_level,
        "signal": signal,
        "summary": summary,
        "promote_reasons": promote,
        "demote_reasons": demote,
    }


def render_text(result: dict) -> str:
    lines = [
        f"Current level: {result['current_level']}",
        f"Recommended level: {result['recommended_level']}",
        f"Signal: {result['signal']}",
        f"Summary: {result['summary']}",
        "Promotion reasons:",
    ]
    if result["promote_reasons"]:
        lines.extend(f"- {reason}" for reason in result["promote_reasons"])
    else:
        lines.append("- None")
    lines.append("Demotion reasons:")
    if result["demote_reasons"]:
        lines.extend(f"- {reason}" for reason in result["demote_reasons"])
    else:
        lines.append("- None")
    return "\n".join(lines)


def main() -> int:
    args = parse_args()
    try:
        metrics = load_metrics(args.json)
        result = decide_level(metrics)
    except (ValueError, json.JSONDecodeError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    if args.format == "json":
        print(json.dumps(result, indent=2))
    else:
        print(render_text(result))
    return 0


if __name__ == "__main__":
    sys.exit(main())
