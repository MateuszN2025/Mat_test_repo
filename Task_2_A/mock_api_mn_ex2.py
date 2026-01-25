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
HTTP status codes:

200 - OK (request succeeded)
201 - Created (resource successfully created)
204 - No Content (successful update/delete with no response body)

400 - Bad Request (client sent invalid data)
401 - Unauthorized (authentication required)
403 - Forbidden (authenticated but no permission)
404 - Not Found (resource does not exist)
409 - Conflict (state conflict, e.g. duplicate resource)

500 - Internal Server Error (server-side failure)
"""