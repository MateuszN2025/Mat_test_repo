from copy import deepcopy

from .store import InMemoryStore


class ItemRepository:
    def __init__(self, store: InMemoryStore):
        self.store = store

    def list_items(self) -> list[dict]:
        return [deepcopy(item) for item in self.store.items.values()]

    def get_item(self, item_id: int) -> dict | None:
        item = self.store.items.get(item_id)
        return deepcopy(item) if item else None

    def create_item(self, payload: dict) -> dict:
        item_id = self.store.next_id
        self.store.next_id += 1
        record = {"id": item_id, **payload}
        self.store.items[item_id] = record
        return deepcopy(record)

    def replace_item(self, item_id: int, payload: dict) -> dict | None:
        if item_id not in self.store.items:
            return None

        record = {"id": item_id, **payload}
        self.store.items[item_id] = record
        return deepcopy(record)

    def patch_item(self, item_id: int, changes: dict) -> dict | None:
        current = self.store.items.get(item_id)
        if current is None:
            return None

        current.update(changes)
        return deepcopy(current)

    def delete_item(self, item_id: int) -> bool:
        return self.store.items.pop(item_id, None) is not None


class RepositoryFactory:
    @staticmethod
    def create(kind: str = "memory", store: InMemoryStore | None = None) -> ItemRepository:
        if kind != "memory":
            raise ValueError("Only the 'memory' repository is implemented for this exercise.")
        return ItemRepository(store or InMemoryStore())
