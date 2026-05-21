users_db: dict[int, dict] = {
    1: {"id": 1,
        "name": "Bob",
        "age": 43},
    2: {"id": 2,
        "name": "Sam",
        "age": 54}
}

payload={"id": 3, "name": "John", "age": 88}

users_db[payload["id"]] = payload

# print(users_db)

ids=[id for id in users_db.keys()]
# print(max(ids))

# print(users_db[3]["age"])

def dict1():
    return {"a":1, "b":2}

def dict2(dict1):
    return dict1

print(dict2["b"])