import sqlite3
from pathlib import Path
from threading import Lock


# ---------------------------------------------------------------------------
# Singleton pattern
# ---------------------------------------------------------------------------
# A Singleton ensures that only ONE instance of this class ever exists.
# Why do we need that here?
#   - SQLite supports only one writer at a time.
#   - If every request created its own store object we could end up with
#     multiple objects pointing at the same file and getting confused.
#   - The Singleton guarantees the whole app shares one store object.
#
# How it works:
#   _instance  – class-level variable that holds the single created instance
#                (or None before the first call).
#   _lock      – a threading Lock so that if two threads call __new__ at the
#                same moment, only one of them actually creates the instance.
#
# The "double-checked locking" pattern below:
#   1. First check: cheap, no lock acquired — avoids lock overhead on every call.
#   2. If _instance is None we grab the lock.
#   3. Second check: another thread might have created the instance while we
#      waited for the lock, so we check again before creating.
# ---------------------------------------------------------------------------
class InMemoryStore:
    # Class-level variables shared by all instances (but there will only be one).
    _instance = None
    _lock = Lock()

    def __new__(cls):
        # __new__ is called before __init__ and decides which object to return.
        # Overriding it is the standard Python way to implement Singleton.
        if cls._instance is None:                    # first check (no lock)
            with cls._lock:                          # acquire lock
                if cls._instance is None:            # second check (with lock)
                    instance = super().__new__(cls)
                    # Store the SQLite file path next to this source file.
                    # Path(__file__).resolve() -> absolute path of store.py
                    # .with_name("practice_api.db") -> swap filename, keep dir
                    instance.db_path = Path(__file__).resolve().with_name("practice_api.db")
                    instance._initialize_database()
                    cls._instance = instance
        return cls._instance

    def _connect(self) -> sqlite3.Connection:
        # Opens a fresh connection to the SQLite file on every call.
        # sqlite3.Row makes columns accessible by name: row["price"] not row[2].
        # We open a new connection each time instead of reusing one because
        # a single connection is not thread-safe across requests.
        connection = sqlite3.connect(self.db_path)
        connection.row_factory = sqlite3.Row
        return connection

    def _initialize_database(self) -> None:
        # executescript runs multiple SQL statements separated by semicolons.
        # CREATE TABLE IF NOT EXISTS = safe to call many times; skips if table exists.
        # INTEGER PRIMARY KEY in SQLite is an alias for the internal rowid and
        # must be unique — trying to INSERT a duplicate id raises IntegrityError.
        # tags is stored as TEXT (JSON string) because SQLite has no array type.
        # is_active is stored as INTEGER (0/1) because SQLite has no boolean type.
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
        # The ? placeholder is a parameterised query — never put user data
        # directly into the SQL string (that would be SQL injection).
        with self._connect() as connection:
            connection.execute("INSERT INTO audit_log (event_name) VALUES (?)", (event_name,))

    def read_audit_log(self) -> list[str]:
        with self._connect() as connection:
            rows = connection.execute("SELECT event_name FROM audit_log ORDER BY id").fetchall()
        # List comprehension: iterate over sqlite3.Row objects, pull out the string value.
        return [row["event_name"] for row in rows]

    def reset(self):
        # Used in tests to wipe all data between test runs so tests don't affect each other.
        # DELETE without a WHERE clause removes every row from the table.
        with self._connect() as connection:
            connection.execute("DELETE FROM items")
            connection.execute("DELETE FROM audit_log")
