import sqlite3
from pathlib import Path
from threading import Lock


class InMemoryStore:
    _instance = None
    _lock = Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    instance = super().__new__(cls)
                    instance.db_path = Path(__file__).resolve().with_name("practice_api.db")
                    instance._initialize_database()
                    cls._instance = instance
        return cls._instance

    def _connect(self) -> sqlite3.Connection:
        connection = sqlite3.connect(self.db_path)
        connection.row_factory = sqlite3.Row
        return connection

    def _initialize_database(self) -> None:
        with self._connect() as connection:
            connection.executescript(
                """
                CREATE TABLE IF NOT EXISTS items (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    price REAL NOT NULL,
                    tags TEXT NOT NULL,
                    is_active INTEGER NOT NULL
                );

                CREATE TABLE IF NOT EXISTS audit_log (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    event_name TEXT NOT NULL
                );
                """
            )

    def append_audit_log(self, event_name: str) -> None:
        with self._connect() as connection:
            connection.execute("INSERT INTO audit_log (event_name) VALUES (?)", (event_name,))

    def read_audit_log(self) -> list[str]:
        with self._connect() as connection:
            rows = connection.execute("SELECT event_name FROM audit_log ORDER BY id").fetchall()
        return [row["event_name"] for row in rows]

    def reset(self):
        with self._connect() as connection:
            connection.execute("DELETE FROM items")
            connection.execute("DELETE FROM audit_log")
