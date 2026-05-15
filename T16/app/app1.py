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

# @app1.post("/items", status_code=status.HTTP_201_CREATED)
# def create_item(payload: dict = Body(...)):
#     # payload: dict = Body(...) tells FastAPI: “read JSON
#     # from the request body into a Python dict”.
#     item = ItemCreate(
#         id=payload["id"],
#         name=payload["name"],
#         price=payload["price"],
#     )
#     items_db[item.id] = item.model_dump()
#     # item.model_dump() [from BaseModel] converts the Pydantic object to a plain dict,
#     # which matches your current items_db structure.
#     return item

@app1.post("/items", status_code=status.HTTP_201_CREATED)
def create_item(payload: ItemCreate):
    if payload.id in items_db:
        raise HTTPException(status_code=409, detail="Item with this id already exists")

    item = payload.model_dump()
    items_db[payload.id] = item
    return item

@app1.patch("/items", status_code=200)      
def update_item_partially(payload: dict = Body(...)):
    # payload: dict = Body(...) tells FastAPI: “read JSON
    # from the request body into a Python dict”.
    
    # items_db: dict[int, dict] = {
    # 1: {"id": 1, "name": "Laptop",  "price": 999.99},
    # 2: {"id": 2, "name": "Monitor", "price": 349.00},
    # }
    
    # list_of_ids = []
    # if payload.get("id") is not None:
    #     for i_dict in items_db.values():
    #         list_of_ids.append(i_dict["id"])
    #     if payload["id"] in list_of_ids:
    #         for i_dict in items_db.values():
    #             if i_dict["id"] == payload["id"]:
    #                 for k in i_dict:
    #                     if payload.get(k) is not None:
    #                         i_dict[k] = payload[k]
    #     else:
    #         raise HTTPException(status_code=400, detail="Bad Request")
    # else:
    #     raise HTTPException(status_code=404, detail="Not Found")
        
    # return i_dict
    

    item_id = payload.get("id")
    if item_id is None:
        raise HTTPException(status_code=400, detail="'id' is required in payload")

    item = items_db.get(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail=f"Item with id={item_id} not found")

    for k in item:
        if payload.get(k) is not None:
            item[k] = payload[k]

    return item

@app1.put("/items", status_code=200)      
def update_item_completely(payload: dict = Body(...)):
    # PUT is treated as full replacement in this handler, so all required
    # fields must be present in the incoming JSON body.
    required_fields = ("id", "name", "price")
    missing_fields = [field for field in required_fields if payload.get(field) is None]

    # Enter validation failure branch when at least one required field is missing.
    if missing_fields:
        # Raise FastAPI HTTPException so the API responds with an explicit client error.
        raise HTTPException(
            # Use 400 because the client sent an incomplete PUT payload.
            status_code=400,
            # Include missing field names to help the caller fix the request quickly.
            detail=f"Incomplete payload. Missing fields: {', '.join(missing_fields)}",
            # Close HTTPException constructor after setting status and detail.
        )

    # Replace the stored record with the full payload.
    items_db[payload["id"]] = payload
    return payload

# Hint: keep this route focused on one delete scenario so status handling stays predictable.
# Registers the DELETE endpoint and declares a 200 success response contract.
# @app1.delete("/items", status_code=200)      
# # Defines the handler and accepts request-body data used to identify the target item.
# def delete_item_completely(payload: dict = Body(...)):
#     item_id = payload.get("id")
#     if item_id is None:
#         raise HTTPException(status_code=400, detail="'id' is required in payload")
#     if not isinstance(item_id, int) or isinstance(item_id, bool):
#         raise HTTPException(status_code=400, detail="'id' must be an integer")

#     # pop performs read+delete in one operation and avoids double dict lookup.
#     deleted_data = items_db.pop(item_id, None)
#     if deleted_data is None:
#         raise HTTPException(status_code=404, detail=f"Item with id={item_id} not found")
#     return deleted_data
    
@app1.delete("/items/{item_id}", status_code=200)      
# Defines the handler and accepts request-body data used to identify the target item.
def delete_item_completely(item_id: int): # ⚠️
    # pop performs read+delete in one operation and avoids double dict lookup.
    # deleted_data = items_db.pop(item_id, None)
    if items_db.get(item_id) is not None:
        deleted_data = items_db[item_id]
        del items_db[item_id]    
        
    else:
        raise HTTPException(status_code=404, detail=f"Item with id={item_id} not found")
    return deleted_data    
    
# status.HTTP_201_CREATED == 201.
# Returning 201 instead of 200 tells the client "resource was created".
# @app1.post("/items", status_code=status.HTTP_201_CREATED)
# def create_item(payload: ItemCreate):
#     if payload.id in items_db:
#         raise HTTPException(status_code=409, detail="Item with this id already exists")
#     # .model_dump() converts the Pydantic model to a plain dict.
#     items_db[payload.id] = payload.model_dump()
#     return items_db[payload.id]  
    
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
