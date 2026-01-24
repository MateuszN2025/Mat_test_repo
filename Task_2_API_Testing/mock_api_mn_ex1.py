import requests, json
api_url_users = 'http://127.0.0.1:5003/users'

# if __name__ == '__main__':
# this protects before running this script
# (whole code below)
# when we import this file somewhere else

print("------------------")
print(__name__)
# if I run this program here - it will be
# __main__
# if I run this program from other file - it will be
# 'mock_api_mn_ex1'
print("------------------")
response = requests.get(api_url_users)
print("Status code:", response.status_code)
print("Response JSON:", response.json())
a = json.dumps(response.json(), indent=4)
print(f"nice string: {a}")
"""
json.dump() 👉 writes JSON to a file
json.dumps() 👉 returns a string
----------------
Function	Use case
json.dumps()	JSON → string (for printing/logging)
json.dump()	JSON → file
json.loads()	string → Python object
json.load()	file → Python object
"""
