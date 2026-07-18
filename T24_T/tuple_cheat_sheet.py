api_response = (200, "OK", {"id": 1}, 400)
tup1 = (9999,)

# print(dir(tuple))
print(api_response.count(200))
print(api_response.index("OK"))
print(api_response + tup1)
print(api_response[2])
status_code, value, data, _ = api_response
print(status_code)
print(api_response[3])

input1 = ("chrome", "127.0", "linux")
def task_tuple_unpack_browser_info(browser_tuple: tuple) -> str:
    """
	Input: ("chrome", "127.0", "linux")
	Output: "BROWSER=chrome VERSION=127.0 OS=linux"
	"""
    br, ver, os = browser_tuple
    return f"BROWSER={br} VERSION={ver} OS={os}"

print(task_tuple_unpack_browser_info(input1))