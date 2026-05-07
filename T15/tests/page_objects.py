from fastapi.testclient import TestClient


class ItemsApiPage:
    def __init__(self, client: TestClient):
        self.client = client

    def health(self):
        return self.client.get("/health")

    def list_items(self, pricing: str = "regular"):
        return self.client.get("/items", params={"pricing": pricing})

    def get_item(self, item_id: int, pricing: str = "regular"):
        return self.client.get(f"/items/{item_id}", params={"pricing": pricing})

    def create_item(self, payload: dict):
        return self.client.post("/items", json=payload)

    def replace_item(self, item_id: int, payload: dict):
        return self.client.put(f"/items/{item_id}", json=payload)

    def patch_item(self, item_id: int, payload: dict):
        return self.client.patch(f"/items/{item_id}", json=payload)

    def delete_item(self, item_id: int):
        return self.client.delete(f"/items/{item_id}")

    def audit_log(self):
        return self.client.get("/audit-log")
