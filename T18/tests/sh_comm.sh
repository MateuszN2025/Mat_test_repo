#!/bin/bash

# command=$1
command="${1:-GET}"

# if [[ $item_id == "" ]]; then
#     item_id=456
# fi

item_id="${2:-0}" # This sets 456 when arg 2 is missing or empty.

data="{\"name\": \"Bob\", \"age\": 2}" # Hint: check the API model and ask whether id is server-generated or required in request body.

if [[ $command == "GET" ]]; then
    curl "http://127.0.0.1:8000/items"
elif [[ $command == "POST" ]]; then
  curl -i -X POST "http://127.0.0.1:8000/items" \
   -H "Content-Type: application/json" \
   -H "Accept: application/json" \
   -d "$data"
elif [[ $command == "DEL" ]]; then
  curl -i -X DELETE "http://127.0.0.1:8000/items/$item_id" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
elif [[ $command == "PUT" ]]; then
  curl -i -X PUT "http://127.0.0.1:8000/items/$item_id" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json" \
  -d '{"name": "Ann", "age": 20}'
elif [[ $command == "PATCH" ]]; then
  curl -i -X PATCH "http://127.0.0.1:8000/items/$item_id" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json" \
  -d '{"age": 100}'
else
  echo "No valid command."
fi
echo
echo