import requests
import json
base_url = "http://127.0.0.1:8000"
users_endpoint = "/users"
full_url = base_url + users_endpoint


# response_get = requests.get(url=full_url)
# print(json.dumps(response_get.json(), indent=4))

data_payload = {
        "name": "Jen",
        "age": 13
        }

requests.post(url=full_url, json=data_payload)
print("------------------------------------------")
response_get = requests.get(url=full_url)
print(json.dumps(response_get.json(), indent=4))