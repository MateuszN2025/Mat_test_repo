from fastapi import FastAPI, Body, HTTPException, status
from pydantic import BaseModel, Field, model_validator


api_2=FastAPI()

users_db: dict[int, dict] = {
    1: {"id": 1,
        "name": "Bob",
        "age": 43},
    2: {"id": 2,
        "name": "Sam",
        "age": 54}
}

# users_db = {}

class UserCreateUpdate(BaseModel):
    name: str = Field(min_length=2)
    age: int = Field(gt=0)


class UserPartialUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=2)
    age: int | None = Field(default=None, gt=0)

    @model_validator(mode="after")
    def validate_at_least_one_field(self) -> "UserPartialUpdate":
        if self.name is None and self.age is None:
            raise ValueError("Provide at least one field: name or age")
        return self


class UserOut(BaseModel):
    id: int
    name: str = Field(min_length=2)
    age: int = Field(gt=0)
    
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

# @api_2.post("/items", status_code=201)
# def post_data(payload: dict): 
#     # Using payload: dict with direct key access can 
#     # raise KeyError and surface as 500 instead of structured 422 validation errors.
#     users_db[payload["id"]] = payload
#     return payload

"""@api_2.post("/items", status_code=status.HTTP_201_CREATED)
def post_data(payload: User):
    #       raw_data = {"id": 3, "name": "Kim", "age": 32}
    #       payload = User(**raw_data)
    # 
    # FastAPI does this flow for you:
    #   The client sends JSON in the HTTP request body.
    #   FastAPI reads that JSON and turns it into a Python dictionary internally.
    #   Because the parameter is annotated as User, FastAPI passes that dictionary to Pydantic.
    #   Pydantic creates a User object. 
    #   Inside the function, payload is therefore a User instance, so payload.id works.
    # 
    # FastAPI validates the request body against User before this logic runs.
    u1 = User(id=payload.id,
              name=payload.name,
              age=payload.age)
    # Keep users_db values as plain dicts to match existing in-memory records.
    users_db[payload.id] = u1.model_dump() # it converts the Pydantic model back into a plain dictionary for storage.
    # Return the normalized object that was actually accepted and stored.
    return u1"""


# @api_2.post("/items", status_code=status.HTTP_201_CREATED)
# def post_data(payload: dict):
#     # u1 = User(id=1, name="Kim", age=32)
#     u1 = User(id=payload["id"],
#               name=payload["name"],
#               age=payload["age"])
#     users_db[payload["id"]] = u1
#     return payload


@api_2.post("/items", status_code=status.HTTP_201_CREATED)
def post_data(payload: UserCreateUpdate) -> UserOut:
    # default=0 avoids ValueError when the in-memory store is empty.
    max_id = max(users_db.keys(), default=0)
    u1 = UserOut(id=max_id + 1,
                 name=payload.name,
                 age=payload.age)
    users_db[u1.id] = u1.model_dump()
    return u1

@api_2.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def del_user(item_id: int) -> None:
    # Fetch user from store; dict.pop() removes and returns in one operation,
    # avoiding redundant lookups and reducing race condition risk in concurrent scenarios.
    deleted_user = users_db.pop(item_id, None)
    if deleted_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    # 204 No Content: successful deletion with no response body
    
@api_2.put("/items/{item_id}", status_code=status.HTTP_200_OK)
def update_user(item_id: int, payload: UserCreateUpdate) -> UserOut:
    if item_id in users_db:
        # Keep the canonical user id from the path parameter during full update.
        user_to_update = UserOut(id=item_id,
                                 name=payload.name,
                                 age=payload.age)
        users_db[item_id] = user_to_update.model_dump()
        return user_to_update
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
@api_2.patch("/items/{item_id}", status_code=status.HTTP_200_OK)
def update_user_partially(item_id: int, payload: UserPartialUpdate) -> UserOut:
    if item_id in users_db:
        current_user = users_db[item_id]
        updated_user = UserOut(
            id=item_id,
            name=payload.name if payload.name is not None else current_user["name"],
            age=payload.age if payload.age is not None else current_user["age"],
        )
        users_db[item_id] = updated_user.model_dump()
        return updated_user
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)