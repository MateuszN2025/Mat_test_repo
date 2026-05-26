from fastapi import FastAPI, HTTPException
from fastapi.responses import Response
from pydantic import BaseModel
import random

# ── Data Models ──────────────────────────────────────────────────────────────

class UserCreate(BaseModel):
    name: str
    age: int


class User(BaseModel):
    id: int
    name: str
    age: int


# ── In-Memory Data Store ──────────────────────────────────────────────────────

_SEED_NAMES = [
    "Alice", "Bob", "Charlie", "Diana", "Ethan",
    "Fiona", "George", "Hannah", "Ivan", "Julia",
]

users: list[dict] = [
    {"id": i + 1, "name": name, "age": random.randint(18, 65)}
    for i, name in enumerate(_SEED_NAMES)
]

next_id: int = len(users) + 1


# ── App ───────────────────────────────────────────────────────────────────────

app = FastAPI(title="User Management API")


# ── Endpoints ─────────────────────────────────────────────────────────────────

@app.get("/users", response_model=list[User])
def list_users():
    return users


@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")


@app.post("/users", response_model=User, status_code=201)
def create_user(body: UserCreate):
    global next_id
    user = {"id": next_id, "name": body.name, "age": body.age}
    next_id += 1
    users.append(user)
    return user


@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, body: UserCreate):
    for user in users:
        if user["id"] == user_id:
            user["name"] = body.name
            user["age"] = body.age
            return user
    raise HTTPException(status_code=404, detail="User not found")


@app.delete("/users/{user_id}", status_code=204)
def delete_user(user_id: int):
    for i, user in enumerate(users):
        if user["id"] == user_id:
            users.pop(i)
            return Response(status_code=204)
    raise HTTPException(status_code=404, detail="User not found")
