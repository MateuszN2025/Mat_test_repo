## Why

There is a need for a simple, lightweight REST API to manage users. FastAPI provides an ideal foundation with automatic documentation, fast performance, and easy development. Using an in-memory list/dictionary as the data store keeps the implementation simple and dependency-free for demonstration and prototyping purposes.

## What Changes

- New FastAPI application with user management endpoints
- In-memory data store (list of user dictionaries) pre-populated with 10 users (random names and ages)
- Auto-incrementing user ID assigned on POST (new user creation)
- CRUD endpoints: list all users, get user by ID, create user, update user, delete user

## Capabilities

### New Capabilities
- `user-management`: REST API endpoints for creating, reading, updating, and deleting users, backed by an in-memory list/dictionary store with auto-assigned IDs and 10 pre-seeded users

### Modified Capabilities

## Impact

- New Python project with FastAPI dependency
- No external database required — data is stored in-memory at runtime
- API exposes user resources with fields: `id`, `name`, `age`
