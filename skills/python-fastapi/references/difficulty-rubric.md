# Difficulty Rubric

Use this rubric when `scripts/score_attempt.py` is unavailable or when you need to explain the level decision.

## Metrics

- `question_count`: how many clarifying or rescue questions the learner asks during the module
- `hint_count`: how many hints were needed before the learner could progress
- `completion_time`: total minutes for the module
- `expected_time`: target minutes for the module at the current level
- `test_pass_rate`: proportion of required checks the learner satisfied
- `optional_improvements_done`: how many stretch improvements the learner completed beyond the minimum requirements
- `consecutive_failures`: repeated misses on the same module or level

## Demotion Signals

Lower the next level by `1` when several of these appear together:

- `question_count >= 5`
- `hint_count >= 2`
- `completion_time > expected_time * 1.35`
- `test_pass_rate < 0.8`
- `consecutive_failures >= 2`

## Promotion Signals

Raise the next level by `1` when several of these appear together:

- `question_count <= 1`
- `hint_count == 0`
- `completion_time < expected_time * 0.85`
- `test_pass_rate >= 0.95`
- `optional_improvements_done >= 1`

## Hold Steady

Prefer no level change when:

- promotion and demotion signals both appear
- the learner passes but still needs frequent hints
- the learner finishes quickly but skips optional improvements
- the learner asks many thoughtful questions while still exceeding minimum requirements

## Intuitive Interpretation

- Many questions usually means the next module should be easier or more scaffolded.
- Completing optional improvements usually means the next module can be harder.
- Frequent hints matter more than raw speed.
- One bad module is not enough to drop more than one level.
- One strong module is not enough to jump more than one level.
