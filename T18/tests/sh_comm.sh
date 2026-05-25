#!/bin/bash

# command=$1
command="${1:-GET}"

# if [[ $user_id == "" ]]; then
#     user_id=456
# fi

user_id="${2:-""}" # This sets 456 when arg 2 is missing or empty.

data="{\"name\": \"Bob\", \"age\": 2}" # Hint: check the API model and ask whether id is server-generated or required in request body.

if [[ $command == "GET" && $user_id == "" ]]; then
  curl "http://127.0.0.1:8000/users"
elif [[ $command == "GET" && $user_id != ""  ]]; then
  curl "http://127.0.0.1:8000/users/$user_id"
elif [[ $command == "POST" ]]; then
  curl -i -X POST "http://127.0.0.1:8000/users" \
   -H "Content-Type: application/json" \
   -H "Accept: application/json" \
   -d "$data"
elif [[ $command == "DEL" ]]; then
  curl -i -X DELETE "http://127.0.0.1:8000/users/$user_id" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
elif [[ $command == "PUT" ]]; then
  curl -i -X PUT "http://127.0.0.1:8000/users/$user_id" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json" \
  -d '{"name": "Ann", "age": 20}'
elif [[ $command == "PATCH" ]]; then
  curl -i -X PATCH "http://127.0.0.1:8000/users/$user_id" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json" \
  -d '{"age": 100}'
else
  echo "No valid command."
fi
echo
echo