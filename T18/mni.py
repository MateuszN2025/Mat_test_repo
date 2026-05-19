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

print(users_db)