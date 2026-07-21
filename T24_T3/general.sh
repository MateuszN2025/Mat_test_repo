# . and source (IDENTICAL in bash)
# . ./script.sh        # POSIX standard
#   source ./script.sh   # Bash-specific (does exact same thing)

# Both execute the script in the CURRENT shell process
# Variables set in script persist after execution
# Can access/modify parent shell's variables

# bash (different behavior)
#   bash script.sh       # Spawns NEW bash process
# Script runs in isolated environment
# Variables created in script are lost after execution
# Cannot modify parent shell's variables

# Use source/. when you need variables/functions to persist in your current shell
# Use bash when you want a clean, isolated execution environment

# command="${1:-GET}"
echo "----------"
func(){
    local pwd1="${1:-$(pwd)}"
    echo "$pwd1"
}
# func 
echo "----if------"
param=5
if [[ $param -gt 4 ]]; then
    echo "old child"
else
    echo "young child"
fi

echo "-----for-----"
for i in 1 2 3 4; do
    echo "$i"
done

echo "-----while-----"
counter1=3
while [[ counter1 -gt 0 ]]; do
    echo "$counter1"
    counter1=$((counter1-1))
done

# CC=5
# while [[ $CC -gt 0 ]]; do
#     date 
#     sleep 1
#     CC=$((CC-1))
# done 
echo "-----read-----"

# while read -r line; do
#     echo "PREFIX|$line"
# done < todo1.txt

echo "-----sed-----"
sed -i 's/ccc/ppp/g' sed.log
echo

echo "-----awk-----"
ps aux | grep python | awk 'BEGIN {print "USER PID"} {print $1, $2, $3}'

