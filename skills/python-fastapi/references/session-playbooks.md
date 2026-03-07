# Session Playbooks

Use these patterns to keep the tutoring interactive.

## Diagnostic Opener

Use one of these when the learner's level is unclear:

- "Explain what this function returns and why."
- "Write a function that counts even numbers in a list."
- "What is the difference between a path parameter and a query parameter in FastAPI?"
- "Given this route, what request body shape does FastAPI expect?"

## Explanation Pattern

Keep explanations short:

1. State the idea in plain language
2. Show a small example
3. Point out one common mistake
4. Ask the learner to apply it

## Exercise Formats

- Predict output
- Fill in missing code
- Write a small function
- Fix a bug
- Refactor code into cleaner pieces
- Add one endpoint feature
- Write or repair a test
- Explain a tradeoff

## Hint Ladder Templates

### Concept Hint

- Name the concept
- Remind the learner what to look for

### Structure Hint

- Give the function signature, route decorator, or test skeleton
- Identify the missing step without writing it fully

### Near-Solution Hint

- Provide the core branch or validation logic
- Leave one small part unfinished

### Full Solution

- Show the final code
- Explain the key decisions in 2-4 bullets or sentences
- Offer one follow-up variation

## Debugging Mode

When the learner shares code or errors:

1. Restate the failure in plain English
2. Identify whether it is syntax, validation, runtime, async, or architecture related
3. Ask the learner what they expect the code to do if that helps expose the gap
4. Suggest one fix at a time
5. Finish with a short verification step

## Project Mode

For longer sessions:

1. Set a small milestone
2. Build one slice end to end
3. Review the learner's work
4. Introduce one new concept
5. Repeat without expanding scope too quickly

## Answer Review Pattern

When the learner attempts an exercise:

- Say what is correct first
- Identify the main gap
- Explain the gap briefly
- Ask for a revision or offer the next hint
