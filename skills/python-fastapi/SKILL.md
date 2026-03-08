---
name: python-fastapi
description: Adaptive tutoring workflow for Python and FastAPI modules with dynamic difficulty levels 1-5. Use when a user asks for guided learning, practice exercises, adaptive coaching, checkpoint assessments, or build/debug/refactor drills for Python and FastAPI topics including syntax/control flow/functions, collections/classes/type hints, testing/debugging/refactoring, async Python/data I/O, FastAPI routing/validation, and dependency-based service architecture.
---

# Python FastAPI

## Overview

Use this skill to run topic-based Python and FastAPI learning modules with adaptive challenge.
Deliver each module using six phases: Assess, Teach, Build From Scratch, Debug, Refactor, and Review.

## Run Workflow

1. Select module and level.
   - Start at level `2` when the user does not provide a level.
   - Recommend the next module in sequence when the user does not provide a module.
   - Let the learner skip ahead if `Assess` is clearly easy for them.

2. Run `Assess`.
   - Ask 3-5 short checkpoint questions.
   - Include one tiny hands-on task.
   - Keep the full phase under 10 minutes.

3. Run `Teach`.
   - Explain only the gaps found in `Assess`.
   - Show one concise module-specific example.
   - Keep the explanation shorter than the exercise work that follows.

4. Run `Build From Scratch`.
   - Generate the exercise packet with `scripts/generate_exercise.py`.
   - Keep requirements explicit and testable.
   - Require runnable code, not pseudocode.

5. Run `Debug`.
   - Present an intentionally broken variant with seeded bugs.
   - Ask for root cause plus fix summary.

6. Run `Refactor`.
   - Preserve behavior while improving readability, architecture, typing, or performance.
   - Require a short rationale for each refactor.

7. Run `Review`.
   - Summarize strengths and gaps.
   - Recommend the next module.
   - Compute the next level using `scripts/score_attempt.py` or follow `references/difficulty-rubric.md`.
   - Prefer holding the level steady when signals conflict.

If the user only wants a quick explanation or a one-off fix, skip to the most relevant phase and still keep the current module and level in mind.

## Module Catalog

1. Python syntax, control flow, and functions
2. Collections, classes, type hints, and exceptions
3. Testing, modules, and refactoring basics
4. Async Python and data I/O
5. FastAPI routes, params, request bodies, and validation
6. FastAPI dependencies, services, persistence, and testing

Use [module-blueprints.md](./references/module-blueprints.md) for per-module outcomes and level-specific task patterns.

## Adaptive Difficulty Policy

Track this data for every module:

- `question_count`
- `hint_count`
- `completion_time`
- `test_pass_rate`
- `optional_improvements_done`
- `expected_time` (minutes for the current module and level)
- `consecutive_failures` (optional, default `0`)

Use `scripts/score_attempt.py` or follow [difficulty-rubric.md](./references/difficulty-rubric.md).

### Scoring command

```bash
python3 scripts/score_attempt.py --json '{
  "current_level": 2,
  "question_count": 4,
  "hint_count": 1,
  "completion_time": 28,
  "expected_time": 35,
  "test_pass_rate": 0.9,
  "optional_improvements_done": 1,
  "consecutive_failures": 0
}'
```

Rules:

- Clamp levels to `1-5`.
- Change by at most `+1` or `-1` per module.
- Prefer no change when promotion and demotion signals conflict.
- Treat `optional_improvements_done` as evidence that the learner went beyond minimum requirements.
- Treat sustained question volume plus hint usage as evidence that the learner needs a simpler next module.

## Exercise Generation

Generate an exercise packet:

```bash
python3 scripts/generate_exercise.py --module 5 --level 2
```

Emit structured output when needed:

```bash
python3 scripts/generate_exercise.py --module 5 --level 2 --format json
```

## Response Format

Use this structure in tutoring responses:

```markdown
## Module
Module <n>: <title> (Level <1-5>)

## Assess
- Q1
- Q2
- Q3
- Tiny task

## Teach
- Gap-focused explanation
- One concrete example

## Build From Scratch
- Goal
- Requirements
- Done criteria

## Debug
- Broken behavior
- Seeded bug clues
- Success criteria

## Refactor
- Refactor targets
- Constraints
- Success criteria

## Review
- Strengths
- Gaps
- Next module recommendation
- Suggested next level
```

## Resources

- `references/module-blueprints.md`: module outcomes and level-specific task patterns.
- `references/difficulty-rubric.md`: thresholds and promotion/demotion policy.
- `references/session-playbooks.md`: phase-specific prompt patterns and review language.
- `scripts/generate_exercise.py`: build/debug/refactor exercise packet generator.
- `scripts/score_attempt.py`: level adjustment calculator.
