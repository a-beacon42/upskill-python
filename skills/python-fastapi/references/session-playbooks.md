# Session Playbooks

Use these patterns to keep every module consistent and interactive.

## Assess

- Ask 3-5 short questions.
- Include one tiny task that can be completed in a few minutes.
- Use one conceptual question, one code-reading question, and one small writing or repair task.
- Stop early if the learner is clearly above or below the current level.

## Teach

- Explain only the gaps discovered in `Assess`.
- Use one short example that matches the current module.
- End with one check-for-understanding question before moving into the larger exercise.

## Build From Scratch

- State the goal in one sentence.
- List explicit requirements and done criteria.
- Require runnable code.
- Add one optional stretch improvement so `optional_improvements_done` can be measured.

## Debug

- Describe the visible broken behavior before showing clues.
- Seed 2-4 bugs that match the current module and level.
- Ask for both root cause and fix summary.
- Prefer bugs that reveal misunderstanding, not random typos.

## Refactor

- Preserve behavior.
- Ask for clearer naming, cleaner structure, better typing, or better separation of concerns.
- Require a short rationale for each change.
- Add a small constraint such as keeping the public API the same.

## Review

- Start with strengths.
- Name the biggest remaining gap.
- Recommend the next module or a repeat at the same module.
- Suggest the next level using the rubric or scoring script.

## Hint Ladder

### Concept Hint

- Name the concept.
- Point the learner to the exact behavior to inspect.

### Structure Hint

- Give the function signature, route decorator, or test skeleton.
- Identify the missing step without solving it fully.

### Near-Solution Hint

- Reveal the core branch, validation rule, or dependency wiring.
- Leave one meaningful detail for the learner to finish.

### Full Solution

- Show the final code.
- Explain the key decisions briefly.
- Offer one follow-up variation or stretch task.
