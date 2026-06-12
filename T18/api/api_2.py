from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field, model_validator

api_2 = FastAPI()

users_db: dict[int, dict] = {
    1: {"id": 1, "name": "Bob", "age": 43},
    2: {"id": 2, "name": "Sam", "age": 54}
}

class UserOut(BaseModel):
    id: int
    name: str = Field(min_length=2)
    age: int = Field(gt=0)

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

# 3. Use response_model
# FastAPI relies on the response_model argument in 
# the decorator to generate accurate OpenAPI schemas (Swagger UI)
# and automatically filter/serialize output data.
# Adding response_model=UserOut ensures only the fields defined 
# in that schema are ever sent to the client.

@api_2.get("/users", response_model=list[UserOut], status_code=status.HTTP_200_OK)
def get_users():
    # Standard REST behavior: return [] if the collection is empty
    return list(users_db.values())

@api_2.get("/users/{user_id}", response_model=UserOut, status_code=status.HTTP_200_OK)
def get_user(user_id: int):
    user = users_db.get(user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user
          
@api_2.post("/users", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def create_user(payload: UserCreateUpdate):
    max_id = max(users_db.keys(), default=0)
    new_user = UserOut(
        id=max_id + 1,
        name=payload.name,
        age=payload.age
    )
    users_db[new_user.id] = new_user.model_dump()
    return new_user

@api_2.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int) -> None:
        if users_db.pop(user_id, None) is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
@api_2.put("/users/{user_id}", response_model=UserOut, status_code=status.HTTP_200_OK)
def update_user_fully(user_id: int, payload: UserCreateUpdate):
    if user_id not in users_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        
    user_to_update = UserOut(
        id=user_id,
        name=payload.name,
        age=payload.age
    )
    users_db[user_id] = user_to_update.model_dump()
    return user_to_update
    
@api_2.patch("/users/{user_id}", response_model=UserOut, status_code=status.HTTP_200_OK)
def update_user_partially(user_id: int, payload: UserPartialUpdate):
    stored_user_data = users_db.get(user_id)
    if not stored_user_data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    # Dynamically update only the fields the user sent
    stored_user_model = UserOut(**stored_user_data)
    update_data = payload.model_dump(exclude_unset=True)
    updated_user = stored_user_model.model_copy(update=update_data)
    
    users_db[user_id] = updated_user.model_dump()
    return updated_user


"""
What to Add for a Production API
To transition this from a "good foundation" to a 
"production-ready architecture," you will eventually want to implement the following patterns:

Persistent Storage: An in-memory dictionary resets
every time your server restarts. The next major step is swapping
users_db for a real database (like PostgreSQL or SQLite) using an ORM like SQLAlchemy or SQLModel.

Dependency Injection: FastAPI shines with its Depends() system.
In a production app, you will use dependency injection to pass 
database sessions or user authentication tokens into your route functions automatically.

Layered Architecture: Right now, your routing (the @api_2 decorators),
your business logic, and your database access are all in one function. As
your app grows, you will want to split these into separate files
(e.g., routes.py, crud.py, models.py) to keep the codebase maintainable.

Environment Variables: Hardcoding configuration isn't safe for production.
You will want to use Pydantic's BaseSettings to load things like database
URLs and secret keys from a .env file.

Authentication: Adding security, such as OAuth2 with JWT (JSON Web Tokens),
to protect certain endpoints so only authorized users can create or delete data.

You have nailed the HTTP layer and the data validation layer perfectly.

What aspect of taking this to the next level interests you most—would
you like to look at how to structure this into multiple files, or how to connect
it to a real database?
"""
