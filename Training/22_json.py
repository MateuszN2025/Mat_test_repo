"""
{
    "name": "John",
    "age": 30,
    "city": "New York"
}

{
    "string": "Hello world",
    "number_integer": 42,
    "number_float": 3.14,
    "boolean": true,
    "null": null,
    "array": [1, 2, 3],
    "object": {
        "nested": "value"
    }
}
"""
import json

# Konwersja Python -> JSON
# dumps() - do stringa
# dump() - do pliku

# Konwersja JSON -> Python
# loads() - z stringa
# load() - z pliku

# Python do JSON

data = {
    "name": "John",
    "age": 30
}
json_string = json.dumps(data)
print(json_string)  # {"name": "John", "age": 30}

# JSON do Python
json_string = '{"name": "John", "age": 30}'
data = json.loads(json_string)
print(data['name'])  # John


# Zapis do pliku
data = {
    "users": [
        {"name": "John", "age": 30},
        {"name": "Alice", "age": 25}
    ]
}

# Zapis
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)

# Odczyt
with open('data.json', 'r') as file:
    loaded_data = json.load(file)

# Ładne formatowanie
json_formatted = json.dumps(data, indent=4)

# Sortowanie kluczy
json_sorted = json.dumps(data, sort_keys=True)

"""
data = {
    "users": [
        {
            "name": "John",
            "address": {
                "street": "Main St",
                "city": "New York"
            }
        }
    ]
}

# Dostęp do zagnieżdżonych danych
print(data['users'][0]['address']['city'])
"""


# Prosta aplikacja z JSON
import json
import requests

def fetch_user_data(user_id):
    response = requests.get(f'https://api.example.com/users/{user_id}')
    return response.json()

def save_user_data(user_id, data):
    with open(f'user_{user_id}.json', 'w') as file:
        json.dump(data, file, indent=4)

# Użycie
user_data = fetch_user_data(123)
save_user_data(123, user_data)