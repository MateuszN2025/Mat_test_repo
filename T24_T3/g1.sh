#!/bin/bash
echo "-----curl GET ------"
# API_URL="http://127.0.0.1:8000/items"
# ENDPOINT="/items"
# echo ${API_URL}${ENPOINT}
# curl -s -X GET "$API_URL$ENPOINT"
# curl "http://127.0.0.1:8000/users" # ✅
API_URL="http://127.0.0.1:8000"
ENDPOINT="/users"
TOKEN="token-admin"
echo "${API_URL}${ENDPOINT}"
curl -s -X GET "$API_URL$ENDPOINT" \
     -H "Authorization: Bearer $TOKEN"

echo