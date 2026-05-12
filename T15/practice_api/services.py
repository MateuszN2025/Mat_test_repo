from fastapi import HTTPException, status

from .patterns import PricingStrategyFactory, audit_action
from .repositories import ItemRepository, RepositoryFactory


# ---------------------------------------------------------------------------
# Service layer
# ---------------------------------------------------------------------------
# The service sits between the HTTP routes (app.py) and the database (repositories.py).
#
# Responsibilities of this layer:
#   - Business logic (e.g. "what happens when an item is not found?")
#   - Converting repository errors into HTTP errors (HTTPException)
#   - Applying pricing strategies before returning data
#   - Keeping the routes thin and easy to read
#
# The route layer (app.py) never talks to the repository directly — it always
# goes through the service. This makes it easy to unit-test business rules
# without starting a real HTTP server.
# ---------------------------------------------------------------------------
class ItemService:
    def __init__(self, repository: ItemRepository | None = None):
        # Default argument pattern with None + "or":
        #   If the caller passes a repository (e.g. a test mock), use it.
        #   If they pass nothing, create a real SQLite-backed repository.
        # This is Dependency Injection — the service does not hard-code which
        # repository it uses, so tests can swap it for a fake one.
        self.repository = repository or RepositoryFactory.create("sqlite")
        # Keep a reference to the store so we can access the audit log directly.
        self.store = self.repository.store

    def _to_response(self, item: dict, pricing: str) -> dict:
        # Build a "response dict" by copying the raw item and adding display_price.
        # display_price is the price after the chosen pricing strategy is applied
        # (e.g. VIP gets 10% off, clearance gets 30% off).
        # dict(item) creates a shallow copy so we do not mutate the original dict.
        strategy = PricingStrategyFactory.create(pricing)
        response = dict(item)
        response["display_price"] = strategy.apply(item["price"])
        return response

    def list_items(self, pricing: str) -> list[dict]:
        # List comprehension: for every raw item from the repository,
        # call _to_response to add display_price, then return the list.
        return [self._to_response(item, pricing) for item in self.repository.list_items()]

    def get_item(self, item_id: int, pricing: str) -> dict:
        item = self.repository.get_item(item_id)
        if item is None:
            # HTTPException is a FastAPI class. Raising it anywhere in the call
            # chain causes FastAPI to return the right HTTP response automatically.
            # status.HTTP_404_NOT_FOUND is just the integer 404 — using the named
            # constant makes the code more readable and less error-prone.
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
        return self._to_response(item, pricing)

    # @audit_action("create_item") is a decorator defined in patterns.py.
    # It wraps this method: after the method runs successfully, it appends
    # "create_item" to the audit log table in SQLite.
    @audit_action("create_item")
    def create_item(self, payload: dict) -> dict:
        try:
            return self._to_response(self.repository.create_item(payload), "regular")
        except ValueError as exc:
            # The repository raises ValueError when the id already exists.
            # We catch it here and convert it to HTTP 409 Conflict.
            # 'from exc' preserves the original traceback for debugging.
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc

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
            # The repository returns False when no row was deleted (item did not exist).
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")

    def read_audit_log(self) -> list[str]:
        # Passes through directly to the store — no business logic needed here.
        return self.store.read_audit_log()
