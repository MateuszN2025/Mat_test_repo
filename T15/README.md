# T15 FastAPI Practice API

This folder contains a small REST API for QA automation practice with FastAPI and pytest.

What matters:
- The API is resource-oriented: `/items` is the collection and `/items/{item_id}` is a single resource.
- All common HTTP methods are covered with REST-style semantics: `GET`, `POST`, `PUT`, `PATCH`, `DELETE`.
- `POST /items` returns `201 Created` and a `Location` header for the new resource.
- The code includes pattern examples you can practice in tests: Singleton, Factory, Strategy, Decorator, Builder, and an API-style Page Object Model.
- Tests use `fastapi.testclient.TestClient`, so you can train API automation without starting a real server.

## Folder guide

This section explains what each important file in `T15` is for, so you can navigate the project faster.

- `T15/__init__.py`: marks `T15` as a Python package so imports like `from T15.practice_api.app import app` work.
- `T15/my_full_api.py`: small runner module that exposes `app` and lets you start the server with `uvicorn`.
- `T15/manual_tests.py`: a tiny manual check using `requests` to call the running API from outside pytest.
- `T15/README.md`: project overview, run instructions, and pattern explanation.
- `T15/practice_api/app.py`: FastAPI entry layer where routes are defined and connected to the service layer.
- `T15/practice_api/models.py`: Pydantic request and response models used for validation and API schema.
- `T15/practice_api/store.py`: singleton in-memory state holder shared by the repository.
- `T15/practice_api/repositories.py`: data-access layer that reads and writes items in the store.
- `T15/practice_api/services.py`: business layer that applies pricing strategy, raises HTTP errors, and records audit actions.
- `T15/practice_api/patterns.py`: design-pattern examples used by the app and the tests.
- `T15/tests/conftest.py`: pytest fixture setup for the test client and clean store state.
- `T15/tests/page_objects.py`: API Page Object Model wrapper around endpoint calls.
- `T15/tests/test_practice_api.py`: focused pytest examples that exercise the REST API and each pattern.

Generated folders such as `__pycache__` are not part of the learning design.

## REST surface

- `GET /items` lists resources.
- `GET /items/{item_id}` reads one resource.
- `POST /items` creates a resource.
- `PUT /items/{item_id}` replaces a resource.
- `PATCH /items/{item_id}` partially updates a resource.
- `DELETE /items/{item_id}` removes a resource.

## Request flow

When a request comes in, the project follows this path:

1. `app.py` receives the HTTP request on a route such as `POST /items`.
2. FastAPI validates the incoming payload using a model from `models.py`.
3. The route function calls `ItemService` from `services.py`.
4. `ItemService` uses `ItemRepository` from `repositories.py`.
5. `ItemRepository` reads or writes the singleton `InMemoryStore` from `store.py`.
6. `ItemService` applies strategy or audit behavior from `patterns.py`.
7. The route returns a response model back through FastAPI.

## Pattern map

- Singleton: `InMemoryStore` keeps one shared store for the app.
- Factory: `RepositoryFactory` and `PricingStrategyFactory` choose the implementation.
- Strategy: pricing modes `regular`, `vip`, `clearance`.
- Decorator: `audit_action` records service actions.
- Builder: `ItemBuilder` prepares request payloads for tests.
- POM: `ItemsApiPage` wraps endpoint calls for pytest tests.

## Objects And Functions

### `practice_api/app.py`

- `create_app() -> FastAPI`: builds and configures the FastAPI application.
- `service = ItemService()`: creates the service object used by all route handlers.
- `healthcheck()`: returns a simple API health response.
- `list_items()`: handles `GET /items` and returns all items, with an optional pricing strategy.
- `get_item()`: handles `GET /items/{item_id}` and returns one item.
- `create_item()`: handles `POST /items`, creates a resource, and sets the `Location` header.
- `replace_item()`: handles `PUT /items/{item_id}` and fully replaces an existing item.
- `patch_item()`: handles `PATCH /items/{item_id}` and partially updates an item.
- `delete_item()`: handles `DELETE /items/{item_id}` and returns `204 No Content`.
- `get_audit_log()`: handles `GET /audit-log` and returns the recorded service actions.
- `app = create_app()`: creates the application instance used by `uvicorn` and by tests.

### `practice_api/models.py`

- `ItemCreate`: input model for creating an item. It validates `name`, `price`, `tags`, and `is_active`.
- `ItemReplace`: same shape as `ItemCreate`, used for full replacement with `PUT`.
- `ItemPatch`: partial-update model for `PATCH`. Every field is optional.
- `ItemResponse`: output model returned by the API. It adds `id` and `display_price`.
- `HealthResponse`: simple model for the `/health` endpoint.

### `practice_api/store.py`

- `InMemoryStore`: singleton object that keeps application state in memory.
- `_instance`: stores the single shared object.
- `_lock`: prevents two threads from creating the singleton at the same time.
- `__new__()`: creates the singleton once and initializes `items`, `audit_log`, and `next_id`.
- `reset()`: clears all in-memory data so tests start from a known state.

### `practice_api/repositories.py`

- `ItemRepository`: thin data-access object around `InMemoryStore`.
- `list_items()`: returns copies of all stored items.
- `get_item(item_id)`: returns one item or `None`.
- `create_item(payload)`: assigns a new id and stores a new item.
- `replace_item(item_id, payload)`: replaces the whole record if it exists.
- `patch_item(item_id, changes)`: updates only the provided fields.
- `delete_item(item_id)`: removes an item and returns `True` or `False`.
- `RepositoryFactory.create()`: factory method that returns a repository implementation. Right now only `memory` is implemented.

### `practice_api/services.py`

- `ItemService`: business layer between the REST routes and the repository.
- `__init__()`: injects a repository or creates one through `RepositoryFactory`.
- `self.audit_log`: points to the shared audit list in the singleton store.
- `_to_response(item, pricing)`: internal helper that applies the selected pricing strategy and builds the API response shape.
- `list_items(pricing)`: returns all items with strategy-based `display_price`.
- `get_item(item_id, pricing)`: returns one item or raises `404`.
- `create_item(payload)`: creates an item and records the action through the decorator.
- `replace_item(item_id, payload)`: full update with `404` handling.
- `patch_item(item_id, changes)`: partial update with `404` handling.
- `delete_item(item_id)`: deletes an item or raises `404`.
- `read_audit_log()`: returns a copy of the recorded actions.

### `practice_api/patterns.py`

- `audit_action(event_name)`: decorator factory. It wraps service methods and appends action names to the audit log.
- `PricingStrategy`: protocol that describes the `apply(price)` method expected from pricing strategies.
- `RegularPricing`: returns the original price rounded to two decimals.
- `VipPricing`: applies a 10% discount.
- `ClearancePricing`: applies a 30% discount.
- `PricingStrategyFactory.create(name)`: chooses which pricing strategy object to build.
- `ItemBuilder`: builder used in tests to create payloads step by step.
- `with_name()`: changes the item name in the builder.
- `with_price()`: changes the price in the builder.
- `with_tags()`: sets the tag list in the builder.
- `inactive()`: marks the item as inactive.
- `build()`: returns the final payload dictionary.

### `tests/conftest.py`

- `PROJECT_ROOT`: helps pytest import the local `T15` package in this workspace layout.
- `api_page()` fixture: creates a fresh `TestClient`, resets the singleton store before and after the test, and returns `ItemsApiPage`.

### `tests/page_objects.py`

- `ItemsApiPage`: Page Object Model wrapper for API calls.
- `health()`: sends `GET /health`.
- `list_items()`: sends `GET /items`.
- `get_item()`: sends `GET /items/{item_id}`.
- `create_item()`: sends `POST /items`.
- `replace_item()`: sends `PUT /items/{item_id}`.
- `patch_item()`: sends `PATCH /items/{item_id}`.
- `delete_item()`: sends `DELETE /items/{item_id}`.
- `audit_log()`: sends `GET /audit-log`.

### `tests/test_practice_api.py`

- `test_healthcheck()`: verifies the API is alive.
- `test_full_crud_flow_uses_builder_and_page_object()`: end-to-end REST flow using the builder and page object.
- `test_singleton_store_is_shared_across_factory_instances()`: proves the singleton store is shared.
- `test_strategy_factory_and_decorator_audit_log()`: verifies the strategy and decorator behavior together.

### `my_full_api.py`

- `app`: imported FastAPI application instance.
- `if __name__ == "__main__":`: local runner block for starting the server directly.

### `manual_tests.py`

- `URL`: target endpoint for a manual check.
- `requests.get(URL)`: simple external client call to the running API.
- `print(response.json())`: prints the response body so you can inspect it manually.

## How to read this project

If the project feels heavy at first, use this order:

1. Start with `practice_api/app.py` to see the endpoints.
2. Read `practice_api/models.py` to understand request and response shapes.
3. Read `practice_api/services.py` to understand the real logic.
4. Read `practice_api/repositories.py` and `practice_api/store.py` to see where data lives.
5. Read `practice_api/patterns.py` to connect each design pattern to a concrete object.
6. Read `tests/page_objects.py` and `tests/test_practice_api.py` to see how pytest uses the API.

## Run locally

Install dependencies:

```bash
source .venv/bin/activate
pip install -r r/requirements.txt
```

Start the API:

```bash
source .venv/bin/activate
python -m uvicorn T15.my_full_api:app --reload
```

Run focused tests:

```bash
source .venv/bin/activate
pytest T15/tests/test_practice_api.py -q
```

## Training ideas

- Add a second repository implementation and extend `RepositoryFactory`.
- Add a new pricing strategy such as `employee` and test it.
- Replace the singleton store with a real database fixture and compare tradeoffs.
