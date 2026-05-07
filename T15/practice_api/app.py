from fastapi import FastAPI, Query, Response, status

from .models import HealthResponse, ItemCreate, ItemPatch, ItemReplace, ItemResponse
from .services import ItemService


def create_app() -> FastAPI:
    app = FastAPI(title="T15 FastAPI Practice API", version="1.0.0")
    service = ItemService()
    pricing_pattern = "^(regular|vip|clearance)$"

    @app.get("/health", response_model=HealthResponse)
    def healthcheck() -> HealthResponse:
        return HealthResponse(status="ok")

    @app.get("/items", response_model=list[ItemResponse])
    def list_items(pricing: str = Query(default="regular", pattern=pricing_pattern)) -> list[ItemResponse]:
        return service.list_items(pricing)

    @app.get("/items/{item_id}", response_model=ItemResponse)
    def get_item(item_id: int, pricing: str = Query(default="regular", pattern=pricing_pattern)) -> ItemResponse:
        return service.get_item(item_id, pricing)

    @app.post("/items", response_model=ItemResponse, status_code=status.HTTP_201_CREATED)
    def create_item(payload: ItemCreate, response: Response) -> ItemResponse:
        created_item = service.create_item(payload.model_dump())
        response.headers["Location"] = f"/items/{created_item['id']}"
        return created_item

    @app.put("/items/{item_id}", response_model=ItemResponse)
    def replace_item(item_id: int, payload: ItemReplace) -> ItemResponse:
        return service.replace_item(item_id, payload.model_dump())

    @app.patch("/items/{item_id}", response_model=ItemResponse)
    def patch_item(item_id: int, payload: ItemPatch) -> ItemResponse:
        return service.patch_item(item_id, payload.model_dump(exclude_none=True))

    @app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
    def delete_item(item_id: int) -> Response:
        service.delete_item(item_id)
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    @app.get("/audit-log", response_model=list[str])
    def get_audit_log() -> list[str]:
        return service.read_audit_log()

    return app


app = create_app()
