#!/usr/bin/env bash

OPER=""
A=0
B=0
RES=0

read -rp "math operation: " OPER
read -rp "a : " A
read -rp "b : " B

case "$OPER" in
  +|-|'*'|/)
    RES=$((A $OPER B))
    echo "$A $OPER $B = $RES"
    ;;
  *)
    echo "Unsupported operation: $OPER"
    exit 1
    ;;
esac


#case "$OPER" in
#  +) RES=$(( A + B )) ;;
#  -) RES=$(( A - B )) ;;
#  '*') RES=$(( A * B )) ;;
#  /) RES=$(( A / B )) ;;
#  *)
#    echo "Unsupported operation: $OPER"
#    exit 1
#    ;;
#esac
