## ADDED Requirements

### Requirement: List all users
The system SHALL provide an endpoint to retrieve all users currently stored in the in-memory data store.

#### Scenario: Retrieve user list
- **WHEN** a client sends GET /users
- **THEN** the system returns HTTP 200 with a JSON array of all user objects (id, name, age)

#### Scenario: List includes pre-seeded users
- **WHEN** the application starts and no additional users have been added
- **THEN** GET /users returns exactly 10 users

### Requirement: Get user by ID
The system SHALL provide an endpoint to retrieve a single user by their unique integer ID.

#### Scenario: Existing user found
- **WHEN** a client sends GET /users/{id} with a valid existing user ID
- **THEN** the system returns HTTP 200 with the user object (id, name, age)

#### Scenario: User not found
- **WHEN** a client sends GET /users/{id} with an ID that does not exist
- **THEN** the system returns HTTP 404 with an error message

### Requirement: Create user
The system SHALL provide an endpoint to add a new user with an auto-assigned ID.

#### Scenario: Successful user creation
- **WHEN** a client sends POST /users with a valid JSON body containing name (string) and age (integer)
- **THEN** the system assigns a new unique integer ID, stores the user, and returns HTTP 201 with the full user object including the assigned ID

#### Scenario: ID auto-increments
- **WHEN** multiple users are created in sequence
- **THEN** each new user receives an ID greater than any previously assigned ID

### Requirement: Update user
The system SHALL provide an endpoint to update an existing user's name and/or age.

#### Scenario: Successful update
- **WHEN** a client sends PUT /users/{id} with a valid JSON body and an existing user ID
- **THEN** the system updates the user's fields and returns HTTP 200 with the updated user object

#### Scenario: Update non-existent user
- **WHEN** a client sends PUT /users/{id} with an ID that does not exist
- **THEN** the system returns HTTP 404 with an error message

### Requirement: Delete user
The system SHALL provide an endpoint to remove a user from the in-memory store by ID.

#### Scenario: Successful deletion
- **WHEN** a client sends DELETE /users/{id} with an existing user ID
- **THEN** the system removes the user and returns HTTP 204 with no body

#### Scenario: Delete non-existent user
- **WHEN** a client sends DELETE /users/{id} with an ID that does not exist
- **THEN** the system returns HTTP 404 with an error message

### Requirement: Pre-seeded data
The system SHALL initialize the in-memory data store with exactly 10 users containing random names and ages on application startup.

#### Scenario: Application startup populates users
- **WHEN** the FastAPI application starts
- **THEN** the in-memory list contains exactly 10 users, each with a unique ID, a non-empty name string, and an integer age
