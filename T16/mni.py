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

print("------------------------------------------")
l1=[{"id":1,"name":"Laptop","price":999.99},{"id":2,"name":"Monitor","price":349.0}]
for i in l1:
    print(i)
    
print("------------------------------------------")
items_db: dict[int, dict] = {
    1: {"id": 1, "name": "Laptop",  "price": 999.99},
    2: {"id": 2, "name": "Monitor", "price": 349.00},
    3: {"id": 3, "name": "Monitor", "price": 349.00},}

payload = {"id": 3, "name": "Banana"}
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
#         print("Id from payload does not match❌")            
# else:
#     print("Id does not EXIST⚠️ in payload")
item_id = 1 
    
items_db[payload["id"]] = payload
print("------------------------------------------")  
# print(payload["id"])
print(items_db)
del items_db[item_id]
print(items_db)
