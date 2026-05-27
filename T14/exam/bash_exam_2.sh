#!/bin/bash

sol0() {
    :
    # File & Directory:
    #     ls, cd, pwd, mkdir, rmdir, cp, mv, rm, touch, find, locate, tree

    # Viewing & Editing:
    #     cat, less, more, head, tail, grep, sort, uniq, wc, nano/vi/vim

    # Permissions & Ownership:
    #     chmod, chown, chgrp, umask

    # Processes:
    #     ps, top, htop, kill, pkill, jobs, bg, fg, & (backgrounding)

    # System Info:
    #     uname, df, du, free, uptime, whoami, id, env, history

    # Networking:
    #     ping, ifconfig/ip, netstat, curl, wget, ssh, scp

    # Archiving:
    #     tar, gzip, gunzip, zip, unzip

    # Text Processing:
    #     awk, sed, cut, tr, paste, xargs

    # Scripting:
    #     Writing basic bash scripts, using variables, loops (for, while), if/else, functions

    # Package Management:
    #     apt, yum, dnf, pacman (depending on distro)

    # User Management:
    #     useradd, userdel, passwd, groups

    # Senior insight: Mastering pipes (|), redirection (>, >>, <),
    # and command substitution ($()) is key for combining commands efficiently.

    # Bash / Linux practice exam
    # Rules:
    # - Solve each task with the named command when possible.
    # - Add your commands below each exercise if you want to practice later.
    
}

# =========================
# File and directory commands
# =========================

# 1. ls - Exercise 1:
# Show all files in the current directory, including hidden ones, in long format.
sol1() {
    :
    ls -al
}


# 2. ls - Exercise 2:
# List files in a target directory sorted by size from largest to smallest.
sol2() {
    :
    ls -lS "${1:-.}" | grep '^-'
}

# 3. cd - Exercise 1:
# Move from your current directory into T14.
sol3() {
    :
    cd /home/mniedziolka/PP/Mat_test_repo/T14/
}

# 4. cd - Exercise 2:
# Move back to the previous directory without typing its full path again.
sol4() {
    :
    cd -
}

# 5. pwd - Exercise 1:
# Print the absolute path of your current working directory.
sol5() {
    :
    pwd
}

# 6. pwd - Exercise 2:
# Confirm that you are inside the expected project folder before running a script.
sol6() {
    :
    echo "➖➖➖➖➖➖➖➖➖"

    expected="/home/mniedziolka/PP/Mat_test_repo/T14/exam"
    if [[ "$(pwd)" == "$expected" ]]; then
        # "$(pwd)" means: run the pwd command first,
        # take its output, and use that output as a string.
        echo "Correct folder"
    else
        echo "Wrong folder"
    fi
    
    echo "➖➖➖➖➖➖➖➖➖"
    echo
}
# sol6

# 7. mkdir - Exercise 1:
# Create a directory named exam_practice.
sol7() {
    :
    mkdir exam_practice
}

# 8. mkdir - Exercise 2:
# Create nested directories logs/archive/2026 in one command.
# mkdir creates directories.
# -p is the main flag you will use most often.
# -m is useful when permissions matter from the start.
# -v helps while learning or debugging scripts.
sol8() {
    :
    mkdir -p logs/archive/2026
}
# sol8

# 9. rmdir - Exercise 1:
# Remove an empty directory named temp_empty.
sol9() {
    :
    rmdir temp_empty
}
# sol9

# 10. rmdir - Exercise 2:
# Remove two empty directories with one command.
sol10() {
    :
    rmdir temp_empty1 temp_empty2
}
# sol10

# 11. cp - Exercise 1:
# Copy file1.txt to file1_backup.txt.
sol11() {
    :
    # touch file1.txt
    cp file1.txt file1_backup.txt
}
# sol11

# 12. cp - Exercise 2:
# Copy all .sh files from one directory into another directory.
sol12() {
    :
    # for file in *.sh; do
    #     echo "$file"
    # done
    # for i in 1 2 3; do
    #     echo "$i"
    # done
    # mkdir sh_files
    for file in *.sh; do
        cp "$file" ./sh_files
    done

}
# sol12

# 13. mv - Exercise 1:
# Rename notes.txt to notes_old.txt.
sol13() {
    :
    # touch notes.txt
    mv notes.txt notes_old.txt

}
# sol13

# 14. mv - Exercise 2:
# Move all .log files into a directory named logs.
sol14() {
    :
    # for i in 1 2 3; do
    #     touch "log_file$i.log"
    # done
    for log_file in *.log; do
        mv "$log_file" ./logs
    done
}
# sol14

# 15. rm - Exercise 1:
# Remove a file named log_file1.log.
sol15() {
    :
    rm -f ./logs/log_file1.log
}
# sol15

# 16. rm - Exercise 2:
# Remove a directory with all its contents.
sol16() {
    :
    rm -rf ./logs/

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
}
# sol16

# 17. touch - Exercise 1:
# Create an empty file named todo.txt.
sol17() {
    :
    touch todo.txt
}

# 18. touch - Exercise 2:
# Create three empty files in one command.
sol18() {
    :
    touch ./sh_files/todo1.sh ./sh_files/todo2.txt ./sh_files/todo3.sh
}
# sol18

# 19. find - Exercise 1:
# Find all .sh files under the current directory.
sol19() {
    :
    find ./sh_files -type f -name "*.sh"
}
# sol19

# 20. find - Exercise 2:
# Find directories modified in the last 2 days.
sol20() {
    :
    find . -type d -mtime -2
}
# sol20

# 21. locate - Exercise 1:
# Search for a file named compose.yaml using the locate database.
sol21() {
    :
}

# 22. locate - Exercise 2:
# Find all paths containing the word jenkins.
sol22() {
    :
}

# 23. tree - Exercise 1:
# Show the directory tree of T14.
sol23() {
    :
    tree /home/mniedziolka/PP/Mat_test_repo/T14
}

# 24. tree - Exercise 2:
# Show only directories up to depth 2 in the current path.
sol24() {
    :
    tree -L 2
}

# =========================
# Viewing and reading files
# =========================

# 25. cat - Exercise 1:
# Display the full content of file1.txt.
sol25() {
    :
    cat file1.txt
}

# 26. cat - Exercise 2:
# Combine two text files and print them to standard output.
sol26() {
    :
    echo
    cat todo2.txt todo3.txt
    echo
}
# sol26

# 27. less - Exercise 1:
# Open a long text file and search for the word error.
sol27() {
    :
    less err.txt 
    less -N err.txt
}
# sol27

# 28. less - Exercise 2:
# Open a file and jump to the end of it for quick inspection.
sol28() {
    :
    # shift + G
}

# 29. more - Exercise 1:
# View a long file one screen at a time.
sol29() {
    :
    more err.txt
}

# 30. more - Exercise 2:
# Open a text file and move page by page through the output.
sol30() {
    :
    more err.txt
    # Press Space for next page
    # Press Enter for next line
    # Press q to quit
}
# sol30

# 31. head - Exercise 1:
# Show the first 5 lines of file2.txt.
sol31() {
    :
    head -n 5 file2.txt
}
# sol31

# 32. head - Exercise 2:
# Print the first 20 lines from every .log file in a directory.
sol32() {
    :
    for i in *.log; do
        printf "\n=== $i ===\n"
        head -n 20 "$i"
    done
}
# sol32

# 33. tail - Exercise 1:
# Show the last 10 lines of a log file.
sol33() {
    :
    tail -n 10 err.txt
}
# sol33
# 34. tail - Exercise 2:
# Follow a log file in real time as new lines are added.
sol34() {
    :
    # mkdir -p ./temp/
    # touch ./temp/null.txt
    # tail -n 10 -f err.txt &
    # APP_PID=$!
    # echo "new_line2" >> err.txt
    # kill "$APP_PID"
    # # It only asks the process to terminate. 
    # # It does not guarantee the process is already gone at the next line.
    # wait "$APP_PID" 1>./temp/null.txt || true
    # cat ./temp/null.txt
    tail -n 10 -f err.txt > ./temp/tail_out.txt &
    APP_PID=$!

    sleep 0.2
    echo "new_line2 $(date +%T)" >> err.txt
    sleep 0.2

    kill "$APP_PID"
    wait "$APP_PID" 2>./temp/wait_err.txt || true

    echo "=== wait stderr ==="
    cat ./temp/wait_err.txt
    echo "=== tail output ==="
    cat ./temp/tail_out.txt
    
}
# sol34

# 35. grep - Exercise 1:
# Search recursively for the word pytest in the current directory.
sol35() {
    :
    grep -R "pytest" .
}
# sol35

# 36. grep - Exercise 2:
# Print only lines that start with ERROR from a log file.
sol36() {
    :
    grep '^ERROR' ./*.log
}
# sol36

# 37. sort - Exercise 1:
# Sort the lines of names.txt alphabetically.
sol37() {
    :
    sort ./todo3.txt
}
# sol37

# 38. sort - Exercise 2:
# Sort a file of numbers from largest to smallest.
sol38() {
    :
    sort -nr ./todo4.txt
    # sort -r = strings,
    # sort -n = numbers,
    # sort -nr = numeric descending.
}
# sol38

# 39. uniq - Exercise 1:
# Remove duplicate adjacent lines from a sorted file.
sol39() {
    :
   sort ./todo2.txt | uniq
}
# sol39

# 40. uniq - Exercise 2:
# Count how many times each repeated line appears.
sol40() {
    :
    sort ./todo2.txt | uniq -c
}
# sol40

# 41. wc - Exercise 1:
# Count the number of lines in file3.txt.
sol41() {
    :
    wc -l ./todo2.txt
}
# sol41

# 42. wc - Exercise 2:
# Show the number of lines, words, and bytes in a file.
sol42() {
    :
    wc ./todo2.txt
}

# 43. nano - Exercise 1:
# Open a new file and write three short notes.
sol43() {
    :
}

# 44. nano - Exercise 2:
# Edit a script and save it under the same name.
sol44() {
    :

}

# 45. vim - Exercise 1:
# Open a file, add one new line, save, and quit.
sol45() {
    :

}

# 46. vim - Exercise 2:
# Search for a word inside a file and move to the next match.
sol46() {
    :

}

# =========================
# Permissions and ownership
# =========================

# 47. chmod - Exercise 1:
# Give the owner execute permission on script.sh.
sol47() {
    :
    chmod u+x script.sh
}

# 48. chmod - Exercise 2:
# Remove write permission for group and others from a file.
sol48() {
    :
    chmod g-w o-w script.sh

}

# 49. chown - Exercise 1:
# Change the owner of report.txt to bob.
sol49() {
    :
    chown bob report.txt

}

# 50. chown - Exercise 2:
# Change owner recursively for a directory and everything inside it.
sol50() {
    :
    chown -R bob dir/

}

# 51. chgrp - Exercise 1:
# Change the group of notes.txt to developers.
sol51() {
    :

}

# 52. chgrp - Exercise 2:
# Change the group recursively for a project directory.
sol52() {
    :

}

# 53. umask - Exercise 1:
# Display the current umask value.
sol53() {
    :

}

# 54. umask - Exercise 2:
# Temporarily set a umask so new files are not writable by group or others.
sol54() {
    :

}

# =========================
# Processes and jobs
# =========================

# 55. ps - Exercise 1:
# Show processes running for the current user.
sol55() {
    :
    ps -u "$(whoami)"
}

# 56. ps - Exercise 2:
# Display the top CPU-consuming processes in a sorted list.
sol56() {
    :
    ps aux --sort=-%cpu | head -n 5
    ps aux | sort -rn -k 3 | head -n 5
    ps aux | awk 'NR==1; NR>1 {print $0 | "sort -rn -k 3"}' | head -n 5
}

# 57. top - Exercise 1:
# Open a live process monitor and inspect CPU usage.
sol57() {
    :

}

# 58. top - Exercise 2:
# Sort running processes by memory usage while top is open.
sol58() {
    :
    # Shif + M (memory)
    # Shift + P (cpu)
    
}

# 59. htop - Exercise 1:
# Open htop and inspect processes for your user.
sol59() {
    :

}

# 60. htop - Exercise 2:
# Use htop to find a process consuming the most CPU.
sol60() {
    :

}

# 61. kill - Exercise 1:
# Stop a process by its PID using the default signal.
sol61() {
    :

}

# 62. kill - Exercise 2:
# Force stop a process that does not exit normally.
sol62() {
    :
    kill -9 '<PID>'
}

# 63. pkill - Exercise 1:
# Stop all processes with a given name.
sol63() {
    :

}

# 64. pkill - Exercise 2:
# Stop all processes owned by a specific user for one command name.
sol64() {
    :

}

# 65. jobs - Exercise 1:
# Show background and stopped jobs in the current shell.
sol65() {
    :

}

# 66. jobs - Exercise 2:
# Start a long command in the background and confirm it appears in jobs.
sol66() {
    :

}

# 67. bg - Exercise 1:
# Resume a stopped job in the background.
sol67() {
    :

}

# 68. bg - Exercise 2:
# Send the second stopped job to the background.
sol68() {
    :
    
}

# 69. fg - Exercise 1:
# Bring the most recent background job to the foreground.
sol69() {
    :
    
}

# 70. fg - Exercise 2:
# Bring a specific job number back to the foreground.
sol70() {
    :
    
}

# =========================
# System information
# =========================

# 71. uname - Exercise 1:
# Print the kernel name of your system.
sol71() {
    :
    uname
}

# 72. uname - Exercise 2:
# Show all available system information in one command.
sol72() {
    :
    uname -a
}

# 73. df - Exercise 1:
# Show disk usage for all mounted filesystems in human-readable format.
sol73() {
    :
    df -h
}

# 74. df - Exercise 2:
# Check disk usage only for the filesystem containing your home directory.
sol74() {
    :
    df -h /home/mniedziolka/
}

# 75. du - Exercise 1:
# Show the size of the current directory in human-readable format.
sol75() {
    :
    du -sh .
}

# 76. du - Exercise 2:
# Find the sizes of immediate subdirectories only.
sol76() {
    :
    du -h -d 1
    du -sh */
}

# 77. free - Exercise 1:
# Show memory usage in human-readable format.
sol77() {
    :
    free -h
}

# 78. free - Exercise 2:
# Display memory usage repeatedly with a short delay.
sol78() {
    :    
    free -h -s 1
}

# 79. uptime - Exercise 1:
# Show how long the system has been running.
sol79() {
    :
    uptime -p
}

# 80. uptime - Exercise 2:
# Check the current load average of the machine.
sol80() {
    :
    uptime
}

# 81. whoami - Exercise 1:
# Print the current username.
sol81() {
    :
    whoami
}

# 82. whoami - Exercise 2:
# Confirm which user is running a script before doing admin actions
sol82() {
    :
    echo "Running as: $(whoami)"
}

# 83. id - Exercise 1:
# Show your UID, GID, and groups.
sol83() {
    :
    id
}

# 84. id - Exercise 2:
# Print only the username of the current user.
sol84() {
    :
    id -un
}

# 85. env - Exercise 1:
# Print all environment variables.
sol85() {
    :
    env
}

# 86. env - Exercise 2:
# Check the values of PATH and HOME during a shell session.
sol86() {
    :
    env | grep 'HOME\|PATH'
}

# 87. history - Exercise 1:
# Show the last 20 commands from your shell history.
sol87() {
    :
    history | tail -n 20
}

# 88. history - Exercise 2:
# Find previous commands related to pytest or docker.
sol88() {
    :
    history | grep -Ei 'pytest|docker'
}

# =========================
# Networking
# =========================

# 89. ping - Exercise 1:
# Check whether google.com responds to network requests.
sol89() {
    :
    ping google.com
}

# 90. ping - Exercise 2:
# Send only 4 ping packets to a target host.
sol90() {
    :
    ping -c 4 google.com
}

# 91. ip - Exercise 1:
# Show all IP addresses assigned to your machine.
sol91() {
    :
    ip a
}

# 92. ip - Exercise 2:
# Display routing information for the system.
sol92() {
    :
    ip route
}

# 93. ifconfig - Exercise 1:
# Show network interface details on a system where ifconfig is available.
sol93() {
    :
    ifconfig
}

# 94. ifconfig - Exercise 2:
# Inspect a single network interface and read its IP address.
sol94() {
    :
    ifconfig | grep eth0
}

# 95. netstat - Exercise 1:
# Show listening TCP ports on the machine.
sol95() {
    :
    netstat -tln
}

# 96. netstat - Exercise 2:
# Display established network connections with numeric addresses.
sol96() {
    :
    netstat -atn | grep ESTABLISHED
}

# 97. curl - Exercise 1:
# Send a GET request to a public API endpoint.
sol97() {
    :
    curl "http://127.0.0.1:8000/users"
}

# 98. curl - Exercise 2:
# Download only the response headers from a URL.
sol98() {
    :

    # curl -I "http://127.0.0.1:8000/users" 
    # The -s (or --silent) flag tells curl to completely
    #  shut off its progress meter and error messages.
    # curl -s "http://127.0.0.1:8000/users" | jq

    curl -I "http://127.0.0.1:8000/users"
    # So when curl uses 2>, it isn't saying "An error occurred!"
    #  It is saying "Here is some diagnostic background noise about the download.
    #  I'm putting it over here so it doesn't mess up your actual data."

    #  -H "Content-Type: application/json": This header tells the server:
    #  "If I send you any data, it is going to be formatted as JSON."

    # -H "Accept: application/json": This header tells the server: 
    # "Please send your response back to me formatted as JSON."
}
# sol98

# 99. wget - Exercise 1:
# Download a file from a URL into the current directory.
sol99() {    
    :
    wget http://localhost:8121/m_file
}

# 100. wget - Exercise 2:
# Save a downloaded file under a custom name.
sol100() {
    :
    wget -O custom_name.txt http://localhost:8121/m_file

}
# sol100

# 101. ssh - Exercise 1:
# Connect to a remote host with a specific username.
sol101() {
    :
    ssh vboxuser1@192.168.0.152
}

# 102. ssh - Exercise 2:
# Run one remote command over SSH without opening an interactive shell.
sol102() {
    :
    sshpass -p "changeme1@" ssh vboxuser1@192.168.0.152 'pwd'
}

# 103. scp - Exercise 1:
# Copy a local file to a remote host.
sol103() {
    :
    sshpass -p "changeme1@" scp err.txt vboxuser1@192.168.0.152:/home/vboxuser1

}
# sol103

sol104() {
    :
    # 104. scp - Exercise 2:
    # Copy a remote directory to your local machine recursively.
    sshpass -p "changeme1@" scp -r vboxuser1@192.168.0.152:/home/vboxuser1/temp ./
}
# sol104

# =========================
# Archiving and compression
# =========================

# 105. tar - Exercise 1:
# Create an archive from a directory named project.
sol105() {
    :
    tar -cvf tartar.tar ./temp
    # -c: Creates a new archive.
    # -v: Verbose mode (optional, but helpful).
    #   It lists all the files as they are being added to the archive.
    # -f: Allows you to specify the filename of the archive (project.tar).
    #    Note: This flag must always be the last one before the file name.
}
# sol105

# 106. tar - Exercise 2:
# Extract an existing tar archive into a target directory.
sol106() {
    :
    # mkdir ./tarFiles/
    tar -xvf tartar.tar --directory ./tarFiles/
}   
# sol106

# 107. gzip - Exercise 1:
# Compress a file named big.log.
sol107() {
    :
    gzip big.log

}
# sol107

# 108. gzip - Exercise 2:
# Compress every .txt file in the current directory.
sol108() {
    :
    # You actually only really need the gzip command. gunzip is 
    # literally just a shortcut for running gzip with the -d (decompress) flag.
    gzip ./*.txt
}
# sol108

# 109. gunzip - Exercise 1:
# Decompress a file named report.txt.gz.
sol109() {
    :
    gunzip report.txt.gz
}

# 110. gunzip - Exercise 2:
# Decompress all .gz files in one directory.
sol110() {
    :
    for file in *.gz; do
        gunzip $file
    done
}

# 111. zip - Exercise 1:
# Create a zip archive from two text files.
sol111() {
    :
    zip archive.zip file1.txt file2.txt

}
# sol111

# 112. zip - Exercise 2:
# Create a recursive zip archive of a whole directory.
sol112() {
    :

    zip -r directory.zip ./temp
}
# sol112

# 113. unzip - Exercise 1:
# Extract archive.zip into the current directory.
sol113() {
    :
    unzip archive.zip
}
# sol113

# 114. unzip - Exercise 2:
# Extract an archive into a directory named extracted_files.
sol114() {
    :
    unzip archive.zip -d extracted_files
}

# =========================
# Text processing
# =========================
# 115. awk - Exercise 1:
# Print the first and third columns from a text file.
sol115() {
    :
    awk '{print $1, $3}' columns.txt
}
# sol115

# 116. awk - Exercise 2:
# Print only the second line of a file.
sol116() {
    :
    awk 'NR == 2 {print; exit}' columns.txt
}
# sol116

# 117. sed - Exercise 1:
# Replace every occurrence of foo with bar in a file output.
sol117() {
    :
    sed 's/foo/bar/g' foobar.txt
}
# sol117

# 118. sed - Exercise 2:
# Print only lines 5 to 10 from a file.
sol118() {
    :
    # sed -n '5,10p' foobar.txt
    head -n 10 foobar.txt | tail -n +5 
    # This first grabs the top 10 lines of the file.
    # |
    # to output everything starting from the 5th line of the chunk it just received.
}
# sol118

# 119. cut - Exercise 1:
# Print the first field from /etc/passwd using : as the delimiter.
sol119() {
    :
    cut -d ':' -f 1 /etc/passwd
    # -d ':': Specifies the delimiter (the character that separates the columns).
    #  In this case, it is a colon.

    # -f 1: Specifies the field (column) number you want to extract. 
    # Field 1 in /etc/passwd corresponds to the usernames.
    # -F':': This is the awk way of setting the Field separator (the delimiter).

}
# sol119

# 120. cut - Exercise 2:
# Extract characters 1 to 5 from every line in a file.
sol120() {
    :
    cut -c 1-5 foobar.txt
}
# sol120

# 121. tr - Exercise 1:
# Convert lowercase letters to uppercase from standard input.
sol121() {
    :
    echo "sdsfsd" | tr 'a-z' 'A-Z'
}
# sol121


# 122. tr - Exercise 2:
# Delete all digits from a text stream.
sol122() {
    :
    echo "s2dsf3sd" | tr -d '0-9'
}
# sol122

# 123. paste - Exercise 1:
# Merge two files side by side line by line.
sol123() {
    :
    paste foobar.txt log.txt
}
# sol123

# 124. paste - Exercise 2:
# Join two files using a custom delimiter.
sol124() {
    :
    paste -d '|' foobar.txt log.txt
}
# sol124

# 125. xargs - Exercise 1:
# Read a list of filenames from standard input and remove them.
sol125() {
    :
    xargs rm
}

# 126. xargs - Exercise 2:
# Use find and xargs together to count lines in multiple files.
sol126() {
    :
    find . -name "*.log" -print0 | xargs -0 wc -l
    # find . -name "*.log" | rm # rm: missing operand
    # 
    # find . -name "*.log" | xargs rm
    # 
    # How it fixes it: xargs captures the list of .log files coming from find and 
    # reformats them as arguments, effectively running: 
    # rm ./setup.log ./error.log ./app.log.
    # 
    # Instead of a vertical stream of data flowing down a pipe, xargs flattens that
    # data into a horizontal line of arguments attached to the back of your target command.
    # find . -name "*.csv" | xargs -P 4 gzip
    # 
    # echo "file1 file2 file3 file4" | xargs -n 2 rm
    #   rm file1 file2   
    #   rm file3 file4 
    # 
    # find . -name "*.txt" | xargs -p rm
    # find . -name "*.txt" -print0 | xargs -0 rm
    #   -print0 tells find to separate files using a hidden null
    #   character (\0) instead of spaces.
    #   -0 tells xargs to look for those null characters,
    #   perfectly preserving filenames that contain spaces.



}
# sol126

# =========================
# Package management
# =========================

sol127() {
    :
    # 127. apt - Exercise 1:
    # Refresh package lists on a Debian-based system.
    sudo apt update
    # sudo apt upgrade         # Upgrades all installed packages to newer versions
    # sudo apt full-upgrade    # Upgrades packages, handling changing dependencies
    # sudo apt install <pkg>   # Downloads and installs a specific package
    # sudo apt remove <pkg>    # Uninstalls a package but keeps its config files
    # sudo apt purge <pkg>     # Completely removes a package and its config files
    # apt search <keyword>     # Searches package names and descriptions for a term
    # apt show <pkg>           # Displays detailed information about a package
    # apt list --installed     # Lists all packages currently installed on the system
    # sudo apt autoremove      # Removes leftover dependencies no longer needed
    # sudo apt clean           # Clears cached installer files to free up disk space
}

sol128() {
    :
    # 128. apt - Exercise 2:
    # Install one package and then inspect whether it is installed.
    sudo apt install -y tree && apt list --installed | grep '^tree/'
}

sol129() {
    :
    # 129. yum - Exercise 1:
    # Install a package on a yum-based system.
    sudo yum install -y tree
}

sol130() {
    :
    # 130. yum - Exercise 2:
    # Search for packages matching the word docker.
    yum search docker
}

sol131() {
    :
    # 131. dnf - Exercise 1:
    # Update package metadata on a dnf-based system.
    sudo dnf makecache
}

sol132() {
    :
    # 132. dnf - Exercise 2:
    # Remove a package that is no longer needed.
    sudo dnf remove -y tree
}

sol133() {
    :
    # 133. pacman - Exercise 1:
    # Synchronize package databases on an Arch-based system.
    sudo pacman -Sy
}

sol134() {
    :
    # 134. pacman - Exercise 2:
    # Install a package and check its files.
    sudo pacman -S --noconfirm tree && pacman -Ql tree
}

# =========================
# User management
# =========================

# 135. useradd - Exercise 1:
# Create a new user named trainee.
sol135() {
    :
    sudo useradd -m trainee

}

# 136. useradd - Exercise 2:
# Create a new user with a home directory and a specific shell.
sol136() {
    sudo useradd -m -s "$2" "$1"
    # How It Works
    # sudo: Creating new user accounts requires root privileges.
    # useradd: The standard low-level utility for creating new users.
    # -m (or --create-home): Forces the system to create the user's 
    #     home directory (usually /home/username) if it doesn't
    #     already exist, and copies skeleton files (like .bashrc) into it.
    # -s "$2" (or --shell): Sets the path to the user's default
    #      login shell (e.g., /bin/bash, /bin/zsh, or /bin/sh).
}
# sol136 newuser /bin/bash

# 137. userdel - Exercise 1:
# Remove a user named trainee.
sol137() {
    :
    sudo userdel trainee

}

# 138. userdel - Exercise 2:
# Remove a user together with the home directory.
sol138() {
    :
    # echo "$1"
    sudo userdel -r "$1"
    
}
# sol138 "mamama"

# 139. passwd - Exercise 1:
# Set a password for a newly created user.
sol139() {
    :
    sudo passwd Bob
}

# 140. passwd - Exercise 2:
# Expire a user's password and force a change on next login if your system supports it.
sol140() {
    :
    sudo passwd -e "root"
}

# 141. groups - Exercise 1:
# Show all groups for the current user.
sol141() {
    :
    groups
}

# 142. groups - Exercise 2:
# Check which groups a target user belongs to.
sol142() {
    :
    groups "root"
    # id -Gn "$1"
}
# sol142

# =========================
# Core shell skills
# =========================

# 143. pipes | - Exercise 1:
# Count how many .txt files exist under the current directory using a pipeline.
sol143() {
    find . -type f -name "*.txt" | wc -l

    # If you happen to have file names that contain actual
    # newline characters (which is rare but technically possible in Linux),
    # the solution above might slightly overcount. If you want to make
    # it 100% bulletproof against weird filenames, you can use this advanced variation:
    find . -type f -name "*.txt" -printf '.' | wc -c
}
# sol143

# 144. pipes | - Exercise 2:
# Show unique logged-in usernames in sorted order using multiple commands.
sol144() {
    :
    # Show unique logged-in usernames in sorted order
    # who | awk '{print $1}' | sort | uniq
    # ps -eo pid,user,pcpu,pmem,comm --sort=-pcpu | head -n 6
    who | awk '{print $1}' | sort | uniq
}
# sol144

# 
# 145. redirection > and >> - Exercise 1:
# Save the output of ls -l into a new file.
sol145() {
    :
    ls -l > log1.txt
}
# sol145

# 146. redirection > and >> - Exercise 2:
# Append the current date to an existing log file.
sol146() {
    :
    date >> log.txt

}
# sol146

# 147. input redirection < - Exercise 1:
# Pass a file into a command that can read from standard input.
sol147() {
    :
    wc -l < todo1.txt
}
# sol147

# 148. input redirection < - Exercise 2:
# Compare behavior of a command with direct filename input versus input redirection.
sol148() {
    :

    file="todo1.txt"
    if [[ ! -f "$file" ]]; then
        printf "line1\nline2\nline3\n" > "$file"
    fi

    # echo "Direct filename input (wc reads from file argument):"
    # wc -l "$file"

    # echo "Input redirection (wc reads from stdin):"
    # wc -l < "$file"
    # < "$file"
    # cat "$file"
    # cat < "$file"
    # awk 'END {print "lines=" NR, "source=" FILENAME}' "$file"
    awk 'END {print "lines=" NR, "source=" FILENAME}' < "$file"
    # Each part:
    # awk
    # The tool that processes text line by line.
    # '...'
    # Single quotes protect the awk program from shell expansion.
    # Without single quotes, shell could break special chars like { }, $.
    # END
    # A special awk block.
    # Runs once, after all input is fully read.
    # { ... }
    # Action block (what to do when END runs).
    # print
    # Outputs values to stdout.
    # "lines="
    # Literal text string.
    # NR
    # Built-in awk variable: total number of records read.
    # With default settings, one record = one input line.
    # "source="
    # Another literal text string.
    # FILENAME
    # Built-in awk variable: current input file name.
    # If input comes from redirection (example: < file), often shows as -.

}
# sol148

# 149. command substitution $() - Exercise 1:
# Store the current date in a variable using command substitution.
sol149() {
    :
    date1=$(date)
    echo "Now is: $date1"

}
# sol149

# 150. command substitution $() - Exercise 2:
# Build a filename that contains the current username.
sol150() {
    :
    touch ${USER}_file1.txt
}
# sol150

# 151. variables - Exercise 1:
# Create a variable with a directory path and use it in a command.
sol151() {
    :
    path=$(pwd)
    echo "This is my path: $path"
}
# sol151

# 152. variables - Exercise 2:
# Print two variables inside one sentence.
sol152() {
    :
    var1=1
    var2="Bobby"
    echo "$var2 has $var1"

}
# sol152

# 153. if / else - Exercise 1:
# Check whether a file exists and print one message if it does and another if it does not.
sol153() {
    :
    if [[ -f "todo23.txt" ]]; then
        echo "FILE exists"
    else
        echo "FILE does not exist"
    fi
}
# sol153

# 154. if / else - Exercise 2:
# Check whether the current user is root before running an admin command.
sol154() {
    :
    if [[ $USER == root ]]; then
        echo "run admin command"
    else
        echo "You're not admin"
    fi

}
# sol154

# 155. for loop - Exercise 1:
# Loop through all .txt files and print each filename.
sol155() {
    :
    for file in *.txt; do
        echo ${file}
    done
}
# sol155

# 156. for loop - Exercise 2:
# Loop through numbers 1 to 5 and create files based on those numbers.
sol156() {
    :
    for i in 1 2 3 4 5; do
        touch ${i}_file.txt
    done
}
# sol156

# 157. while loop - Exercise 1:
# Print the current time every second for five iterations.
sol157() {
    :
    CC=5
    while [[ $CC -gt 0 ]]; do
        date 
        sleep 1
        CC=$((CC-1))
    done 
}
# sol157

# 158. while loop - Exercise 2:
# Read a file line by line and print each line with a prefix.
sol158() {
    :
    # CC=5
    # while [[ $CC -gt 0 ]]; do
    #     echo "$CC"
    #     sleep 0.2
    #     CC=$((CC-1))
    # done
    # Read todo1.txt safely line by line, preserving leading/trailing spaces and backslashes.
    while read -r line; do
        echo "PREFIX|$line"
    done < todo1.txt
}
# sol158

# 159. functions - Exercise 1:
# Write a function that prints a separator line.
sol159() {
    :
    echo "==="
}
# sol159

# 160. functions - Exercise 2:
# Write a function that accepts one filename argument and checks whether it exists.
file=todo1.txt
sol160() {
    :
    if [[ -f "$1" ]]; then
        echo "FILE EXISTS"
    else
        echo "FILE DOES NOT EXIST"
    fi
    
}
# sol160

echo

