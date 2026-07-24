a=2
b=2

if (( $a >= $b )); then
    echo "a wins"
else
    echo "b wins"

fi

c="mama"
d="mama"

if [[ $c -eq $d ]]; then
    echo "equal"
else
    echo "not equal"
fi