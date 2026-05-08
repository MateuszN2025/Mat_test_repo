#!/bin/bash
# echo "--1--"
# date '+%T'

# while true; do date '+%T'; sleep 1; done
# while true; do
#     date '+%T'
#     sleep 1
# done

# ls -lS
# echo "----------"
# ls -lS | grep '^-' 
# echo "----------"
# ls -lS | grep '^d' 

# -rw-r--r-- 1 root root   19 May  7 13:00 file5.txt
# ^ -
# drwxr-xr-x 2 root root 4096 May  6 14:31 practice_dir
# ^ d

# echo "--3--"
# wc -l file1.txt

# find . -type d -mtime -1

# find prac* -type f
# find . -type f -name "*.sh"
# echo

# for f in *.txt; do echo "==$f=="; head -n 3 "$f"; done
# for f in *.txt; do
#     echo ">> $f <<"
#     head -n 3 "$f"
# done

# echo "--6--"
# for f in *.txt; do mv "$f" "${f// /_}"; done

# echo "--7--"
# du -sk /home/mniedziolka/PP/Mat_test_repo/T1
# du --apparent-size /home/mniedziolka/PP/Mat_test_repo/T1

# echo "--8--"
# who | awk '{print $1}' | sort | uniq

# echo "--9--"
# ps -u "$USER" | wc -l
# echo $USER

# echo "--10--"
# ls -l *.sh | awk '{print $1, $9}'

# echo "--12--"
# ls -t | head -n 1

# echo "--16--"
# ls -lS | grep '^-' | head -n 1 | awk '{print $9, $5}'

# awk: a text-processing tool that splits
#  each input line into fields (columns),
#  usually separated by spaces.
# awk '{print}' file6.txt
# echo "---"
# awk '{print $1 $3}' file6.txt
# awk 'NR==2' file6.txt
# echo "$HOME"
# if [[ -e "fdsff.txt" ]]; then echo ; fi
# # opopop
# echo $?
# ps aux --sort=-%cpu | head -n 6 | awk '{print $2 "\t" $3 "\t" $11}'
# ps aux --sort=-%cpu | head -n 6 | awk '{sub(/\/bin.*/, "/", $11); print $2 "\t" $3 "\t" $11}'
# env

# echo "--32--"
# comm=start
# comm=stop
# case "$comm" in
# 	start) echo "Starting..." ;;
# 	stop) echo "Stopping..." ;;
# 	restart) echo "Restarting..." ;;
# 	*) echo "Unknown command" ;;
# esac

#  To see all users
# cut -d: -f1 /etc/passwd

# To add a user named bob on Linux, run as root or with sudo:
# sudo useradd bob
# To also create a home directory for bob (recommended):
# sudo useradd -m bob
# To set a password for bob:
# sudo passwd bob

echo "--28--"
ps aux --sort=-%cpu | head -n 6

# chmod u+x file.txt  # add execute for owner
# chmod g-w file.txt  # remove write for group
# chmod o+r file.txt  # add read for others
# chmod a+r file.txt  # add read for everyone


# drwxr-x--- 2 vboxuser1 bob 4096 maj 8 10:26 bob

# d: type (d = directory, - = file)
# rwxr-x---: permissions (owner: rwx, group: r-x, others: ---)
# 2: number of hard links (directory entries)

# vboxuser1: owner (user)
# bob: group

# 4096: size in bytes (for directories, usually 4096)
# maj: month (Polish for May)
# 8: day
# 10:26: time of last modification
# bob: name of the file/directory

# To delete a user on Linux, use the userdel command as root or with sudo:
# sudo userdel username
# If you also want to remove the user’s home directory and mail spool:
# sudo userdel -r username
# ps -u username.