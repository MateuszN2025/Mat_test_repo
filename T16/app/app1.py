from fastapi import FastAPI, HTTPException, status, Body, Response
from pydantic import BaseModel, Field
import json

# FastAPI() creates the application object.
# Think of it as the "engine" — you register routes on it.
app1 = FastAPI()

# One hardcoded item stored in a plain Python dict.
# No database, no Pydantic — keep it simple for now.
ITEM = {"id": 1, "name": "Laptop", "price": 999.99}

# ITEMS = {
#     1: {"id": 1, "name": "Laptop", "price": 999.99},
#     2: {"id": 2, "name": "Mouse", "price": 49.99},
# }

# --- Data layer (in-memory, no database yet) ---
# A simple dict acting as our "database".
# Key = item id, Value = item dict.
items_db: dict[int, dict] = {
    1: {"id": 1, "name": "Laptop",  "price": 999.99},
    2: {"id": 2, "name": "Monitor", "price": 349.00},
}

# @app.get(...) registers a GET route.
# The path parameter {item_id} is captured from the URL.
# FastAPI automatically converts it to int because of the type hint.
# @app1.get(path="/items/{item_id}")
# def get_item(item_id: int):
#     return ITEM



class ItemCreate(BaseModel):
    id: int
    name: str = Field(min_length=1)
    price: float = Field(gt=0)
    
    
# @app1.post("/items/{item_id}", status_code=status.HTTP_201_CREATED)
# def create_item(item_id: int, payload: ItemCreate):
#     item = payload.model_dump()
#     items_db[item_id] = item
#     return item

# @app1.post("/items/{item_id}", status_code=status.HTTP_201_CREATED)
# def create_item(item_id: int, payload: dict = Body(...)):
#     # payload: dict = Body(...) tells FastAPI: “read JSON
#     # from the request body into a Python dict”.
#     item = ItemCreate(
#         id=payload["id"],
#         name=payload["name"],
#         price=payload["price"],
#     )
#     items_db[item_id] = item.model_dump()
#     # item.model_dump() [from BaseModel] converts the Pydantic object to a plain dict,
#     # which matches your current items_db structure.
#     return item

# @app1.post("/items/{item_id}", status_code=201)      
# def create_item(item_id: int, payload: dict = Body(...)):
#     # payload: dict = Body(...) tells FastAPI: “read JSON
#     # from the request body into a Python dict”.
#     items_db[item_id] = payload
#     return payload
    
# status.HTTP_201_CREATED == 201.
# Returning 201 instead of 200 tells the client "resource was created".
@app1.post("/items", status_code=status.HTTP_201_CREATED)
def create_item(payload: ItemCreate):
    if payload.id in items_db:
        raise HTTPException(status_code=409, detail="Item with this id already exists")
    # .model_dump() converts the Pydantic model to a plain dict.
    items_db[payload.id] = payload.model_dump()
    return items_db[payload.id]  
    
# @app1.get("/items")
# def list_items():
#     return items_db #
#     # GET all
#     # {"1":{"id":1,"name":"Laptop","price":999.99},"2":{"id":2,"name":"Monitor","price":349.0}}

@app1.get("/items")
def list_items(pretty: bool = False):
    # Keep default API output as regular JSON objects.
    data = list(items_db.values())
    if pretty:
        return Response(content=json.dumps(data, indent=4), media_type="application/json")
    return data


@app1.get("/items/{item_id}")
def get_item(item_id: int):
    
    item = items_db.get(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


"""
Here is what happens step by step when pytest runs test_get_mocked_item(client, mock_items):

1.pytest collects the test and sees two fixture arguments: client and mock_items.
2.pytest sets up client first — TestClient(app1) is created and held in memory.
3.pytest enters the mock_items fixture and executes code before yield:
    fake_items dict is created with item 99.
    patch("app.app1.ITEMS", fake_items) is called.
    The real ITEMS dict in the app module is temporarily replaced with fake_items.
    The with block is entered, patch is now active.
    
4.yield fake_items pauses the fixture and hands fake_items to the test as the mock_items argument.
5.The test function body runs:
    client.get("/items/99") sends an in-process HTTP request to the app.
    FastAPI calls get_item(item_id=99).
    ITEMS.get(99) looks up key 99 in fake_items (real ITEMS is replaced).
    Returns {"id": 99, "name": "Mocked Item", "price": 0.01}.
    Assertions pass.

6.Test function finishes.
7.Control returns to mock_items fixture after yield.
8.The with patch(...) context manager exits and automatically restores the
original ITEMS dict in app.app1.
9.client fixture is torn down (TestClient closed).
10.pytest marks the test as passed and moves to the next one.

Senior insight: step 8 is why patch with yield is preferred
over manually saving and restoring values — it is guaranteed
to restore even if the test raises an exception.
"""
