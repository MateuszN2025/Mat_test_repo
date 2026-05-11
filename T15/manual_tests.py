import w_r
import requests
import json


URL = "http://127.0.0.1:8000/"
ITEMS = "items/"
ID = "1/"

@w_r
def main():
    
    payload1 = {
        "id": 1,
        "name": "Keyboard",
        "price": 199,
        "tags": ["electronics"],
        "is_active": True
    }
    
    payload2 = {
        "id": 15,
        "name": "Mouse",
        "price": 10,
        "tags": ["electronics"],
        "is_active": True
    }
    
    print("------------------------------------------")
    print(requests.post(url=f"{URL + ITEMS}", json=payload1).status_code)
    print(requests.post(url=f"{URL + ITEMS}", json=payload2).status_code)
    
  
    
    print("------------------------------------------")
    id1 = f"{URL + ITEMS}" + "1"
    response3 = requests.get(id1)
    print(json.dumps((response3.json()), indent=4))
    print(response3.status_code)
    
    print("------------------------------------------")
    id2 = f"{URL + ITEMS}" + "15"
    response4 = requests.get(id2)
    print(json.dumps((response4.json()), indent=4))
    print(response4.status_code)
    
    print("------------------------------------------")
    id3 = f"{URL + ITEMS}"
    response5 = requests.get(id3)
    print(json.dumps((response5.json()), indent=4))
    print(response5.status_code)
    
    
main()