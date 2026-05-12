
# Import Pydantic's BaseModel and Field for data validation and serialization
from pydantic import BaseModel, Field



# Base class for item data. Inherits from Pydantic's BaseModel for validation.
class ItemBase(BaseModel):
    # Item name, must be a non-empty string
    name: str = Field(min_length=1)
    # Item price, must be a float greater than 0
    price: float = Field(gt=0)
    # List of tags, defaults to empty list
    tags: list[str] = Field(default_factory=list)
    # Whether the item is active, defaults to True
    is_active: bool = True



# Model for creating a new item. Requires all ItemBase fields plus an id.
class ItemCreate(ItemBase):
    # Unique identifier for the item
    id: int



# Model for replacing an item (PUT). Same as ItemBase, no id field.
class ItemReplace(ItemBase):
    pass



# Model for partial update (PATCH). All fields are optional and can be None.
class ItemPatch(BaseModel):
    # Optional name, must be non-empty string if provided
    name: str | None = Field(default=None, min_length=1)
    # Optional price, must be >0 if provided
    price: float | None = Field(default=None, gt=0)
    # Optional tags list
    tags: list[str] | None = None
    # Optional is_active flag
    is_active: bool | None = None



# Model for API responses. Includes all ItemBase fields, id, and display_price.
class ItemResponse(ItemBase):
    # Unique identifier for the item
    id: int
    # Price formatted for display (could include discounts, etc.)
    display_price: float



# Model for health check endpoint response.
class HealthResponse(BaseModel):
    # Status string (e.g., 'ok')
    status: str
