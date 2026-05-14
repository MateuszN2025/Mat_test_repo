import json, w_r

oa = {
"openapi": "3.1.0",
"info": {
"title": "FastAPI",
"version": "0.1.0"
},
"paths": {
"/items": {
"post": {
"requestBody": {
"required": True,
"content": {
"application/json": {
"schema": { "$ref": "#/components/schemas/ItemCreate" }
}
}
},
"responses": {
"201": { "description": "Successful Response" },
"422": { "$ref": "#/components/schemas/HTTPValidationError" }
}
},
"get": {
"parameters": [
{ "name": "pretty", "in": "query", "schema": { "type": "boolean", "default": False } }
]
}
},
"/items/{item_id}": {
"get": {
"parameters": [
{ "name": "item_id", "in": "path", "required": True, "schema": { "type": "integer" } }
]
}
}
},
"components": {
"schemas": {
"ItemCreate": {
"type": "object",
"required": ["id", "name", "price"],
"properties": {
"id": { "type": "integer" },
"name": { "type": "string", "minLength": 1 },
"price": { "type": "number", "exclusiveMinimum": 0.0 }
}
}
}
}
}

# print(json.dumps(oa, indent=4))
@w_r
def file():
    try:
        with open("open_api.json", "r"):
            print("File was already created✅.")
    except (FileNotFoundError) as e:
        print(f"{e} ⚠️")
        # file creation if does not exists
        print("New file will be createdℹ️.")
        with open("open_api.json", "w") as fj:
            fj.write(json.dumps(oa, indent=4))        
    finally:
        print("File exists anyway.")
    
    print()
    try:
        result = 1/3
    except ZeroDivisionError as e:
        print(e)
    else:
        # else works when try block will be exectuted without issue
        # The else handles the success case.
        print(f"ELSE")
        print("Success:", result)
    finally:
        print("FINALLY")
        
file()

"""
from pathlib import Path
import json
from app.app1 import app1

def export_openapi() -> Path:
    output_path = Path(__file__).resolve().parent / "open_api.json"
    output_path.write_text(json.dumps(app1.openapi(), indent=4), encoding="utf-8")
    return output_path

if __name__ == "__main__":
    path = export_openapi()
    print(f"OpenAPI exported to {path}")
"""