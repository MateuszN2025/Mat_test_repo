#!/bin/bash
POKEMAN_URL="https://pokeapi.co/api/v2/pokemon/ditto"
echo "--------"
curl "$POKEMAN_URL" | jq -c '.forms'