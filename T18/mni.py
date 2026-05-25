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

# print(dict2["b"])

base = {"APP_HOST": "old-host", "X": "1"}

env = {
    **base,
    "APP_HOST": "127.0.0.1",
    "APP_PORT": "8000",
}

# print(env)

# list1 = [1,2,3]

usr = users_db[1]
# print(usr)

a = [{"id":1,"name":"Bob","age":43},{"id":2,"name":"Sam","age":54}]
print(a.max())