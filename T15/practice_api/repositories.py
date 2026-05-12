import json
import sqlite3

from .store import InMemoryStore


# ---------------------------------------------------------------------------
# Repository pattern
# ---------------------------------------------------------------------------
# The Repository pattern separates "how to talk to the database" from
# "what the business rules are".
#
# Without this pattern everything would be in one big file:
#   route → SQL query → business logic → SQL query → return JSON
#
# With the Repository:
#   route → service (business rules) → repository (SQL only) → store (connection)
#
# Benefit: if you want to swap SQLite for PostgreSQL later, you only rewrite
# this file; the service and routes stay the same.
# ---------------------------------------------------------------------------
class ItemRepository:
    def __init__(self, store: InMemoryStore):
        # The repository does NOT own the database connection.
        # It receives a store object and uses store._connect() to get connections.
        # This is Dependency Injection — easier to replace in tests.
        self.store = store

    @staticmethod
    def _row_to_item(row) -> dict:
        # sqlite3.Row is like a dict but we convert it to a plain dict here
        # so the rest of the code does not depend on sqlite3 types.
        # tags is stored in SQLite as a JSON string, so we decode it back to a list.
        # is_active is stored as 0/1, bool() converts it to True/False.
        return {
            "id": row["id"],
            "name": row["name"],
            "price": row["price"],
            "tags": json.loads(row["tags"]),   # "[\"sale\"]"  →  ["sale"]
            "is_active": bool(row["is_active"]),  # 1 → True, 0 → False
        }

    def list_items(self) -> list[dict]:
        # 'with self.store._connect() as connection' uses the sqlite3 connection
        # as a context manager: it commits on exit and rolls back on exception.
        # fetchall() returns a list of sqlite3.Row objects.
        with self.store._connect() as connection:
            rows = connection.execute("SELECT id, name, price, tags, is_active FROM items ORDER BY id").fetchall()
        return [self._row_to_item(row) for row in rows]

    def get_item(self, item_id: int) -> dict | None:
        # fetchone() returns one sqlite3.Row or None if no row matched.
        # The (item_id,) is a single-element tuple — the trailing comma is required!
        with self.store._connect() as connection:
            row = connection.execute(
                "SELECT id, name, price, tags, is_active FROM items WHERE id = ?",
                (item_id,),
            ).fetchone()
        # Ternary: if row is truthy convert it, otherwise return None.
        return self._row_to_item(row) if row else None

    def create_item(self, payload: dict) -> dict:
        record = dict(payload)  # defensive copy so we do not mutate the caller's dict
        try:
            with self.store._connect() as connection:
                connection.execute(
                    "INSERT INTO items (id, name, price, tags, is_active) VALUES (?, ?, ?, ?, ?)",
                    (
                        record["id"],
                        record["name"],
                        record["price"],
                        json.dumps(record["tags"]),   # list → JSON string for storage
                        int(record["is_active"]),     # True/False → 1/0 for SQLite
                    ),
                )
        except sqlite3.IntegrityError as exc:
            # IntegrityError is raised when the PRIMARY KEY constraint is violated
            # (i.e. we tried to INSERT an id that already exists).
            # We convert it to a plain ValueError so the service layer does not need
            # to import sqlite3 — keeps layers decoupled.
            raise ValueError(f"Item with id {record['id']} already exists.") from exc

        # Re-fetch from DB to return exactly what was stored (not the input dict).
        return self.get_item(record["id"])

    def replace_item(self, item_id: int, payload: dict) -> dict | None:
        # PUT semantics: replace ALL fields of an existing item.
        # cursor.rowcount tells us how many rows the UPDATE actually touched.
        # If rowcount == 0 the item did not exist.
        with self.store._connect() as connection:
            cursor = connection.execute(
                "UPDATE items SET name = ?, price = ?, tags = ?, is_active = ? WHERE id = ?",
                (
                    payload["name"],
                    payload["price"],
                    json.dumps(payload["tags"]),
                    int(payload["is_active"]),
                    item_id,
                ),
            )
        if cursor.rowcount == 0:
            return None  # Signal to the service: item not found
        return self.get_item(item_id)

    def patch_item(self, item_id: int, changes: dict) -> dict | None:
        # PATCH semantics: only update the fields provided; keep the rest.
        # Strategy: load the current item, merge changes into it, then UPDATE all columns.
        # This is simpler than building a dynamic SQL UPDATE with variable columns.
        current = self.get_item(item_id)
        if current is None:
            return None

        # dict.update() overwrites only the keys present in 'changes'.
        # Keys not in 'changes' keep their old values.
        current.update(changes)
        with self.store._connect() as connection:
            connection.execute(
                "UPDATE items SET name = ?, price = ?, tags = ?, is_active = ? WHERE id = ?",
                (
                    current["name"],
                    current["price"],
                    json.dumps(current["tags"]),
                    int(current["is_active"]),
                    item_id,
                ),
            )
        return self.get_item(item_id)

    def delete_item(self, item_id: int) -> bool:
        with self.store._connect() as connection:
            cursor = connection.execute("DELETE FROM items WHERE id = ?", (item_id,))
        # rowcount > 0 means a row was actually deleted (item existed).
        # rowcount == 0 means nothing was deleted (item did not exist).
        return cursor.rowcount > 0


# ---------------------------------------------------------------------------
# Factory pattern
# ---------------------------------------------------------------------------
# The Factory pattern hides the construction details behind a simple method call.
# Instead of:  repo = ItemRepository(InMemoryStore())
# You write:   repo = RepositoryFactory.create("sqlite")
#
# Benefit: if construction becomes more complex later (e.g. reading config,
# choosing between databases) you change it in one place.
# ---------------------------------------------------------------------------
class RepositoryFactory:
    @staticmethod
    def create(kind: str = "memory", store: InMemoryStore | None = None) -> ItemRepository:
        if kind not in {"memory", "sqlite"}:
            raise ValueError("Use 'memory' or 'sqlite' for this exercise repository.")
        # If no store is provided, create a new InMemoryStore (which is a Singleton,
        # so the same instance is always returned regardless of how many times this runs).
        return ItemRepository(store or InMemoryStore())
