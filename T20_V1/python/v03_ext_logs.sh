#!/bin/bash

# FILE1="v03_logs.txt"
# FILE2="v03_logs_extracted.txt"

# if [[ -f $FILE2 ]]; then
#     echo "File already exists"
# else
#     touch $FILE2
# fi

# while read line; do
#     echo "$line" | grep INFO >> $FILE2
# done < $FILE1

# amount=$(wc -l < $FILE2)
# echo "$amount"

#!/bin/bash

# ======================================================

FILE1="v03_logs.txt"
# FILE2="v03_logs_extracted.txt"

# # > overwrites cleanly on every run — no stale data from previous runs
# grep 'INFO' "$FILE1" > "$FILE2"

# amount=$(wc -l < "$FILE2")
# echo "$amount"

# ======================================================

#!/bin/bash
grep -c 'INFO' "$FILE1"

# grep -o '\[\w\+\]' "$FILE1" | tr -d '[]'
grep -o '\[\w\+\]' v03_logs.txt | tr -d '[]' | sort | uniq -c