#!/bin/bash
echo "Mat 323"
echo "arguments: $1 $2"
echo "\$@: $@"
echo "\$*: $*"
echo $#

if [[ $1 -ge 1000 && $1 -lt 2000 ]]; then
    echo "Good number"
else
    echo "Bad !"
fi

POKEMAN_URL="https://pokeapi.co/api/v2/pokemon/ditto"
echo "--------"
curl "$POKEMAN_URL" > ditto.txt

echo "--------"
# while true; do date | awk '{print $4}'; sleep 1; done

for i in 1 2 3 4 5; do
    printf $i
done

API_URL="${API_URL:-http://127.0.0.1:8000/users}"
BEARER_TOKEN="${BEARER_TOKEN:-replace_me}"
data='{"name":"ditto"}'

curl --location --request POST "$API_URL" \
    --header "Authorization: Bearer $BEARER_TOKEN" \
    --header "Content-Type: application/json" \
    --header "Accept: application/json" \
    --data "$data"

TOKEN=$(curl -sS -X POST "http://127.0.0.1:8000/auth/login" \
  -H "Content-Type: application/json" \
  -d '{"username":"qa_user","password":"qa_pass"}' | jq -r '.access_token')

TOKEN_WITH_QUOTES=$(curl -sS -X POST "http://127.0.0.1:8000/auth/login" \
    -H "Content-Type: application/json" \
    -d '{"username":"qa_user","password":"qa_pass"}' | jq '.access_token')

TOKEN_NO_JQ=$(curl -sS -X POST "http://127.0.0.1:8000/auth/login" \
    -H "Content-Type: application/json" \
    -d '{"username":"qa_user","password":"qa_pass"}' | sed -n 's/.*"access_token"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p')

# Input JSON: {"access_token":"abc123"}
# jq '.access_token' -> "abc123" (with quotes)
# jq -r '.access_token' -> abc123 (no quotes)
# no jq option (sed) -> abc123 (works for simple one-line JSON)

curl -sS -H "Authorization: Bearer $TOKEN" "http://127.0.0.1:8000/users"
