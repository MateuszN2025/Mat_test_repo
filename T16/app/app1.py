from fastapi import FastAPI, HTTPException

# FastAPI() creates the application object.
# Think of it as the "engine" — you register routes on it.
app1 = FastAPI()

# One hardcoded item stored in a plain Python dict.
# No database, no Pydantic — keep it simple for now.
ITEM = {"id": 1, "name": "Laptop", "price": 999.99}

ITEMS = {
    1: {"id": 1, "name": "Laptop", "price": 999.99},
    2: {"id": 2, "name": "Mouse", "price": 49.99},
}

# @app.get(...) registers a GET route.
# The path parameter {item_id} is captured from the URL.
# FastAPI automatically converts it to int because of the type hint.
# @app1.get(path="/items/{item_id}")
# def get_item(item_id: int):
#     return ITEM

@app1.get("/items/{item_id}")
def get_item(item_id: int):
    item = ITEMS.get(item_id)
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
8.The with patch(...) context manager exits and automatically restores the original ITEMS dict in app.app1.
9.client fixture is torn down (TestClient closed).
10.pytest marks the test as passed and moves to the next one.

Senior insight: step 8 is why patch with yield is preferred over manually saving and restoring values — it is guaranteed to restore even if the test raises an exception.
"""
