from pydantic import BaseModel, Field

# a = "http://127.0.0.1:8000/items/"
# print(f"{a}1")


class ItemCreate(BaseModel):
    id: int
    name: str = Field(min_length=1)
    price: float = Field(gt=0)
    
i1 = ItemCreate(id=112, name="ABC", price=1)


# i2 = ItemCreate(id="a", name="ABCD", price=1) 
# #  unable to parse string as an integer [type=int_parsing, input_value='a', input_type=str]

i3 = ItemCreate(id="1", name="ABCD", price=1) 
# i4 = ItemCreate(id="1", name="", price=1) # String should have at least 1 character
# i5 = ItemCreate(id="1", name="", price=-9) #Input should be greater than 0


items_db: dict[int, dict] = {
    1: {"id": 1, "name": "Laptop",  "price": 999.99},
    2: {"id": 2, "name": "Monitor", "price": 349.00},
}

items_db_list = list(items_db)
print("------------------------------------------")
print(items_db_list)
print(len(items_db_list))