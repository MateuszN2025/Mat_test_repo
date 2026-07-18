# Python, Bash & REST API Testing
## QA Automation Cheat Sheet

---

## 1. HTTP Fundamentals

### HTTP Methods

| Method | Purpose | Has Body | Idempotent | Safe |
|---|---|---|---|---|
| `GET` | Read a resource | No | Yes | Yes |
| `POST` | Create a resource | Yes | No | No |
| `PUT` | Replace a resource fully | Yes | Yes | No |
| `PATCH` | Partially update a resource | Yes | No | No |
| `DELETE` | Remove a resource | No | Yes | No |
| `HEAD` | Like GET but response body omitted | No | Yes | Yes |
| `OPTIONS` | Describe supported methods | No | Yes | Yes |

- **Idempotent:** calling it N times has the same effect as calling it once
- **Safe:** does not modify server state

### HTTP Status Codes

| Range | Meaning | Common codes |
|---|---|---|
| 2xx | Success | 200 OK, 201 Created, 204 No Content |
| 3xx | Redirect | 301 Moved Permanently, 304 Not Modified |
| 4xx | Client error | 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 409 Conflict, 422 Unprocessable Entity, 429 Too Many Requests |
| 5xx | Server error | 500 Internal Server Error, 502 Bad Gateway, 503 Service Unavailable, 504 Gateway Timeout |

### HTTP Headers (most important for QA)

```
# Request headers
Content-Type: application/json          # body format you're sending
Accept: application/json                # format you expect back
Authorization: Bearer <token>           # auth token
X-Request-ID: abc-123                   # tracing (correlate logs)
User-Agent: QA-Bot/1.0

# Response headers
Content-Type: application/json
Location: /api/users/42                 # returned after 201 Created
X-RateLimit-Remaining: 99              # how many calls left
Retry-After: 60                         # seconds to wait after 429
```

### REST Design Conventions

```
GET     /users           → list all users
POST    /users           → create a user
GET     /users/{id}      → get one user
PUT     /users/{id}      → replace user
PATCH   /users/{id}      → partial update
DELETE  /users/{id}      → delete user

GET     /users/{id}/orders   → nested resource
POST    /users/{id}/orders   → create order for user
```

---

## 2. Bash for API Testing

### curl — the essential tool

```bash
# GET request
curl -s https://api.example.com/users

# GET with pretty-print (requires jq)
curl -s https://api.example.com/users | jq .

# GET with custom header
curl -s -H "Authorization: Bearer $TOKEN" https://api.example.com/users

# POST with JSON body
curl -s -X POST https://api.example.com/users \
  -H "Content-Type: application/json" \
  -d '{"name": "Alice", "email": "alice@example.com"}'

# PUT (full replace)
curl -s -X PUT https://api.example.com/users/1 \
  -H "Content-Type: application/json" \
  -d '{"name": "Alice Updated", "email": "alice@example.com"}'

# PATCH (partial update)
curl -s -X PATCH https://api.example.com/users/1 \
  -H "Content-Type: application/json" \
  -d '{"email": "newemail@example.com"}'

# DELETE
curl -s -X DELETE https://api.example.com/users/1

# Show response code only
curl -s -o /dev/null -w "%{http_code}" https://api.example.com/users

# Show response code AND body
curl -s -w "\nHTTP_CODE:%{http_code}" https://api.example.com/users

# Follow redirects
curl -s -L https://api.example.com/redirect

# Skip TLS verification (only for local testing)
curl -sk https://localhost:4443/health

# Verbose — shows full request/response headers
curl -v https://api.example.com/users

# Read body from file
curl -s -X POST https://api.example.com/users \
  -H "Content-Type: application/json" \
  -d @payload.json

# Set timeout
curl -s --max-time 10 https://api.example.com/slow-endpoint
```

### jq — parse and filter JSON

```bash
# Pretty print
echo '{"name":"Alice","age":30}' | jq .

# Extract a field
curl -s https://api.example.com/users/1 | jq '.name'

# Extract nested field
curl -s https://api.example.com/users/1 | jq '.address.city'

# Iterate array
curl -s https://api.example.com/users | jq '.[] | .name'

# Filter array by condition
curl -s https://api.example.com/users | jq '[.[] | select(.active == true)]'

# Extract specific fields from array
curl -s https://api.example.com/users | jq '[.[] | {id, name, email}]'

# Count items
curl -s https://api.example.com/users | jq 'length'

# Get first item
curl -s https://api.example.com/users | jq '.[0]'

# Check if field exists
curl -s https://api.example.com/users/1 | jq 'has("email")'

# Create new JSON structure
jq -n --arg name "Alice" --argjson age 30 '{"name": $name, "age": $age}'
```

### Bash API test script pattern

```bash
#!/usr/bin/env bash
set -euo pipefail               # exit on error, unset variable, pipe failure

BASE_URL="https://api.example.com"
TOKEN="${API_TOKEN:?API_TOKEN env var is required}"   # fail fast if not set

# Helper: assert HTTP status code
assert_status() {
  local expected=$1 actual=$2 label=$3
  if [[ "$actual" != "$expected" ]]; then
    echo "FAIL [$label] expected HTTP $expected, got $actual" >&2
    exit 1
  fi
  echo "PASS [$label] HTTP $actual"
}

# Test: GET /users returns 200
status=$(curl -s -o /dev/null -w "%{http_code}" \
  -H "Authorization: Bearer $TOKEN" "$BASE_URL/users")
assert_status 200 "$status" "GET /users"

# Test: POST /users creates a user and returns 201
response=$(curl -s -w "\n%{http_code}" -X POST "$BASE_URL/users" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"name":"TestUser","email":"test@example.com"}')

body=$(echo "$response" | head -n -1)
status=$(echo "$response" | tail -n 1)
assert_status 201 "$status" "POST /users"

# Extract created user ID
user_id=$(echo "$body" | jq -r '.id')
echo "Created user ID: $user_id"

# Test: DELETE the created user
status=$(curl -s -o /dev/null -w "%{http_code}" -X DELETE \
  -H "Authorization: Bearer $TOKEN" "$BASE_URL/users/$user_id")
assert_status 204 "$status" "DELETE /users/$user_id"

echo "All tests passed."
```

---

## 3. Python for API Testing

### requests library — basics

```python
import requests

BASE_URL = "https://api.example.com"
HEADERS = {
    "Authorization": "Bearer my_token",
    "Content-Type": "application/json",
    "Accept": "application/json",
}

# GET
response = requests.get(f"{BASE_URL}/users", headers=HEADERS)
response.raise_for_status()   # raises HTTPError for 4xx/5xx
users = response.json()

# POST
payload = {"name": "Alice", "email": "alice@example.com"}
response = requests.post(f"{BASE_URL}/users", json=payload, headers=HEADERS)
# json= automatically sets Content-Type: application/json and serializes dict

# PUT
response = requests.put(f"{BASE_URL}/users/1", json=payload, headers=HEADERS)

# PATCH
response = requests.patch(
    f"{BASE_URL}/users/1",
    json={"email": "new@example.com"},
    headers=HEADERS
)

# DELETE
response = requests.delete(f"{BASE_URL}/users/1", headers=HEADERS)

# Query parameters
response = requests.get(
    f"{BASE_URL}/users",
    params={"page": 1, "limit": 20, "active": True},  # → ?page=1&limit=20&active=True
    headers=HEADERS
)

# Timeout (always set it — prevents hanging tests)
response = requests.get(f"{BASE_URL}/users", timeout=10)

# Session (reuses TCP connection + shares headers/cookies)
session = requests.Session()
session.headers.update(HEADERS)
session.get(f"{BASE_URL}/users")
session.post(f"{BASE_URL}/users", json=payload)
```

### Response object — what to inspect

```python
response = requests.get(f"{BASE_URL}/users/1")

response.status_code        # 200
response.ok                 # True if status_code < 400
response.json()             # parsed JSON body (dict/list)
response.text               # raw body as string
response.content            # raw body as bytes
response.headers            # dict-like object
response.headers["Content-Type"]
response.elapsed            # timedelta — how long the request took
response.url                # final URL (after redirects)
response.history            # list of redirect responses
```

### API client class — reusable pattern

```python
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


class APIClient:
    """Thin wrapper around requests for QA automation."""

    def __init__(self, base_url: str, token: str, timeout: int = 10):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        })

        # Retry on transient network errors (not on 4xx — those are test failures)
        retry = Retry(total=3, backoff_factor=0.5,
                      status_forcelist=[500, 502, 503, 504])
        adapter = HTTPAdapter(max_retries=retry)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

    def get(self, path: str, **kwargs):
        return self.session.get(f"{self.base_url}{path}",
                                timeout=self.timeout, **kwargs)

    def post(self, path: str, payload: dict, **kwargs):
        return self.session.post(f"{self.base_url}{path}",
                                 json=payload, timeout=self.timeout, **kwargs)

    def put(self, path: str, payload: dict, **kwargs):
        return self.session.put(f"{self.base_url}{path}",
                                json=payload, timeout=self.timeout, **kwargs)

    def patch(self, path: str, payload: dict, **kwargs):
        return self.session.patch(f"{self.base_url}{path}",
                                  json=payload, timeout=self.timeout, **kwargs)

    def delete(self, path: str, **kwargs):
        return self.session.delete(f"{self.base_url}{path}",
                                   timeout=self.timeout, **kwargs)
```

---

## 4. pytest for API Testing

### Project structure

```
tests/
  conftest.py           ← shared fixtures (client, base_url, auth token)
  test_users.py         ← tests for /users endpoint
  test_orders.py        ← tests for /orders endpoint
  helpers/
    assertions.py       ← custom assertion helpers
    schemas.py          ← JSON schema definitions
```

### conftest.py — fixtures

```python
import os
import pytest
from api_client import APIClient   # your wrapper class


@pytest.fixture(scope="session")
def api_client():
    """Single client shared across all tests in the session."""
    token = os.environ["API_TOKEN"]          # never hardcode tokens
    base_url = os.environ.get("BASE_URL", "https://api.example.com")
    return APIClient(base_url=base_url, token=token)


@pytest.fixture
def created_user(api_client):
    """Create a user before a test, delete it after."""
    response = api_client.post("/users", {"name": "Temp", "email": "tmp@test.com"})
    assert response.status_code == 201
    user = response.json()
    yield user                               # hand user data to the test
    api_client.delete(f"/users/{user['id']}")  # teardown: clean up
```

### test_users.py — test examples

```python
import pytest


class TestGetUsers:
    def test_returns_200(self, api_client):
        r = api_client.get("/users")
        assert r.status_code == 200

    def test_returns_list(self, api_client):
        r = api_client.get("/users")
        assert isinstance(r.json(), list)

    def test_items_have_required_fields(self, api_client):
        users = api_client.get("/users").json()
        assert len(users) > 0
        for user in users:
            assert "id" in user
            assert "email" in user


class TestCreateUser:
    def test_returns_201_with_valid_payload(self, api_client):
        payload = {"name": "Alice", "email": "alice_unique@test.com"}
        r = api_client.post("/users", payload)
        assert r.status_code == 201
        # cleanup
        api_client.delete(f"/users/{r.json()['id']}")

    def test_returns_201_location_header(self, api_client):
        r = api_client.post("/users", {"name": "Bob", "email": "bob_unique@test.com"})
        assert r.status_code == 201
        assert "Location" in r.headers            # REST best practice
        api_client.delete(f"/users/{r.json()['id']}")

    @pytest.mark.parametrize("payload,expected_status", [
        ({},                                      400),   # empty body
        ({"name": "NoEmail"},                     422),   # missing required field
        ({"name": "X", "email": "not-an-email"},  422),   # invalid format
    ])
    def test_returns_error_on_invalid_payload(self, api_client, payload, expected_status):
        r = api_client.post("/users", payload)
        assert r.status_code == expected_status

    def test_duplicate_email_returns_409(self, api_client, created_user):
        r = api_client.post("/users", {
            "name": "Duplicate",
            "email": created_user["email"]    # same email as fixture
        })
        assert r.status_code == 409


class TestDeleteUser:
    def test_returns_204(self, api_client, created_user):
        r = api_client.delete(f"/users/{created_user['id']}")
        assert r.status_code == 204

    def test_delete_nonexistent_returns_404(self, api_client):
        r = api_client.delete("/users/99999999")
        assert r.status_code == 404

    def test_delete_is_idempotent_or_404(self, api_client, created_user):
        api_client.delete(f"/users/{created_user['id']}")
        r = api_client.delete(f"/users/{created_user['id']}")
        assert r.status_code in (204, 404)    # both are acceptable
```

### JSON Schema validation

```python
# pip install jsonschema
from jsonschema import validate, ValidationError

USER_SCHEMA = {
    "type": "object",
    "required": ["id", "name", "email", "created_at"],
    "properties": {
        "id":         {"type": "integer"},
        "name":       {"type": "string", "minLength": 1},
        "email":      {"type": "string", "format": "email"},
        "created_at": {"type": "string", "format": "date-time"},
        "active":     {"type": "boolean"},
    },
    "additionalProperties": False    # strict: no unexpected fields
}

def test_user_schema(api_client, created_user):
    r = api_client.get(f"/users/{created_user['id']}")
    assert r.status_code == 200
    try:
        validate(instance=r.json(), schema=USER_SCHEMA)
    except ValidationError as e:
        pytest.fail(f"Schema validation failed: {e.message}")
```

### Mocking with pytest + responses / unittest.mock

```python
# pip install responses
import responses as resp
import requests

@resp.activate
def test_get_users_mocked():
    resp.add(resp.GET, "https://api.example.com/users",
             json=[{"id": 1, "name": "Alice"}], status=200)

    r = requests.get("https://api.example.com/users")
    assert r.status_code == 200
    assert r.json()[0]["name"] == "Alice"
    assert len(resp.calls) == 1              # verify the call was made


# unittest.mock — mock at function level
from unittest.mock import patch, MagicMock

def test_service_calls_api(my_service):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = [{"id": 1}]

    with patch("requests.get", return_value=mock_response) as mock_get:
        result = my_service.get_users()
        mock_get.assert_called_once_with(
            "https://api.example.com/users", timeout=10
        )
    assert result == [{"id": 1}]
```

---

## 5. Authentication in API Tests

### Bearer Token

```python
# In conftest.py — fetch token once per session
@pytest.fixture(scope="session")
def auth_token():
    r = requests.post("https://api.example.com/auth/token", json={
        "client_id": os.environ["CLIENT_ID"],
        "client_secret": os.environ["CLIENT_SECRET"],
    })
    assert r.status_code == 200, f"Auth failed: {r.text}"
    return r.json()["access_token"]
```

### Testing Auth Scenarios

```python
def test_unauthenticated_returns_401(base_url):
    r = requests.get(f"{base_url}/users")   # no Authorization header
    assert r.status_code == 401

def test_invalid_token_returns_401(base_url):
    r = requests.get(f"{base_url}/users",
                     headers={"Authorization": "Bearer invalid_token_xyz"})
    assert r.status_code == 401

def test_expired_token_returns_401(base_url, expired_token):
    r = requests.get(f"{base_url}/users",
                     headers={"Authorization": f"Bearer {expired_token}"})
    assert r.status_code == 401

def test_forbidden_resource_returns_403(base_url, low_privilege_token):
    r = requests.delete(f"{base_url}/admin/users/1",
                        headers={"Authorization": f"Bearer {low_privilege_token}"})
    assert r.status_code == 403    # authenticated but NOT authorized
```

---

## 6. Response Time & Performance Checks

```python
import pytest

RESPONSE_TIME_THRESHOLD_MS = 500

def test_get_users_response_time(api_client):
    r = api_client.get("/users")
    elapsed_ms = r.elapsed.total_seconds() * 1000
    assert elapsed_ms < RESPONSE_TIME_THRESHOLD_MS, \
        f"Response too slow: {elapsed_ms:.0f}ms (threshold: {RESPONSE_TIME_THRESHOLD_MS}ms)"
```

```bash
# Measure with curl
curl -s -o /dev/null -w "DNS: %{time_namelookup}s  Connect: %{time_connect}s  TTFB: %{time_starttransfer}s  Total: %{time_total}s\n" \
  https://api.example.com/users
```

---

## 7. Environment & Configuration

### .env pattern (never commit secrets)

```bash
# .env  (add to .gitignore!)
API_TOKEN=my_secret_token
BASE_URL=https://staging.api.example.com
CLIENT_ID=abc123
CLIENT_SECRET=xyz789
```

```python
# pip install python-dotenv
from dotenv import load_dotenv
import os

load_dotenv()                          # loads .env into os.environ
token = os.environ["API_TOKEN"]        # KeyError if missing — fail fast
base_url = os.environ.get("BASE_URL", "https://api.example.com")  # with default
```

```bash
# Load and run tests
export $(grep -v '^#' .env | xargs)   # bash: export all .env vars
pytest tests/ -v
```

### pytest.ini / pyproject.toml

```ini
# pytest.ini
[pytest]
testpaths = tests
addopts = -v --tb=short
markers =
    smoke: fast critical path tests
    regression: full regression suite
    auth: authentication related tests
```

```bash
# Run only smoke tests
pytest -m smoke

# Run excluding slow tests
pytest -m "not slow"

# Run specific file
pytest tests/test_users.py -v

# Run test by name pattern
pytest -k "test_create or test_delete" -v

# Stop after first failure
pytest -x

# Show 5 slowest tests
pytest --durations=5
```

---

## 8. Common Pitfalls & Senior-Level Insights

### Test Isolation
```python
# BAD — test depends on another test's side effect
def test_delete_user(api_client):
    api_client.delete("/users/1")   # assumes user 1 exists from previous test

# GOOD — test creates its own data
def test_delete_user(api_client, created_user):
    r = api_client.delete(f"/users/{created_user['id']}")
    assert r.status_code == 204
```

### Don't Assert Only Status Code
```python
# WEAK — passes even if response body is garbage
def test_create_user(api_client):
    r = api_client.post("/users", {"name": "Alice", "email": "a@b.com"})
    assert r.status_code == 201

# STRONG — validates structure AND content
def test_create_user(api_client):
    payload = {"name": "Alice", "email": "alice@test.com"}
    r = api_client.post("/users", payload)
    assert r.status_code == 201
    body = r.json()
    assert body["name"] == payload["name"]
    assert body["email"] == payload["email"]
    assert isinstance(body["id"], int)
    assert "created_at" in body
    assert "Location" in r.headers
```

### Retry Logic vs Flakiness
```python
# Retrying a failing assertion hides real bugs — avoid this:
for _ in range(3):
    r = api_client.get("/users/1")
    if r.status_code == 200:
        break

# Better: if the API is eventually consistent, poll with a timeout
import time

def wait_for_user(api_client, user_id, timeout=5):
    deadline = time.time() + timeout
    while time.time() < deadline:
        r = api_client.get(f"/users/{user_id}")
        if r.status_code == 200:
            return r.json()
        time.sleep(0.2)
    pytest.fail(f"User {user_id} not available after {timeout}s")
```

### Useful pytest Patterns

```python
# Mark test as expected to fail (bug not yet fixed)
@pytest.mark.xfail(reason="Bug #1234 — PATCH doesn't validate email format")
def test_patch_invalid_email(api_client, created_user):
    r = api_client.patch(f"/users/{created_user['id']}", {"email": "bad"})
    assert r.status_code == 422

# Skip conditionally
@pytest.mark.skipif(
    os.environ.get("ENV") == "prod",
    reason="Do not run destructive tests in production"
)
def test_delete_all_users(api_client):
    ...

# Parametrize with IDs for readability
@pytest.mark.parametrize("method,path,expected", [
    ("get",    "/users",        200),
    ("get",    "/users/99999",  404),
    ("delete", "/users/99999",  404),
], ids=["list-users", "get-nonexistent", "delete-nonexistent"])
def test_status_codes(api_client, method, path, expected):
    r = getattr(api_client, method)(path)
    assert r.status_code == expected
```

---

## 9. Quick Reference

### curl Flags

| Flag | Meaning |
|---|---|
| `-s` | Silent — no progress bar |
| `-v` | Verbose — show headers |
| `-X METHOD` | Set HTTP method |
| `-H "Key: Val"` | Add request header |
| `-d 'body'` | Request body (string) |
| `-d @file.json` | Request body from file |
| `--json 'body'` | Shorthand: sets body + Content-Type + Accept to JSON (curl ≥ 7.82) |
| `-o /dev/null` | Discard body |
| `-w "%{http_code}"` | Print status code after |
| `-L` | Follow redirects |
| `-k` | Skip TLS verification |
| `--max-time N` | Total timeout in seconds |
| `-u user:pass` | Basic auth |

### Python requests Exceptions

```python
import requests

try:
    r = requests.get("https://api.example.com/users", timeout=5)
    r.raise_for_status()              # raises HTTPError for 4xx/5xx
except requests.exceptions.ConnectionError:
    print("Could not connect to server")
except requests.exceptions.Timeout:
    print("Request timed out")
except requests.exceptions.HTTPError as e:
    print(f"HTTP error: {e.response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")     # catch-all base class
```
