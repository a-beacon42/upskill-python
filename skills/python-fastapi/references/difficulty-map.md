# Difficulty Map

Use this ladder to set and adjust challenge level.

## Level 1: Foundations

Use for learners who are new to Python or cannot yet read simple code comfortably.

- Focus: variables, control flow, functions, lists/dicts, imports, virtual environments
- FastAPI scope: what an API is, simple `@app.get()` routes, path parameters
- Exercise types: predict output, fill in blanks, fix one-line bugs, write tiny functions
- Signals to stay here: confusion about syntax, indentation, return values, or imports

## Level 2: Applied Basics

Use for learners who know core Python syntax and can write small scripts.

- Focus: classes, exceptions, modules, type hints, list comprehensions, basic testing
- FastAPI scope: query params, request bodies, status codes, response models
- Exercise types: write a helper function, add validation, build a small CRUD endpoint
- Signals to move up: answers are accurate, code is mostly correct, learner asks "why" more than "what"

## Level 3: Intermediate Backend

Use for learners building real services with some confidence.

- Focus: async/await, generators, decorators, packaging, pytest patterns
- FastAPI scope: `APIRouter`, dependencies, Pydantic models, settings, middleware, test clients
- Exercise types: refactor routes, debug validation errors, write endpoint tests, split code into modules
- Signals to move down: async confusion, unclear separation between models/services/routes

## Level 4: Advanced Service Design

Use for learners who can already build and ship small APIs.

- Focus: concurrency tradeoffs, typing strategy, architecture, performance, reliability
- FastAPI scope: lifespan, background tasks, auth, websockets, async DB access, error design
- Exercise types: design reviews, performance debugging, auth flow implementation, architecture tradeoff questions
- Signals to move up: learner anticipates edge cases and explains tradeoffs without prompting

## Level 5: Expert Challenge

Use sparingly. Treat this as mentorship for strong engineers.

- Focus: scaling patterns, framework internals, observability, production hardening
- FastAPI scope: dependency graph design, OpenAPI customization, advanced testing strategy, deployment constraints
- Exercise types: critique architecture, reason about race conditions, optimize a service boundary, design extensible abstractions
- Guardrail: keep problems realistic, not puzzle-like

## Promotion Rules

- Promote one level when the learner succeeds twice in a row without heavy hints.
- Promote when the learner asks for deeper internals, tradeoffs, or design discussion.
- Promote when the learner solves the exercise and explains the reasoning clearly.

## Reduction Rules

- Reduce one level when the learner confuses prerequisites.
- Reduce when the learner cannot start after a conceptual hint.
- Reduce when the learner asks for a simpler explanation.

## Difficulty Knobs

Change difficulty without changing the topic:

- Easier: smaller code, explicit steps, named checkpoints, more examples
- Harder: less scaffolding, missing implementation details, edge cases, testing requirements, performance constraints
