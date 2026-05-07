from fastapi import HTTPException, status

from .patterns import PricingStrategyFactory, audit_action
from .repositories import ItemRepository, RepositoryFactory


class ItemService:
    def __init__(self, repository: ItemRepository | None = None):
        self.repository = repository or RepositoryFactory.create("memory")
        self.audit_log = self.repository.store.audit_log

    def _to_response(self, item: dict, pricing: str) -> dict:
        strategy = PricingStrategyFactory.create(pricing)
        response = dict(item)
        response["display_price"] = strategy.apply(item["price"])
        return response

    def list_items(self, pricing: str) -> list[dict]:
        return [self._to_response(item, pricing) for item in self.repository.list_items()]

    def get_item(self, item_id: int, pricing: str) -> dict:
        item = self.repository.get_item(item_id)
        if item is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
        return self._to_response(item, pricing)

    @audit_action("create_item")
    def create_item(self, payload: dict) -> dict:
        return self._to_response(self.repository.create_item(payload), "regular")

    @audit_action("replace_item")
    def replace_item(self, item_id: int, payload: dict) -> dict:
        item = self.repository.replace_item(item_id, payload)
        if item is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
        return self._to_response(item, "regular")

    @audit_action("patch_item")
    def patch_item(self, item_id: int, changes: dict) -> dict:
        item = self.repository.patch_item(item_id, changes)
        if item is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
        return self._to_response(item, "regular")

    @audit_action("delete_item")
    def delete_item(self, item_id: int) -> None:
        deleted = self.repository.delete_item(item_id)
        if not deleted:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")

    def read_audit_log(self) -> list[str]:
        return list(self.audit_log)
