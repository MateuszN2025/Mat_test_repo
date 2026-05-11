import json
import sqlite3

from .store import InMemoryStore


class ItemRepository:
    def __init__(self, store: InMemoryStore):
        self.store = store

    @staticmethod
    def _row_to_item(row) -> dict:
        return {
            "id": row["id"],
            "name": row["name"],
            "price": row["price"],
            "tags": json.loads(row["tags"]),
            "is_active": bool(row["is_active"]),
        }

    def list_items(self) -> list[dict]:
        with self.store._connect() as connection:
            rows = connection.execute("SELECT id, name, price, tags, is_active FROM items ORDER BY id").fetchall()
        return [self._row_to_item(row) for row in rows]

    def get_item(self, item_id: int) -> dict | None:
        with self.store._connect() as connection:
            row = connection.execute(
                "SELECT id, name, price, tags, is_active FROM items WHERE id = ?",
                (item_id,),
            ).fetchone()
        return self._row_to_item(row) if row else None

    def create_item(self, payload: dict) -> dict:
        record = dict(payload)
        try:
            with self.store._connect() as connection:
                connection.execute(
                    "INSERT INTO items (id, name, price, tags, is_active) VALUES (?, ?, ?, ?, ?)",
                    (
                        record["id"],
                        record["name"],
                        record["price"],
                        json.dumps(record["tags"]),
                        int(record["is_active"]),
                    ),
                )
        except sqlite3.IntegrityError as exc:
            raise ValueError(f"Item with id {record['id']} already exists.") from exc

        return self.get_item(record["id"])

    def replace_item(self, item_id: int, payload: dict) -> dict | None:
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
            return None
        return self.get_item(item_id)

    def patch_item(self, item_id: int, changes: dict) -> dict | None:
        current = self.get_item(item_id)
        if current is None:
            return None

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
        return cursor.rowcount > 0


class RepositoryFactory:
    @staticmethod
    def create(kind: str = "memory", store: InMemoryStore | None = None) -> ItemRepository:
        if kind not in {"memory", "sqlite"}:
            raise ValueError("Use 'memory' or 'sqlite' for this exercise repository.")
        return ItemRepository(store or InMemoryStore())
