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
else
    echo "POST"
    curl -X POST "http://127.0.0.1:8000/items" \
    -H "Content-Type: application/json" \
    -d "{\"id\": $item_id, \"name\": \"XXX\", \"price\": 27779.00}"
    # -d "{'id': $item_id, 'name': 'xxx', 'price': 333.00}" #❌
fi

echo
