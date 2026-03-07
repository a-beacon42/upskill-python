# Curriculum

Use this map to choose the next lesson, prerequisite, or project milestone.

## Python Track

1. Variables, types, conditionals, loops
2. Functions, arguments, return values
3. Lists, dicts, sets, tuples
4. Modules, imports, virtual environments
5. Exceptions and defensive coding
6. Classes, dataclasses, and basic object modeling
7. Type hints and static reasoning
8. File I/O and JSON handling
9. Async fundamentals: coroutines, `await`, event loop mental model
10. Testing with `pytest`

## FastAPI Track

1. ASGI and what FastAPI solves
2. Creating an app and simple routes
3. Path parameters, query parameters, and request bodies
4. Pydantic models for validation and serialization
5. Response models, status codes, and error handling
6. `APIRouter` and modular project layout
7. Dependency injection with `Depends`
8. Settings and configuration
9. Middleware, lifespan, and background tasks
10. Auth, database integration, and test strategy

## Mixed Project Track

Use this sequence for project-based tutoring:

1. Define the API goal in one sentence
2. Sketch the routes and request/response shapes
3. Implement one route end to end
4. Extract models and services
5. Add validation and error handling
6. Add tests
7. Add persistence or external integrations
8. Review architecture and tradeoffs

## Prerequisite Checks

- If the learner struggles with Pydantic models, check Python classes, dicts, and type hints.
- If the learner struggles with `async def`, check coroutine basics before returning to FastAPI.
- If the learner struggles with dependencies, teach plain Python function composition first.
- If the learner struggles with API tests, teach `pytest` assertions and fixtures first.
