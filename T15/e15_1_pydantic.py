
# PYDANTIC LEARNING PATH: Most Common Cases
from pydantic import BaseModel, Field, ValidationError, field_validator, ConfigDict
from typing import Optional
import w_r


# =============================================================================
# Define all models
# =============================================================================

# 1. Basic model with required fields
class User(BaseModel):
    id: int
    name: str


# 4. Using Field for extra validation
class Product(BaseModel):
    name: str = Field(min_length=2)
    price: float = Field(gt=0)


# 5. Optional fields and defaults
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    tags: list[str] = []


# 6. Nested models
class Order(BaseModel):
    user: User
    products: list[Product]


# 7. Model config: strict types, validate assignment (Pydantic v2 syntax)
class StrictUser(BaseModel):
    model_config = ConfigDict(validate_assignment=True)
    
    id: int
    name: str


# 8. Custom validation with @field_validator
class CustomModel(BaseModel):
    value: int
    
    @field_validator('value')
    @classmethod
    def must_be_even(cls, v):
        if v % 2 != 0:
            raise ValueError('must be even')
        return v


# 10. Aliases and extra fields (Pydantic v2 syntax)
class AliasModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    
    real_name: str = Field(alias="realName")


# =============================================================================
# Main function with all examples
# =============================================================================

@w_r
def main():
    # 1. Basic model with required fields
    print("1. Basic model:")
    user = User(id=1, name="Alice")
    print(user)

    # 2. Type coercion (Pydantic v2 is strict by default)
    print("\n2. Type coercion (strict by default):")
    user2 = User(id=2, name="123")  # Both types match exactly
    print(user2)

    # If you try to pass name=123 (int), it will raise a validation error in Pydantic v2.
    # Uncomment below to see the error:
    # try:
    #     User(id=2, name=123)
    # except ValidationError as e:
    #     print(e)

    # 3. Validation error on bad input
    print("\n3. Validation error:")
    try:
        User(id="not_an_int", name="Bob")
    except ValidationError as e:
        print(e)

    # 4. Field validation
    print("\n4. Field validation:")
    try:
        Product(name="A", price=-5)
    except ValidationError as e:
        print(e)

    # 5. Optional fields
    print("\n5. Optional fields:")
    item = Item(name="Book")
    print(item)

    # 6. Nested models
    print("\n6. Nested models:")
    order = Order(user=user, products=[Product(name="Pen", price=1.5)])
    print(order)

    # 7. Strict model with validate_assignment
    print("\n7. Strict model:")
    strict_user = StrictUser(id=3, name="Eve")
    try:
        strict_user.id = "not_int"
    except ValidationError as e:
        print(e)

    # 8. Custom validator
    print("\n8. Custom validator:")
    try:
        CustomModel(value=3)
    except ValidationError as e:
        print(e)

    # 9. Model to dict/json
    print("\n9. Export to dict/json:")
    print(user.model_dump())
    print(user.model_dump_json())

    # 10. Aliases and extra fields
    print("\n10. Aliases:")
    alias = AliasModel(realName="Neo")
    print(alias)
    alias2 = AliasModel(real_name="Trinity")
    print(alias2)

    # ---
    # Senior tip: Use ValidationError to catch and handle bad input. Use Field for constraints. Use ConfigDict for model configuration.
    # Practice: Try changing types, omitting required fields, or breaking constraints to see Pydantic's error messages.


if __name__ == "__main__":
    main()