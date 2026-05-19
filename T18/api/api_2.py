from fastapi import FastAPI, Body, HTTPException

api_2=FastAPI()

users_db: dict[int, dict] = {
    1: {"id": 1,
        "name": "Bob",
        "age": 43},
    2: {"id": 2,
        "name": "Sam",
        "age": 54}
}

@api_2.get("/items")
def get_data():
    # users = []
    # for user in users_db.values():
    #     users.append(user)    
    return list(users_db.values())

# @api_2.post("/items", status_code=201)
# def post_data(item_id: int, payload: dict):
#     if item_id != payload["id"]:
#         raise HTTPException(status_code=400)
#     # dict tells FastAPI to parse that JSON as a Python dictionary
#     users_db[payload["id"]] = payload
#     return item_id, payload

@api_2.post("/items", status_code=201)
def post_data(payload: dict):
    users_db[payload["id"]] = payload
    return payload