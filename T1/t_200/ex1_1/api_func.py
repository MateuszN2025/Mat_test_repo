import requests
import json

"""
| Funkcja | Wejście        | Wyjście        |
| ------- | -------------- | -------------- |
| `dump`  | obiekt Pythona | zapis do pliku |
| `dumps` | obiekt Pythona | `str` (JSON)   |
| `load`  | plik JSON      | obiekt Pythona |
| `loads` | `str` (JSON)   | obiekt Pythona |

"""

url_get = "https://jsonplaceholder.typicode.com/posts/1"
response_get = requests.get(url=url_get)
print(response_get)
print(response_get.status_code)
print(response_get.headers)
print("------------")
a = response_get.text
print(type(a))
j = response_get.json()
print(type(j))
print(j)
print(j['title'])
print(json.dumps(j,indent=4))
print("------------")
print("------------")
data1 = {'title': 'foo','body': 'bar','userId': 1,'S': 2}
# url_post = "https://jsonplaceholder.typicode.com/postsd/" 404 - wrong endpoint
url_post = "https://jsonplaceholder.typicode.com/posts/"
response_post = requests.post(url=url_post,data=data1)
print(response_post)
print(response_post.json())

'''
1xx continue 

2xx success
200 - OK
201 - created

3xx redirection

4xx error

400 Bad request
401 unauthorized
404 Not found

500 - internal server error
503 - SERVER UNAVAILABLE
'''


"""
curl -X POST -H "Content-Type: application/json" -d '{"title":"foo","body":"bar","userId":1,"S":2}' https://jsonplaceholder.typicode.com/posts
"""
