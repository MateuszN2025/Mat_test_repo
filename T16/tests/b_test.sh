#!/bin/bash
method="$1"
item_id="$2"

if [[ $method == "GET" ]]; then
    if [[ $item_id == "" ]]; then   
        echo "GET all"
        # curl "http://127.0.0.1:8000/items"
        curl -s "http://127.0.0.1:8000/items?pretty=true"
    else
        echo "GET $item_id"
        curl "http://127.0.0.1:8000/items/$item_id"
    fi

elif [[ $method == "POST" ]]; then
    echo "POST"
    curl -X POST "http://127.0.0.1:8000/items" \
    -H "Content-Type: application/json" \
    -d "{\"id\": $item_id, \"name\": \"XXX\", \"price\": 27779.00}"

elif [[ $method == "PATCH" ]]; then
    echo "PATCH"
    # -s              : silent mode — suppresses curl's progress meter
    # -w "..."        : write-out — appends the HTTP status code after the response body
    # -X PATCH        : sets the HTTP method to PATCH
    # -H "..."        : sets the Content-Type header so the server knows we're sending JSON
    # -d "..."        : request body — id selects which item to update, name is the field being patched
    curl -s -w "\nStatus: %{http_code}\n" -X PATCH "http://127.0.0.1:8000/items" \
        -H "Content-Type: application/json" \
        -d "{\"id\": $item_id, \"name\": \"patched_name\"}"

elif [[ $method == "PUT" ]]; then
    echo "PUT"
    curl -s -w "\nStatus: %{http_code}\n" -X PUT "http://127.0.0.1:8000/items" \
        -H "Content-Type: application/json" \
        -d "{\"id\": $item_id, \"name\": \"put_name\", \"price\": \"8888\"}"

# elif [[ $method == "DELETE" ]]; then
#     echo "DELETE"
#     curl -s -w "\nStatus: %{http_code}\n" -X DELETE "http://127.0.0.1:8000/items" \
#         -H "Content-Type: application/json" \
#         -d "{\"id\": $item_id}"

elif [[ $method == "DELETE" ]]; then
    echo "DELETE"
    curl -s -w "\nStatus: %{http_code}\n" -X DELETE "http://127.0.0.1:8000/items/$item_id" 
else
    echo "HTTPS method isn't selected. ⚠️"
fi

echo
