## 1. Project Setup

- [x] 1.1 Create project directory structure (`app/` with `main.py`)
- [x] 1.2 Create `requirements.txt` with `fastapi` and `uvicorn` dependencies
- [x] 1.3 Verify FastAPI and Uvicorn can be installed and the app starts

## 2. Data Models

- [x] 2.1 Define `UserCreate` Pydantic model with `name: str` and `age: int`
- [x] 2.2 Define `User` Pydantic model with `id: int`, `name: str`, `age: int`

## 3. In-Memory Data Store

- [x] 3.1 Create module-level `users: list[dict]` variable as the in-memory store
- [x] 3.2 Create module-level `next_id: int` counter starting at 1
- [x] 3.3 Pre-seed the store with 10 users (random names and ages) at module initialization

## 4. CRUD Endpoints

- [x] 4.1 Implement `GET /users` — return all users as JSON array
- [x] 4.2 Implement `GET /users/{id}` — return user by ID or 404 if not found
- [x] 4.3 Implement `POST /users` — accept `UserCreate`, assign auto-incremented ID, store and return HTTP 201 with created user
- [x] 4.4 Implement `PUT /users/{id}` — update existing user's name and age, return 200 or 404
- [x] 4.5 Implement `DELETE /users/{id}` — remove user from store, return 204 or 404

## 5. Validation & Testing

- [x] 5.1 Verify pre-seeded data appears correctly on `GET /users` after startup
- [x] 5.2 Test `POST /users` assigns correct auto-incrementing IDs
- [x] 5.3 Test 404 responses for `GET`, `PUT`, and `DELETE` on non-existent IDs
- [x] 5.4 Confirm `DELETE /users/{id}` returns 204 and user is no longer in list
