#!/usr/bin/env python3
"""Generate module exercise packets for the python-fastapi skill."""

from __future__ import annotations

import argparse
import json
import sys


LEVEL_PROFILES = {
    1: {
        "label": "Foundations",
        "assess_style": "definition and code-reading",
        "build_additions": [
            "Keep the work in one file.",
            "Use direct, explicit control flow.",
        ],
        "debug_additions": [
            "Keep the bug count small and visible.",
        ],
        "refactor_additions": [
            "Focus on naming and removing duplication.",
        ],
    },
    2: {
        "label": "Applied Basics",
        "assess_style": "short reasoning and small code writing",
        "build_additions": [
            "Require one helper function or one extracted router/service boundary.",
            "Include at least one edge-case check.",
        ],
        "debug_additions": [
            "Mix one syntax or validation issue with one logic issue.",
        ],
        "refactor_additions": [
            "Preserve behavior while improving readability and structure.",
        ],
    },
    3: {
        "label": "Intermediate",
        "assess_style": "design choices plus targeted implementation",
        "build_additions": [
            "Require type hints and a cleaner module boundary.",
            "Add a small test or verification step.",
        ],
        "debug_additions": [
            "Include at least one bug tied to architecture or typing.",
        ],
        "refactor_additions": [
            "Improve separation of concerns and testability.",
        ],
    },
    4: {
        "label": "Advanced",
        "assess_style": "tradeoff analysis and realistic code review",
        "build_additions": [
            "Introduce a non-trivial constraint such as performance, concurrency, or API ergonomics.",
            "Require a brief design rationale.",
        ],
        "debug_additions": [
            "Use bugs that expose lifecycle, dependency, or concurrency mistakes.",
        ],
        "refactor_additions": [
            "Target maintainability and performance without changing the public surface.",
        ],
    },
    5: {
        "label": "Expert Challenge",
        "assess_style": "system design and edge-case reasoning",
        "build_additions": [
            "Require explicit tradeoffs and a production-style constraint.",
            "Expect tests or validation strategy, not only implementation.",
        ],
        "debug_additions": [
            "Use subtle bugs that require reasoning across multiple layers.",
        ],
        "refactor_additions": [
            "Target extensibility, observability, and long-term maintainability.",
        ],
    },
}

MODULES = {
    1: {
        "title": "Python syntax, control flow, and functions",
        "assess": [
            "Explain the difference between returning a value and printing a value.",
            "Predict the output of a short function with an `if`/`elif` chain.",
            "Identify when a `for` loop is clearer than repeated `if` statements.",
        ],
        "tiny_task": "Write a function that categorizes a numeric score into named bands.",
        "teach_focus": "function boundaries, branching order, and clear return values",
        "build_goal": "Build a small rules-based function set that transforms raw user input into a summary result.",
        "build_requirements": [
            "Accept multiple inputs and normalize them before applying rules.",
            "Return structured data instead of only printing output.",
            "Handle at least one invalid input case.",
        ],
        "done_criteria": [
            "The main function returns the correct summary for valid input.",
            "Invalid input is handled predictably.",
            "The code is runnable without manual editing.",
        ],
        "debug_behavior": "A scoring function picks the wrong branch for boundary values and mixes printing with return values.",
        "debug_clues": [
            "One condition shadows a later branch.",
            "The caller receives `None` unexpectedly.",
            "Input arrives as text but is compared as if it were already numeric.",
        ],
        "debug_success": [
            "The learner explains each bug and why it appears.",
            "The corrected version returns stable results for edge cases.",
        ],
        "refactor_targets": [
            "Extract repeated branching logic into helper functions.",
            "Rename vague variables and remove nested conditionals where possible.",
        ],
        "refactor_constraints": [
            "Keep the observable behavior the same.",
            "Do not add external dependencies.",
        ],
        "refactor_success": [
            "The flow is easier to read.",
            "Behavior remains unchanged for the provided cases.",
        ],
    },
    2: {
        "title": "Collections, classes, type hints, and exceptions",
        "assess": [
            "Explain when you would use a list of dicts versus a small class or dataclass.",
            "Identify the likely bug in code that mutates a shared default collection.",
            "Describe what a type hint communicates even when Python does not enforce it at runtime.",
        ],
        "tiny_task": "Model a small inventory record and validate one incoming field.",
        "teach_focus": "data modeling, defensive programming, and clear types",
        "build_goal": "Build a small record manager that validates input and stores structured Python objects.",
        "build_requirements": [
            "Represent records with clear fields and type hints.",
            "Reject or normalize invalid data.",
            "Expose at least one lookup or filter operation.",
        ],
        "done_criteria": [
            "Records are stored in a consistent shape.",
            "At least one invalid input path is handled cleanly.",
            "The core operations are easy to follow.",
        ],
        "debug_behavior": "The record manager mutates shared data, accepts invalid shapes, and raises the wrong exception at runtime.",
        "debug_clues": [
            "A default collection is reused between instances.",
            "A field is treated like a number after arriving as text.",
            "Error handling hides the real validation problem.",
        ],
        "debug_success": [
            "The learner identifies the data-model issue and the exception path.",
            "The corrected code preserves valid behavior while rejecting bad inputs.",
        ],
        "refactor_targets": [
            "Improve the model with better types or a dataclass.",
            "Separate validation from storage operations.",
        ],
        "refactor_constraints": [
            "Preserve the public interface.",
            "Keep the solution idiomatic Python.",
        ],
        "refactor_success": [
            "Data flow is clearer.",
            "The validation rules are easier to test.",
        ],
    },
    3: {
        "title": "Testing, modules, and refactoring basics",
        "assess": [
            "Explain what makes a unit test reliable.",
            "Describe why import structure can break tests in a small project.",
            "Identify one smell that suggests a function should be split apart.",
        ],
        "tiny_task": "Write one `pytest` assertion for a small helper function.",
        "teach_focus": "safe change, module boundaries, and meaningful tests",
        "build_goal": "Build a small multi-file Python feature with tests that prove the behavior.",
        "build_requirements": [
            "Split the logic into at least two modules.",
            "Write tests for the happy path and one failure or edge case.",
            "Keep side effects isolated behind a small boundary.",
        ],
        "done_criteria": [
            "The code layout is runnable and understandable.",
            "The tests describe the intended behavior.",
            "The learner can explain why the tests matter.",
        ],
        "debug_behavior": "A small project has failing tests caused by import layout problems and brittle assertions.",
        "debug_clues": [
            "One module reaches too deeply into another module's internals.",
            "A test asserts an exact string when the important behavior is structural.",
            "Imports only work from one working directory.",
        ],
        "debug_success": [
            "The learner fixes both the layout issue and the test design issue.",
            "The learner explains why the new tests are more stable.",
        ],
        "refactor_targets": [
            "Remove duplication across modules.",
            "Improve naming and test readability.",
        ],
        "refactor_constraints": [
            "Keep the same public behavior.",
            "Keep or improve test coverage of important paths.",
        ],
        "refactor_success": [
            "The code is easier to navigate.",
            "The tests remain meaningful after the refactor.",
        ],
    },
    4: {
        "title": "Async Python and data I/O",
        "assess": [
            "Explain what `await` does in plain language.",
            "Identify the problem in async code that performs blocking work directly.",
            "Describe when file or network boundaries should be separated from orchestration logic.",
        ],
        "tiny_task": "Repair a short async function that forgets to await an operation.",
        "teach_focus": "async mental model, non-blocking behavior, and I/O boundaries",
        "build_goal": "Build an async workflow that loads structured data, transforms it, and returns a safe result.",
        "build_requirements": [
            "Use `async` and `await` correctly.",
            "Separate orchestration from raw I/O or parsing work.",
            "Handle at least one failure path.",
        ],
        "done_criteria": [
            "The async flow is correct and understandable.",
            "Blocking or failure-prone work is isolated clearly.",
            "The learner can explain where errors are handled.",
        ],
        "debug_behavior": "An async workflow mixes blocking code, misses an `await`, and leaves cleanup behavior unclear.",
        "debug_clues": [
            "A coroutine object appears where data was expected.",
            "A blocking call sits inside an async function.",
            "Resource cleanup happens only on the happy path.",
        ],
        "debug_success": [
            "The learner explains the async bug and the lifecycle bug.",
            "The fixed version makes the data flow and cleanup explicit.",
        ],
        "refactor_targets": [
            "Separate the async coordinator from parsing or I/O helpers.",
            "Make error handling and cleanup more consistent.",
        ],
        "refactor_constraints": [
            "Keep the same external contract.",
            "Do not remove async behavior just to simplify the code.",
        ],
        "refactor_success": [
            "The concurrency flow is easier to reason about.",
            "The I/O boundaries are clearer and safer.",
        ],
    },
    5: {
        "title": "FastAPI routes, params, request bodies, and validation",
        "assess": [
            "Explain the difference between a path parameter, a query parameter, and a request body.",
            "Describe why a response model is useful even when the route already returns a dict.",
            "Identify the likely cause of a validation error from mismatched field names or types.",
        ],
        "tiny_task": "Write a small FastAPI route signature that accepts one path parameter and one query parameter.",
        "teach_focus": "HTTP shape, FastAPI parameter sources, and Pydantic validation",
        "build_goal": "Build a small FastAPI feature with a couple of endpoints and explicit validation rules.",
        "build_requirements": [
            "Create at least one read endpoint and one write endpoint.",
            "Use request and response models where they help communicate the contract.",
            "Return clear status codes and validation errors.",
        ],
        "done_criteria": [
            "The endpoints are runnable.",
            "The data contract is explicit.",
            "The happy path and one invalid input case are both clear.",
        ],
        "debug_behavior": "A FastAPI route reads data from the wrong parameter source and returns a shape that does not match the declared model.",
        "debug_clues": [
            "One field is declared in the wrong place.",
            "The returned data omits or renames a required field.",
            "The route status code does not match the operation.",
        ],
        "debug_success": [
            "The learner explains the validation failure and fixes the route contract.",
            "The route behavior matches the documented shape after the fix.",
        ],
        "refactor_targets": [
            "Extract router code and schema definitions into cleaner units.",
            "Reduce repeated response or validation logic.",
        ],
        "refactor_constraints": [
            "Preserve the API contract unless the task explicitly allows a change.",
            "Keep the route names and paths stable.",
        ],
        "refactor_success": [
            "The route layer becomes thinner and easier to read.",
            "The schema and validation code are easier to reuse.",
        ],
    },
    6: {
        "title": "FastAPI dependencies, services, persistence, and testing",
        "assess": [
            "Explain what `Depends` solves in a FastAPI app.",
            "Describe why router logic should stay thin when business rules grow.",
            "Identify what makes a service layer easier to test than framework-bound code.",
        ],
        "tiny_task": "Sketch a dependency function that provides a small service object to a route.",
        "teach_focus": "dependency injection, service boundaries, and testable architecture",
        "build_goal": "Build a FastAPI feature that uses dependency injection and a service boundary to manage data or business rules.",
        "build_requirements": [
            "Keep route handlers thin.",
            "Move business rules into a service or repository boundary.",
            "Include at least one test or verification path for the service or API boundary.",
        ],
        "done_criteria": [
            "Dependencies are explicit.",
            "The framework layer and business logic are separated.",
            "The learner can explain how the code would be tested.",
        ],
        "debug_behavior": "A dependency-backed FastAPI feature leaks framework details into the service layer and fails under async or test setup conditions.",
        "debug_clues": [
            "The service depends directly on request objects or globals.",
            "The async dependency is wired incorrectly.",
            "The test setup cannot isolate the business rule from the framework.",
        ],
        "debug_success": [
            "The learner explains the wiring problem and the architecture problem.",
            "The corrected solution is easier to test and reason about.",
        ],
        "refactor_targets": [
            "Separate router, service, and persistence responsibilities more clearly.",
            "Improve typing, naming, and test seams.",
        ],
        "refactor_constraints": [
            "Preserve the behavior and route contract.",
            "Avoid introducing unnecessary abstraction.",
        ],
        "refactor_success": [
            "The architecture is cleaner without becoming overengineered.",
            "The learner can justify each new boundary.",
        ],
    },
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate a tutoring exercise packet.")
    parser.add_argument("--module", type=int, required=True, choices=sorted(MODULES))
    parser.add_argument("--level", type=int, required=True, choices=sorted(LEVEL_PROFILES))
    parser.add_argument(
        "--format",
        choices=("markdown", "json"),
        default="markdown",
        help="Output format.",
    )
    return parser.parse_args()


def build_packet(module_number: int, level: int) -> dict:
    module = MODULES[module_number]
    profile = LEVEL_PROFILES[level]
    assess_questions = module["assess"] + [
        f"Difficulty note: ask in a {profile['assess_style']} style."
    ]
    return {
        "module": module_number,
        "title": module["title"],
        "level": level,
        "level_label": profile["label"],
        "assess": {
            "questions": assess_questions,
            "tiny_task": module["tiny_task"],
        },
        "teach": {
            "focus": module["teach_focus"],
            "example_note": f"Use one concise {module['title'].lower()} example.",
        },
        "build_from_scratch": {
            "goal": module["build_goal"],
            "requirements": module["build_requirements"] + profile["build_additions"],
            "done_criteria": module["done_criteria"],
        },
        "debug": {
            "broken_behavior": module["debug_behavior"],
            "seeded_bug_clues": module["debug_clues"] + profile["debug_additions"],
            "success_criteria": module["debug_success"],
        },
        "refactor": {
            "targets": module["refactor_targets"],
            "constraints": module["refactor_constraints"] + profile["refactor_additions"],
            "success_criteria": module["refactor_success"],
        },
        "review": {
            "prompts": [
                "Summarize strengths first.",
                "Name the main remaining gap.",
                "Recommend the next module or a repeat.",
                "Suggest the next level with a short reason.",
            ]
        },
    }


def render_markdown(packet: dict) -> str:
    lines = [
        "## Module",
        f"Module {packet['module']}: {packet['title']} (Level {packet['level']} - {packet['level_label']})",
        "",
        "## Assess",
    ]
    lines.extend(f"- {question}" for question in packet["assess"]["questions"])
    lines.append(f"- Tiny task: {packet['assess']['tiny_task']}")
    lines.extend(
        [
            "",
            "## Teach",
            f"- Focus: {packet['teach']['focus']}",
            f"- Example note: {packet['teach']['example_note']}",
            "",
            "## Build From Scratch",
            f"- Goal: {packet['build_from_scratch']['goal']}",
            "- Requirements:",
        ]
    )
    lines.extend(f"  - {item}" for item in packet["build_from_scratch"]["requirements"])
    lines.append("- Done criteria:")
    lines.extend(f"  - {item}" for item in packet["build_from_scratch"]["done_criteria"])
    lines.extend(
        [
            "",
            "## Debug",
            f"- Broken behavior: {packet['debug']['broken_behavior']}",
            "- Seeded bug clues:",
        ]
    )
    lines.extend(f"  - {item}" for item in packet["debug"]["seeded_bug_clues"])
    lines.append("- Success criteria:")
    lines.extend(f"  - {item}" for item in packet["debug"]["success_criteria"])
    lines.extend(
        [
            "",
            "## Refactor",
            "- Refactor targets:",
        ]
    )
    lines.extend(f"  - {item}" for item in packet["refactor"]["targets"])
    lines.append("- Constraints:")
    lines.extend(f"  - {item}" for item in packet["refactor"]["constraints"])
    lines.append("- Success criteria:")
    lines.extend(f"  - {item}" for item in packet["refactor"]["success_criteria"])
    lines.extend(
        [
            "",
            "## Review",
        ]
    )
    lines.extend(f"- {item}" for item in packet["review"]["prompts"])
    return "\n".join(lines)


def main() -> int:
    args = parse_args()
    packet = build_packet(args.module, args.level)
    if args.format == "json":
        print(json.dumps(packet, indent=2))
    else:
        print(render_markdown(packet))
    return 0


if __name__ == "__main__":
    sys.exit(main())
