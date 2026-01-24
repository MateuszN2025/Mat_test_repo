import requests
import json
from mock_api_mn_ex1 import api_url_users
url2 = api_url_users

print("###################")
response = requests.get(url=url2)
print(response.status_code)

response2 = requests.request(method='GET', url=url2)
print(response2)
print(response2.json())
print(json.dumps(response2.json(), indent=3))

"""
HTTP status code:
200 - correct response
201 - correct modification
400 - error
404 - not found
500 - internal server error
"""