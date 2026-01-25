import requests
import json

url1 = 'https://jsonplaceholder.typicode.com/posts/1'
response1 = requests.get(url=url1)
print("####################")
print(response1.status_code)
print(response1.json())
print(json.dumps(response1.json(), indent=4))

print("####################")
response2 = requests.request(method='GET', url=url1)
print(json.dumps(response2.json(), indent=3))
