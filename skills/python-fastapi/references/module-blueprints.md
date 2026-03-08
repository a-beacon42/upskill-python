# Module Blueprints

Use these blueprints to choose outcomes and exercise patterns for each module.

## Module 1: Python syntax, control flow, and functions

- Outcomes: read simple Python, write functions, use conditionals and loops, return values correctly
- Build pattern: small utility or command-style function with branching rules
- Debug pattern: wrong branch ordering, missing returns, input conversion mistakes
- Refactor pattern: replace nested conditionals with helper functions and clearer names
- Level notes:
  - L1: single function, small inputs, no imports
  - L3: multiple helpers, type hints, edge-case checks
  - L5: reusable interface, validation strategy, performance tradeoffs

## Module 2: Collections, classes, type hints, and exceptions

- Outcomes: model data with dicts or classes, use type hints, handle invalid inputs
- Build pattern: record manager, parser, or domain object with validation
- Debug pattern: mutable default mistakes, wrong type assumptions, missing exception handling
- Refactor pattern: improve data modeling with dataclasses, types, and smaller methods
- Level notes:
  - L1: lists and dicts only
  - L3: dataclasses, custom exceptions, richer typing
  - L5: tradeoffs between object models, validation layers, and API ergonomics

## Module 3: Testing, modules, and refactoring basics

- Outcomes: split code into modules, write `pytest` tests, isolate side effects, refactor safely
- Build pattern: small library plus tests and one CLI or script entry point
- Debug pattern: failing tests, import layout mistakes, brittle assertions
- Refactor pattern: remove duplication, improve function boundaries, add clearer tests
- Level notes:
  - L1: simple assertions and one test file
  - L3: fixtures, parametrization, module layout decisions
  - L5: design test strategy, contract tests, and refactor sequencing

## Module 4: Async Python and data I/O

- Outcomes: explain `async`/`await`, avoid blocking mistakes, work with JSON/files or async clients
- Build pattern: async task runner, file-to-model pipeline, or service client wrapper
- Debug pattern: forgotten `await`, blocking calls in async code, resource cleanup errors
- Refactor pattern: separate orchestration from I/O, improve error handling and lifecycle management
- Level notes:
  - L1: read async code and fix one obvious misuse
  - L3: coordinate multiple coroutines and structured data flow
  - L5: reason about concurrency tradeoffs, retries, and backpressure

## Module 5: FastAPI routes, params, request bodies, and validation

- Outcomes: create endpoints, validate input with Pydantic, choose status codes, shape responses
- Build pattern: small CRUD or workflow API with two to four endpoints
- Debug pattern: request/response model mismatch, wrong parameter source, validation failures
- Refactor pattern: extract routers and schemas, reduce repeated response logic
- Level notes:
  - L1: one GET and one POST endpoint
  - L3: `APIRouter`, response models, error handling
  - L5: API design tradeoffs, pagination, filtering, and schema evolution

## Module 6: FastAPI dependencies, services, persistence, and testing

- Outcomes: use `Depends`, separate router/service/repository layers, test the service boundary
- Build pattern: service-backed API with settings or persistence abstraction
- Debug pattern: dependency wiring bugs, async test setup issues, leaking framework concerns into domain logic
- Refactor pattern: preserve behavior while improving separation of concerns, typing, and testability
- Level notes:
  - L1: simple dependency function and one service object
  - L3: service/repository split with tests and settings
  - L5: authentication, lifecycle, performance, and maintainability tradeoffs
