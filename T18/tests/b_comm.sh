#!/bin/bash

# command=$1
command="${1:-GET}"

# if [[ $item_id == "" ]]; then
#     item_id=456
# fi

item_id="${2:-456}" # This sets 456 when arg 2 is missing or empty.
data="{\"id\": $item_id, \"name\": \"XXX\", \"age\": 88}"

if [[ $command == "GET" ]]; then
    curl "http://127.0.0.1:8000/items"
elif [[ $command == "POST" ]]; then
# curl -X POST "http://127.0.0.1:8000/items" \
#   -H "Content-Type: application/json" \
#   -H "Accept: application/json" \
#   -H "X-Request-ID: test-456" \
#   -d "$data"
  curl -i -X POST "http://127.0.0.1:8000/items" \
   -H "Content-Type: application/json" \
   -H "Accept: application/json" \
   -d "$data"

  # -d '{"id": 7, "name": "Ann", "age": 20}'

fi



echo
echo