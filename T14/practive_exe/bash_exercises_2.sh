#!/bin/bash
# Bash Medium Level Exercises 2 (Tasks 1-20)

# Exercise 01
# Print the current date and time in the format YYYY-MM-DD HH:MM:SS.
echo "--1--"
date '+%F %T'


# Exercise 02
# List all files in the current directory, sorted by size (largest first).
echo "--2--"
ls -lS | grep '^-' 

# Exercise 03
# Print the number of lines in all .txt files in the current directory.
echo "--3--"
wc -l *.txt

# Exercise 04
# Find and print all files modified in the last 24 hours.
echo "--4--"
find . -type f -mtime -1

# Exercise 05
# Print the first 3 lines of every .log file in the current directory.
echo "--5--"
for f in *.log; do head -n 3 "$f"; done

# Exercise 06
# Replace all spaces with underscores in all .txt filenames in the current directory.
echo "--6--"
for f in *.txt; do mv "$f" "${f// /_}"; done

# Exercise 07
# Print the disk usage of the current directory in human-readable format.
echo "--7--"
du -sh .

# Exercise 08
# Print the usernames of all users currently logged in.
echo "--8--"
who | awk '{print $1}' | sort | uniq

# Exercise 09
# Print the number of running processes for your user.
echo "--9--"
ps -u "$USER" | wc -l

# Exercise 10
# Print the permissions of all .sh files in the current directory.
echo "--10--"
ls -l *.sh | awk '{print $1, $9}'

# Exercise 11
# Print the names of all subdirectories in the current directory.
echo "--11--"
find . -maxdepth 1 -type d | tail -n +2

# Exercise 12
# Print the last modified file in the current directory.
echo "--12--"
ls -t | head -n 1

# Exercise 13
# Print the sum of all numbers in a file called numbers.txt (one number per line).
echo "--13--"
awk '{s+=$1} END {print s}' numbers.txt

# Exercise 14
# Print all lines from file3.txt that contain the word ERROR.
echo "--14--"
grep ERROR file3.txt

# Exercise 15
# Print the number of files in the current directory and all subdirectories.
echo "--15--"
find . -type f | wc -l

# Exercise 16
# Print the name and size of the largest file in the current directory.
echo "--16--"
ls -lS | grep '^-' | head -n 1 | awk '{print $9, $5}'

# Exercise 17
# Print the number of unique words in file3.txt.
echo "--17--"
tr -s ' ' '\n' < file3.txt | sort | uniq | wc -l

# Exercise 18
# Print the lines from file3.txt that do not contain the word ERROR.
echo "--18--"
grep -v ERROR file3.txt

# Exercise 19
# Print the current user's home directory.
echo "--19--"
echo "$HOME"

# Exercise 20
# Print the names of all files in the current directory that are larger than 1MB.
echo "--20--"
find . -maxdepth 1 -type f -size +1M -exec ls -lh {} \; | awk '{print $9}'
# Exercise 21
# Use awk to print the second column from file1.txt.
echo "--21--"
awk '{print $2}' file1.txt

# Exercise 22
# Use sed to replace all occurrences of 'foo' with 'bar' in file2.txt.
echo "--22--"
sed 's/foo/bar/g' file2.txt

# Exercise 23
# Print the exit code of the last command.
echo "--23--"
echo $?

# Exercise 24
# Copy file1.txt to a remote server using scp (replace user@host with actual values).
echo "--24--"
# scp file1.txt user@host:/path/to/destination
echo "scp file1.txt user@host:/path/to/destination"

# Exercise 25
# Change permissions to make all .sh files executable.
echo "--25--"
chmod +x *.sh

# Exercise 26
# Change ownership of file2.txt to user 'bob' (requires sudo).
echo "--26--"
# sudo chown bob file2.txt
echo "sudo chown bob file2.txt"

# Exercise 27
# List all processes containing 'python'.
echo "--27--"
ps aux | grep python

# Exercise 28
# Show top 5 CPU-consuming processes.
echo "--28--"
ps aux --sort=-%cpu | head -n 6

# Exercise 29
# Kill a process with PID 1234.
echo "--29--"
# kill 1234
echo "kill 1234"

# Exercise 30
# Find all .log files in current and subdirectories.
echo "--30--"
find . -name "*.log"

# Exercise 31
# Use grep to find lines containing 'FAIL' in all .txt files.
echo "--31--"
grep FAIL *.txt

# Exercise 32
# Use a case statement to print a message based on $1 (start/stop/restart).
echo "--32--"
case "$1" in
	start) echo "Starting..." ;;
	stop) echo "Stopping..." ;;
	restart) echo "Restarting..." ;;
	*) echo "Unknown command" ;;
esac

# Exercise 33
# Print the current PATH variable.
echo "--33--"
echo "$PATH"

# Exercise 34
# Print the current HOME variable.
echo "--34--"
echo "$HOME"

# Exercise 35
# Print the current USER variable.
echo "--35--"
echo "$USER"

# Exercise 36
# Print the current working directory using PWD.
echo "--36--"
echo "$PWD"
