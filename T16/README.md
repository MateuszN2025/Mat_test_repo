# T16 – Build Your First FastAPI Step by Step

This guide walks you from zero to a small API backed by SQLite.
Each step builds on the previous one. **Do not skip ahead** — the goal is to understand every line before adding the next layer.

When you finish all steps, look back at `T15/practice_api/` — it is the "grown-up" version of what you build here.

---

## Prerequisites

Make sure the virtual environment is active and FastAPI + uvicorn are installed:

```bash
# activate the project venv
source .venv/bin/activate

# install what you need (already in requirements.txt, but just in case)
pip install fastapi uvicorn
```

---

## Step 1 – One endpoint, one hardcoded object

**Goal:** Start the server and hit `GET /items/1` to get back a single item.

Create the file `T16/step1_app.py`:

```python
from fastapi import FastAPI

# FastAPI() creates the application object.
# Think of it as the "engine" — you register routes on it.
app = FastAPI()

# One hardcoded item stored in a plain Python dict.
# No database, no Pydantic — keep it simple for now.
ITEM = {"id": 1, "name": "Laptop", "price": 999.99}


# @app.get(...) registers a GET route.
# The path parameter {item_id} is captured from the URL.
# FastAPI automatically converts it to int because of the type hint.
@app.get("/items/{item_id}")
def get_item(item_id: int):
    return ITEM
```

**Run it:**

```bash
cd T16
uvicorn step1_app:app --reload
```

**Test it in your browser or with curl:**

```bash
curl http://127.0.0.1:8000/items/1
# Expected: {"id": 1, "name": "Laptop", "price": 999.99}
```

Also open `http://127.0.0.1:8000/docs` — FastAPI generates interactive docs for free.

**What to notice:**
- The route returns a plain `dict` — FastAPI serializes it to JSON automatically.
- `item_id: int` in the function signature is all you need for path parameter parsing.
- `--reload` restarts the server on file save; remove it in production.

**Practice task:** Change the item name to something else, save, and see the server reload automatically.

---

## Step 2 – Add a second object and a list endpoint

**Goal:** Store two items in memory, add `GET /items` to return all of them, and add `POST /items` to create a new one.

Create `T16/step2_app.py`:

```python
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI()

# --- Data layer (in-memory, no database yet) ---
# A simple dict acting as our "database".
# Key = item id, Value = item dict.
items_db: dict[int, dict] = {
    1: {"id": 1, "name": "Laptop",  "price": 999.99},
    2: {"id": 2, "name": "Monitor", "price": 349.00},
}


# --- Pydantic model for input validation ---
# Pydantic checks that incoming JSON has the right fields and types.
# Field(gt=0) means "greater than 0" — price must be positive.
class ItemCreate(BaseModel):
    id: int
    name: str = Field(min_length=1)
    price: float = Field(gt=0)


# --- Endpoints ---

@app.get("/items")
def list_items():
    # .values() returns the dict items; list() converts them so FastAPI can serialize.
    return list(items_db.values())


@app.get("/items/{item_id}")
def get_item(item_id: int):
    item = items_db.get(item_id)
    if item is None:
        # HTTPException sends the right HTTP status code + error message.
        raise HTTPException(status_code=404, detail="Item not found")
    return item


# status.HTTP_201_CREATED == 201.
# Returning 201 instead of 200 tells the client "resource was created".
@app.post("/items", status_code=status.HTTP_201_CREATED)
def create_item(payload: ItemCreate):
    if payload.id in items_db:
        raise HTTPException(status_code=409, detail="Item with this id already exists")
    # .model_dump() converts the Pydantic model to a plain dict.
    items_db[payload.id] = payload.model_dump()
    return items_db[payload.id]
```

**Run it:**

```bash
uvicorn step2_app:app --reload
```

**Test it:**

```bash
# Get all items
curl http://127.0.0.1:8000/items

# Get one item
curl http://127.0.0.1:8000/items/1

# Create a new item
curl -X POST http://127.0.0.1:8000/items \
     -H "Content-Type: application/json" \
     -d '{"id": 3, "name": "Keyboard", "price": 79.99}'

# Try to create the same id again — expect 409 Conflict
curl -X POST http://127.0.0.1:8000/items \
     -H "Content-Type: application/json" \
     -d '{"id": 3, "name": "Keyboard", "price": 79.99}'
```

**What to notice:**
- Restarting the server loses all in-memory data — that is why we need a database.
- Pydantic validation errors are returned automatically as `422 Unprocessable Entity` with details — try sending `"price": -5` to see it.

**Practice task:** Add a `DELETE /items/{item_id}` endpoint that removes an item from `items_db` and returns `204 No Content`.

---

## Step 3 – Persist data in SQLite

**Goal:** Replace the in-memory dict with a real SQLite database so data survives server restarts.

Create `T16/step3_app.py`:

```python
import sqlite3
from contextlib import contextmanager
from pathlib import Path

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI()

# Path to the database file, next to this script.
DB_PATH = Path(__file__).parent / "items.db"


# --- Database helpers ---

def get_connection() -> sqlite3.Connection:
    """Open a connection and configure it to return rows as dicts."""
    conn = sqlite3.connect(DB_PATH)
    # row_factory lets you access columns by name: row["name"] instead of row[0]
    conn.row_factory = sqlite3.Row
    return conn


@contextmanager
def db():
    """
    Context manager that opens a connection and commits (or rolls back) automatically.
    'with db() as conn:' is the pattern used throughout the code below.
    """
    conn = get_connection()
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def init_db():
    """Create the items table if it does not exist yet."""
    with db() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS items (
                id    INTEGER PRIMARY KEY,
                name  TEXT    NOT NULL,
                price REAL    NOT NULL
            )
            """
        )


# Call init_db when the module loads so the table is always there.
init_db()


# --- Pydantic models ---

class ItemCreate(BaseModel):
    id: int
    name: str = Field(min_length=1)
    price: float = Field(gt=0)


def row_to_dict(row) -> dict:
    """Convert a sqlite3.Row to a plain Python dict."""
    return {"id": row["id"], "name": row["name"], "price": row["price"]}


# --- Endpoints ---

@app.get("/items")
def list_items():
    with db() as conn:
        rows = conn.execute("SELECT id, name, price FROM items ORDER BY id").fetchall()
    return [row_to_dict(r) for r in rows]


@app.get("/items/{item_id}")
def get_item(item_id: int):
    with db() as conn:
        row = conn.execute(
            "SELECT id, name, price FROM items WHERE id = ?",
            (item_id,),  # Always use ? placeholders — never f-strings with user input!
        ).fetchone()
    if row is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return row_to_dict(row)


@app.post("/items", status_code=status.HTTP_201_CREATED)
def create_item(payload: ItemCreate):
    try:
        with db() as conn:
            conn.execute(
                "INSERT INTO items (id, name, price) VALUES (?, ?, ?)",
                (payload.id, payload.name, payload.price),
            )
    except sqlite3.IntegrityError:
        # PRIMARY KEY violation — the id already exists in the table.
        raise HTTPException(status_code=409, detail="Item with this id already exists")
    return get_item(payload.id)
```

**Run it:**

```bash
uvicorn step3_app:app --reload
```

**Test the persistence:**

```bash
# Add an item
curl -X POST http://127.0.0.1:8000/items \
     -H "Content-Type: application/json" \
     -d '{"id": 1, "name": "Laptop", "price": 999.99}'

# Stop the server (Ctrl+C), restart it, then:
curl http://127.0.0.1:8000/items
# The item is still there — it was saved to items.db
```

**What to notice:**
- The `?` placeholder in SQL is critical for security — it prevents SQL injection.
- `sqlite3.IntegrityError` is raised when the PRIMARY KEY constraint is violated (duplicate id).
- `conn.row_factory = sqlite3.Row` lets you access columns by name like a dict.
- The context manager (`with db() as conn`) guarantees the connection is closed even if an exception is raised.

**Practice task:** Add a `DELETE /items/{item_id}` endpoint. Use `cursor.rowcount` to detect whether the item existed (rowcount == 0 → return 404).

---

## Step 4 – What T15 adds on top of this

Once you are comfortable with Step 3, open `T15/practice_api/` and read the files in this order:

| File | What it adds compared to your Step 3 |
|------|---------------------------------------|
| `store.py` | Wraps the SQLite connection in a Singleton so only one instance is ever created |
| `repositories.py` | Separates SQL queries from business logic — the Repository pattern |
| `services.py` | Business logic layer between the routes and the repository |
| `patterns.py` | Strategy pattern for pricing, Builder pattern for tests, audit log decorator |
| `models.py` | Separate Pydantic models for create / replace / patch / response |
| `app.py` | Thin route layer — just delegates to the service |

The architecture seems complex because every layer has a single responsibility.
In Step 3 you did everything in one file — that is fine for learning, but hard to test and change later.

---

## Checklist before moving to T15

- [ ] Step 1: server starts, `GET /items/1` returns JSON
- [ ] Step 2: `GET /items` returns a list, `POST /items` adds an item, 409 on duplicate
- [ ] Step 3: data survives a server restart, `items.db` file is created on disk
- [ ] Practice task from Step 3: DELETE endpoint with proper 404 handling
