#!/usr/bin/env bash

echo CALCULATOR

OPER=""
A=0
B=0
RES=0

read -rp "math operation: " OPER
read -rp "a : " A
read -rp "b : " B

case "$OPER" in
  +|-|'*'|/)
#   RES=$((A $OPER B)) # 234 / 432 = 0
#   RES=$(echo "scale=4; $A $OPER $B" | bc) # 234 / 432 = .5416
    RES=$(awk "BEGIN { printf \"%.4f\", $A $OPER $B }")
    echo "$A $OPER $B = $RES"
#    echo "$RES"
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
