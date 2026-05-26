## Context

A simple in-memory REST API is needed for managing users. FastAPI is chosen for its speed, automatic OpenAPI documentation generation, and Pythonic async support. Data is stored in a Python list of dictionaries at runtime — no external database is required. The API is seeded with 10 users (random names and ages) on startup.

## Goals / Non-Goals

**Goals:**
- Implement a FastAPI application with full CRUD for users
- Store users in an in-memory list/dictionary (no database)
- Auto-assign integer IDs on user creation (auto-increment)
- Pre-seed 10 users with random names and ages at startup
- Expose endpoints: GET /users, GET /users/{id}, POST /users, PUT /users/{id}, DELETE /users/{id}

**Non-Goals:**
- Persistent storage (no database, no file-based storage)
- Authentication or authorization
- Pagination or filtering
- Production deployment concerns (Docker, CI/CD, etc.)

## Decisions

### In-memory list as data store
**Decision**: Use a module-level Python list of dicts as the "database".  
**Rationale**: Keeps the implementation simple and self-contained with zero dependencies beyond FastAPI. Suitable for prototyping.  
**Alternatives considered**: SQLite (adds complexity), Pydantic BaseSettings-backed dict (overkill).

### Auto-incrementing ID
**Decision**: Track a module-level counter variable (`next_id`) that increments on each POST.  
**Rationale**: Simple, deterministic, and avoids UUID complexity. IDs from deleted users are not reused.  
**Alternatives considered**: UUID (less readable for simple demos), max(existing ids)+1 (O(n) and fragile on empty list).

### Pydantic models for request/response
**Decision**: Use Pydantic `BaseModel` for `UserCreate` (name, age) and `User` (id, name, age).  
**Rationale**: FastAPI's native validation and automatic schema generation relies on Pydantic models.

## Risks / Trade-offs

- **[Risk] Data loss on restart** → Mitigation: Acceptable for this use case; document that data is ephemeral.
- **[Risk] No concurrency safety** → Mitigation: FastAPI with a single Uvicorn worker is effectively single-threaded for the in-memory state; acceptable for prototype scope.
- **[Risk] IDs not reused after deletion** → Mitigation: Intentional; simpler logic and avoids potential confusion.
