#!/bin/bash
item_id="$1"
curl "http://127.0.0.1:8000/items$1"

# curl -X POST "http://127.0.0.1:8000/items/3" \
#   -H "Content-Type: application/json" \
#   -d '{"id": 3, "name": "XXX", "price": 27779.00}'
