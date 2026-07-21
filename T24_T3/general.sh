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
echo "-----func-----"
 function func(){
    local pwd1="${1:-$(pwd)}"
    echo "$pwd1"
}
func 
echo "----if------"
param=5
if [[ $param -gt 4 ]]; then
    echo "old child"
else
    echo "young child"
fi

echo "-----for simple-----"
for i in 1 2 3 4; do
    echo "$i"
done

echo "-----for medium-----"
for ((i=;i<10;i++)); do
    echo "$i"
done

echo "-----while-----"
counter1=3
while [[ counter1 -gt 0 ]]; do
    echo "$counter1"
    counter1=$((counter1-1))
done


echo "-----while one line-----"
counter111=3
while [[ $counter111 -gt 0 ]]; do date | awk '{print $4}'; \
 counter111=$((counter111-1)); sleep 0.1; done

# CC=5
# while [[ $CC -gt 0 ]]; do
#     date 
#     sleep 1
#     CC=$((CC-1))
# done 
echo "-----read-----"
while read -r line; do
    echo "PREFIX|$line"
done < sed.log

# echo "-----sed-----"
# sed -i 's/ccc/ppp/g' sed.log
# echo

echo "-----awk-----"
ps aux | grep python | awk 'BEGIN {print "USER PID"} {print $1, $2, $3}'

echo "-----grep-----"
type=INFO
cat sed.log | grep "$type" | echo "$type: $(wc -l)" # 2

echo "-----touch-----"
# touch text1.txt text2.txt

echo "-----for & files 1-----"
for file in *.txt; do
    echo "$file"
done

echo "-----for & files 2-----"
# for file in *.txt; do
#     mv "$file" "$(whoami)_$file"
# done

echo "-----for & files 3-----"
# for file in *.txt; do
#     mv "$file" "${file%.txt}.log"
# done

# # Remove any extension
# ${file%.*}
# # Replace extension
# ${file%.*}.new
# # Remove multiple dots (e.g., file.tar.gz)
# ${file%%.tar.gz}.log

echo "-----find-----"
find ./ -type f -name "*e*" 

echo "-----here doc-----"
bash << EOF
    func1(){
        echo "⚠️  here doc"      
    }
    func1
EOF

echo "-----func with \$-----"
func1(){
        echo "\$1: $1"
        echo "\$2: $2"
        echo "num of param $#"
        echo "params: $@"     
        echo "params: $*"     
}
func1 123123 "Cat"

echo "-----here doc-----"
cut -c1-80 ps_log.logs | head -n 5

echo "-----ls----------"
ls -lS | grep '^-'

echo "-----if -f ------"
if [[ -f "sed1.log" ]];then
    echo "File exists ✅ "
else
    echo "File does not exists ❌"
fi

echo "-----ssh ------"

echo "-----sshpass ------"

echo "-----ssh keygen ------"

echo "-----curl ------"

echo "-----wget ------"
# wget -O custom_name.txt http://localhost:8121/m_file

# 2>
# uname -a
# cmp, diff
# uptime -p
# id -un
# env | grep 'HOME\|PATH'
# history
# ip route
# ⚠️ tcpdump
# ⚠️ Wireshark
# apt list --installed 

# != → string not equal
# -ne → numeric not equal (integers)
# && : AND
# || : OR
# ! : NOT
# -eq equal
# -ne not equal
# -gt greater than
# -ge greater or equal
# -lt less than
# -le less or equal