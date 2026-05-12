from fastapi import FastAPI, Query, Response, status

from .models import HealthResponse, ItemCreate, ItemPatch, ItemReplace, ItemResponse
from .services import ItemService


# ---------------------------------------------------------------------------
# Application factory function
# ---------------------------------------------------------------------------
# create_app() creates and configures the FastAPI application.
# Wrapping everything in a function (instead of writing at module level) makes
# it easy to create separate app instances in tests with different configurations.
# This pattern is called the "Application Factory" pattern.
# ---------------------------------------------------------------------------
def create_app() -> FastAPI:
    # FastAPI() is the main application object.
    # title and version appear in the auto-generated /docs page.
    app = FastAPI(title="T15 FastAPI Practice API", version="1.0.0")

    # One service instance is created here and shared by all routes.
    # Because the service is created inside the function, every call to
    # create_app() gets a fresh service (important in tests).
    service = ItemService()

    # Regex that allows only these three exact values for the 'pricing' query param.
    # FastAPI validates it automatically — invalid values return 422 Unprocessable Entity.
    pricing_pattern = "^(regular|vip|clearance)$"

    # -----------------------------------------------------------------------
    # Health check endpoint
    # -----------------------------------------------------------------------
    # response_model=HealthResponse tells FastAPI:
    #   1. Validate the returned dict against HealthResponse before sending it.
    #   2. Use HealthResponse to generate the schema in /docs.
    # -----------------------------------------------------------------------
    @app.get("/health", response_model=HealthResponse)
    def healthcheck() -> HealthResponse:
        return HealthResponse(status="ok")

    # -----------------------------------------------------------------------
    # Query parameters
    # -----------------------------------------------------------------------
    # 'pricing: str = Query(default="regular", pattern=pricing_pattern)'
    # means: read 'pricing' from the URL query string (?pricing=vip),
    # default to "regular" if not provided, and reject anything that does
    # not match the regex pattern.
    # -----------------------------------------------------------------------
    @app.get("/items", response_model=list[ItemResponse])
    def list_items(pricing: str = Query(default="regular", pattern=pricing_pattern)) -> list[ItemResponse]:
        return service.list_items(pricing)

    @app.get("/items/{item_id}", response_model=ItemResponse)
    def get_item(item_id: int, pricing: str = Query(default="regular", pattern=pricing_pattern)) -> ItemResponse:
        return service.get_item(item_id, pricing)

    # -----------------------------------------------------------------------
    # POST /items — Create a new item
    # -----------------------------------------------------------------------
    # status_code=201: override the default 200 to signal "resource created".
    # Response is injected by FastAPI so we can set response headers manually.
    # The Location header is a REST convention: tell the client where the new
    # resource lives so they can GET it without guessing the URL.
    # payload.model_dump() converts the Pydantic model to a plain dict.
    # -----------------------------------------------------------------------
    @app.post("/items", response_model=ItemResponse, status_code=status.HTTP_201_CREATED)
    def create_item(payload: ItemCreate, response: Response) -> ItemResponse:
        created_item = service.create_item(payload.model_dump())
        response.headers["Location"] = f"/items/{created_item['id']}"
        return created_item

    # -----------------------------------------------------------------------
    # PUT /items/{item_id} — Replace an entire item (all fields required)
    # -----------------------------------------------------------------------
    @app.put("/items/{item_id}", response_model=ItemResponse)
    def replace_item(item_id: int, payload: ItemReplace) -> ItemResponse:
        return service.replace_item(item_id, payload.model_dump())

    # -----------------------------------------------------------------------
    # PATCH /items/{item_id} — Update only the provided fields
    # -----------------------------------------------------------------------
    # exclude_none=True omits fields that were not sent in the request body.
    # Without it, all missing fields would be serialised as None and would
    # overwrite the existing values in the database.
    # -----------------------------------------------------------------------
    @app.patch("/items/{item_id}", response_model=ItemResponse)
    def patch_item(item_id: int, payload: ItemPatch) -> ItemResponse:
        return service.patch_item(item_id, payload.model_dump(exclude_none=True))

    # -----------------------------------------------------------------------
    # DELETE /items/{item_id} — Remove an item
    # -----------------------------------------------------------------------
    # 204 No Content: success response with no body — the standard for DELETE.
    # We return an explicit Response object (not a dict) so FastAPI does not
    # try to serialise a body.
    # -----------------------------------------------------------------------
    @app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
    def delete_item(item_id: int) -> Response:
        service.delete_item(item_id)
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    @app.get("/audit-log", response_model=list[str])
    def get_audit_log() -> list[str]:
        return service.read_audit_log()

    return app


# Module-level 'app' variable is what uvicorn looks for when you run:
#   uvicorn practice_api.app:app
# create_app() is called once at import time.
app = create_app()
