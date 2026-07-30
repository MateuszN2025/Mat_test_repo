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
# ssh -i ~/.ssh/id_ed25519 user@host
# ssh vboxuser1@192.168.0.152

echo "-----sshpass ------"
# sshpass -p "changeme1@" ssh vboxuser1@192.168.0.152

echo "-----ssh-keygen ------"
# ssh-keygen
# ssh-keygen -t ed25519 -C "your_email@example.com"
# -t type
# -C comment

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

echo "-----curl POST auth ------"
# -H "Content-Type: application/json" # most common
# Content-Type: format of request body you send
# Accept: format you want back.
# Authorization: token/API key/basic auth.

TOKEN=$(curl -s -X POST "http://127.0.0.1:8000/auth/token" \
    -H "Content-Type: application/x-www-form-urlencoded" \
    -d "username=admin&password=admin123" \
    | python3 -c 'import json,sys; print(json.load(sys.stdin).get("access_token", ""))')

if [[ -z "$TOKEN" ]]; then
        echo "Token fetch failed"
        exit 1
fi

echo "⚠️ TOKEN: $TOKEN"
echo

echo "-----curl GET auth ------"
curl -X GET "http://127.0.0.1:8000/users" \
    -H "Authorization: Bearer $TOKEN"

# ############################################
# # 1) GET with Accept + Bearer token
# curl -X GET "http://127.0.0.1:8000/users" \
#   -H "Accept: application/json" \
#   -H "Authorization: Bearer token-admin"
# ############################################
#   # 2) POST form data (OAuth2 token style)
# curl -X POST "http://127.0.0.1:8000/auth/token" \
#   -H "Content-Type: application/x-www-form-urlencoded" \
#   -d "username=admin&password=admin123"
#   # ℹ️ -H "Content-Type: application/json"
#   # ℹ️ -d '{"username":"admin","password":"admin123"}'
# ############################################
#   # 3) POST JSON body
# curl -X POST "http://127.0.0.1:8000/items" \
#   -H "Content-Type: application/json" \
#   -H "Accept: application/json" \
#   -d '{"name":"book","price":10}'


echo "-----python3 http server ------"
# cd /tmp
# python3 -m http.server 8033

echo "-----wget ------"
# wget -O custom_name.txt http://localhost:8121/m_file

echo "-----uname -a ------"
uname -a

# uname -a | tr ' ' '\n' # It replaces every space with a newline, so each word is printed on its own line.

echo "-----cmp------"
cmp root_text1.log root_text2.log
# root_text1.log root_text2.log differ: byte 1, line 1

echo "-----diff------ compare files line by line"
diff -y root_text1.log root_text2.log

# 2>

echo "-----uptime------"
uptime -p
uptime

echo "-----id - print real and effective user and group IDs-----"
# id output confirms the current user is root:
# uid=0(root) → user ID is 0 (superuser)
# gid=0(root) → primary group is root
# groups=0(root) → only in root group
id -un

echo "-----apt------"
apt list --installed | tail -n 5

echo "-----ip route------"
ip route get 8.8.8.8

echo "-----tcpdump------"
# ℹ️ tcpdump -s1500 -nlpi eth0
# wlan0
# ppp0

# tcpdump -s1500 -nlpi eth0 captures packets on interface 
#   eth0 with practical defaults for troubleshooting.
# -s1500 → snap length: capture up to 1500 bytes per packet 
#   (often full Ethernet payload, but not always full jumbo/encapsulated frames).
# -n → no DNS/service name resolution (faster, cleaner output).
# -l → line-buffered output (good for piping to grep/logs in real time).
# -p → do not enable promiscuous mode.
#       promiscuous mode means a network interface accepts all packets it 
#       can see, not just packets addressed to its own MAC address.
# -i eth0 → listen on interface eth0.

# ℹ️ sudo tcpdump -s0 -nli eth0 -c 100
# -s0 — capture entire packet (no snap-length truncation).
# -n — disable name resolution (show raw IPs/ports).
# -l — line-buffered output (useful for piping/live logs).
# -i eth0 — capture on interface eth0.
# -c 100 — stop after 100 packets.


# ⚠️ Wireshark
# HTTP is request → response. The client always initiates. 
# Once the server responds, the connection closes (or idles).
# ℹ️ WebSocket is a persistent, bidirectional connection. 
# After an initial HTTP handshake, both sides can send messages at any time.
# 
# Interface → Capture Filter → Packets → Display Filter → Analysis
# Display Filters (Most Used Daily)
# By protocol
    # tcp
    # udp
    # websocket
    # tls

# By IP
    # ip.addr == 192.168.1.10
    # ip.src == 192.168.1.1
    # ip.dst == 192.168.1.2

# By port
    # tcp.port == 9000          # common OCPP WebSocket port
    # tcp.port == 8443

# Combine
    # ip.addr == 192.168.1.10 && tcp.port == 9000

# Find specific content (slow, use carefully)
    # frame contains "BootNotification"


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

echo "-----redirection basics------"

echo "1) stdout to file with 1>"
echo "hello stdout" 1> out.log

echo "2) stderr to file with 2>"
ls /path/that/does/not/exist 2> err.log || true

echo "3) send stdout to stderr with 1>&2"
echo "this goes to stderr" 1>&2

echo "-----more redirection options------"
# ❌1&>2 is not valid❌. Use 1>&2 (or just >&2 in bash).

echo "4) short form: stdout to stderr with >&2"
echo "stdout redirected to stderr" >&2

echo "5) discard only stdout to /dev/null"
echo "this will be hidden" > /dev/null

echo "6) discard only stderr to /dev/null"
ls /path/that/does/not/exist 2> /dev/null || true

echo "7) discard both stdout and stderr"
ls /path/that/does/not/exist > /dev/null 2>&1 || true

echo "8) bash shortcut: send both stdout+stderr"
ls /path/that/does/not/exist &> /tmp/devnull || true


echo "----- dd ------"
# dd = low-level byte/block copy tool (disk/files/streams)
# Syntax:
#   dd if=<input_file> of=<output_file> [bs=<block_size>] [count=<blocks>] [skip=<in_blocks>] [seek=<out_blocks>] [status=progress]
#
# Most useful options:
# if=   input source ("if" = input file)
# of=   output target ("of" = output file)
# bs=   block size (for example: 1K, 1M, 4M)
# count=number of blocks to copy
# skip= skip N blocks from input before copying
# seek= skip N blocks on output before writing
# conv= conversion flags (for example: conv=notrunc,noerror,sync)
# status=progress shows live transfer progress
#
# Safe/basic examples:
# 1) Create a 10 MiB zero-filled file
#    dd if=/dev/zero of=zero_10M.bin bs=1M count=10 status=progress
#
# 2) Backup a disk/partition to an image file (read-only style usage)
#    dd if=/dev/sdX of=disk_backup.img bs=4M status=progress
#
# 3) Restore image back to disk (DANGEROUS: overwrite target)
#    dd if=disk_backup.img of=/dev/sdX bs=4M status=progress
#
# 4) Write random data for quick test file
#    dd if=/dev/urandom of=random_5M.bin bs=1M count=5 status=progress
#
# ⚠️ Be very careful with of=/dev/sdX: wrong target can destroy data.

