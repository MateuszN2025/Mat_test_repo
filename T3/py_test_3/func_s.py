import requests, json

url_json = "https://jsonplaceholder.typicode.com/posts/1"
url_json_post = "https://jsonplaceholder.typicode.com/posts/"

def f_r(url1):
    response = requests.get(url=url1)
    return  [response.json(),
             response.status_code]

def f_r_g(url1):
    response = requests.request(method='GET', url=url1)
    return  [response.json(),
             response.status_code]

def f_r_po(url1, data):
    response = requests.request(method='POST', url=url1, data=data)
    return response.status_code

def f_r_g_u(url1, userId):
    print(f"This is URL: {url1+str(userId)}")
    response = requests.request(method='GET', url=url1+str(userId))

    return response.json()

# print("------------------------")
# print(f_r(url_json)[0])
# print("------------------------")
# print(f_r(url_json)[1])
# print("------------------------")
# print(f_r(url_json)[0]['userId'])
# print(f_r(url_json)[0]['title'])
# print("------------------------")
# print("------------------------")
# print(f_r_g(url_json)[0]['title'])
# print("------------------------")
# data_json = {'userId': 221, 'id': 331}
# # print(f_r_po(url1=url_json[0:len(url_json)-1], data=data_json))
# print(f_r_po(url1=url_json_post, data=data_json))
# print(f_r(url_json)[0])
print("------------------------")
aaa = f_r_g_u(url1=url_json_post, userId=5)
print(type(aaa))
bbb = json.dumps(aaa, indent=4)
print(bbb)
print(type(bbb))