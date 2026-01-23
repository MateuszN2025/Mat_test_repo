#!/bin/bash
#while true; do date; sleep 1; done

# If-Else Statements
if [ condition ]; then
    # commands
elif [ another_condition ]; then
    # commands
else
    # commands
fi

# Comparison Operators
# -eq (equal)
# -ne (not equal)
# -gt (greater than)
# -lt (less than)
# -ge (greater or equal)
# -le (less or equal)

age=20
if [ $age -ge 18 ]; then
    echo "Adult"
else
    echo "Minor"
fi

# String Comparisons
if [ "$name" = "John" ]; then
    echo "Name is John"
fi

# File Tests
if [ -f filename ]; then
    echo "File exists"
fi

# Multiple Conditions
if [ condition1 ] && [ condition2 ]; then
    # AND condition
fi

if [ condition1 ] || [ condition2 ]; then
    # OR condition
fi