from pydantic import BaseModel, Field


class ItemCreate(BaseModel):
    name: str = Field(min_length=1)
    price: float = Field(gt=0)
    tags: list[str] = Field(default_factory=list)
    is_active: bool = True


class ItemReplace(ItemCreate):
    pass


class ItemPatch(BaseModel):
    name: str | None = Field(default=None, min_length=1)
    price: float | None = Field(default=None, gt=0)
    tags: list[str] | None = None
    is_active: bool | None = None


class ItemResponse(ItemCreate):
    id: int
    display_price: float


class HealthResponse(BaseModel):
    status: str
