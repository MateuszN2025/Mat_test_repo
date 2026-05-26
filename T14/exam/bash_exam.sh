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
    ls -lS | grep '^-'
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
    cd ..
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
    mkdir -p temp_empty1 temp_empty2
}
# sol8

# 9. rmdir - Exercise 1:
# Remove an empty directory named temp_empty.
sol9() {
    :
    rm -r temp_empty
}
# sol9

# 10. rmdir - Exercise 2:
# Remove two empty directories with one command.
sol10() {
    :
    rm -r temp_empty1 temp_empty2
}
# sol10

# 11. cp - Exercise 1:
# Copy file1.txt to file1_backup.txt.
sol11() {
    :
    # touch file1.txt
    cp file1.txt file3_backup.sh
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
        cp $file ./sh_files
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
    # rm -f ./sh_files/*.sh
    # rm -r ./logs/
    # pwd
    for file in *.*; do
        if [[ "$file" != "bash_exam.sh" ]]; then
            rm -f $file
        fi
    done

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
    cat todo1.txt
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
    head -5 err.txt
}
# sol31

# 32. head - Exercise 2:
# Print the first 20 lines from every .log file in a directory.
sol32() {
    :
    for i in *.*; do
        printf "\n=== $i ===\n"
        nl -ba $i | head -5
    done
}
# sol32

# 33. tail - Exercise 1:
# Show the last 10 lines of a log file.
sol33() {
    :
    nl -ba err.txt | tail -10 
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
    grep -r PYTEST .
}
# sol35

# 36. grep - Exercise 2:
# Print only lines that start with ERROR from a log file.
sol36() {
    :
    grep -i ERROR ./todo3*
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
    chown report.txt bob

}

# 50. chown - Exercise 2:
# Change owner recursively for a directory and everything inside it.
sol50() {
    :
    chown -r dir/ bob

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
    ps -u root
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
    du -sh /home/mniedziolka/
}

# 76. du - Exercise 2:
# Find the sizes of immediate subdirectories only.
sol76() {
    :
    du -h -d 1
    du -sh */
}

sol77() {
    :
    # 77. free - Exercise 1:
    # Show memory usage in human-readable format.
}

sol78() {
    :
    # 78. free - Exercise 2:
    # Display memory usage repeatedly with a short delay.
}

sol79() {
    :
    # 79. uptime - Exercise 1:
    # Show how long the system has been running.
}

sol80() {
    :
    # 80. uptime - Exercise 2:
    # Check the current load average of the machine.
}

sol81() {
    :
    # 81. whoami - Exercise 1:
    # Print the current username.
}

sol82() {
    :
    # 82. whoami - Exercise 2:
    # Confirm which user is running a script before doing admin actions.
}

sol83() {
    :
    # 83. id - Exercise 1:
    # Show your UID, GID, and groups.
}

sol84() {
    :
    # 84. id - Exercise 2:
    # Print only the username of the current user.
}

sol85() {
    :
    # 85. env - Exercise 1:
    # Print all environment variables.
}

sol86() {
    :
    # 86. env - Exercise 2:
    # Check the values of PATH and HOME during a shell session.
}

sol87() {
    :
    # 87. history - Exercise 1:
    # Show the last 20 commands from your shell history.
}

sol88() {
    :
    # 88. history - Exercise 2:
    # Find previous commands related to pytest or docker.
}

# =========================
# Networking
# =========================

sol89() {
    :
    # 89. ping - Exercise 1:
    # Check whether google.com responds to network requests.
}

sol90() {
    :
    # 90. ping - Exercise 2:
    # Send only 4 ping packets to a target host.
}

sol91() {
    :
    # 91. ip - Exercise 1:
    # Show all IP addresses assigned to your machine.
}

sol92() {
    :
    # 92. ip - Exercise 2:
    # Display routing information for the system.
}

sol93() {
    :
    # 93. ifconfig - Exercise 1:
    # Show network interface details on a system where ifconfig is available.
}

sol94() {
    :
    # 94. ifconfig - Exercise 2:
    # Inspect a single network interface and read its IP address.
}

sol95() {
    :
    # 95. netstat - Exercise 1:
    # Show listening TCP ports on the machine.
}

sol96() {
    :
    # 96. netstat - Exercise 2:
    # Display established network connections with numeric addresses.
}

sol97() {
    :
    # 97. curl - Exercise 1:
    # Send a GET request to a public API endpoint.
}

sol98() {
    :
    # 98. curl - Exercise 2:
    # Download only the response headers from a URL.
}

sol99() {
    :
    # 99. wget - Exercise 1:
    # Download a file from a URL into the current directory.
}

sol100() {
    :
    # 100. wget - Exercise 2:
    # Save a downloaded file under a custom name.
}

sol101() {
    :
    # 101. ssh - Exercise 1:
    # Connect to a remote host with a specific username.
}

sol102() {
    :
    # 102. ssh - Exercise 2:
    # Run one remote command over SSH without opening an interactive shell.
}

sol103() {
    :
    # 103. scp - Exercise 1:
    # Copy a local file to a remote host.
}

sol104() {
    :
    # 104. scp - Exercise 2:
    # Copy a remote directory to your local machine recursively.
}

# =========================
# Archiving and compression
# =========================

sol105() {
    :
    # 105. tar - Exercise 1:
    # Create an archive from a directory named project.
}

sol106() {
    :
    # 106. tar - Exercise 2:
    # Extract an existing tar archive into a target directory.
}

sol107() {
    :
    # 107. gzip - Exercise 1:
    # Compress a file named big.log.
}

sol108() {
    :
    # 108. gzip - Exercise 2:
    # Compress every .txt file in the current directory.
}

sol109() {
    :
    # 109. gunzip - Exercise 1:
    # Decompress a file named report.txt.gz.
}

sol110() {
    :
    # 110. gunzip - Exercise 2:
    # Decompress all .gz files in one directory.
}

sol111() {
    :
    # 111. zip - Exercise 1:
    # Create a zip archive from two text files.
}

sol112() {
    :
    # 112. zip - Exercise 2:
    # Create a recursive zip archive of a whole directory.
}

sol113() {
    :
    # 113. unzip - Exercise 1:
    # Extract archive.zip into the current directory.
}

sol114() {
    :
    # 114. unzip - Exercise 2:
    # Extract an archive into a directory named extracted_files.
}

# =========================
# Text processing
# =========================

sol115() {
    :
    # 115. awk - Exercise 1:
    # Print the first and third columns from a text file.
}

sol116() {
    :
    # 116. awk - Exercise 2:
    # Print only the second line of a file.
}

sol117() {
    :
    # 117. sed - Exercise 1:
    # Replace every occurrence of foo with bar in a file output.
}

sol118() {
    :
    # 118. sed - Exercise 2:
    # Print only lines 5 to 10 from a file.
}

sol119() {
    :
    # 119. cut - Exercise 1:
    # Print the first field from /etc/passwd using : as the delimiter.
}

sol120() {
    :
    # 120. cut - Exercise 2:
    # Extract characters 1 to 5 from every line in a file.
}

sol121() {
    :
    # 121. tr - Exercise 1:
    # Convert lowercase letters to uppercase from standard input.
}

sol122() {
    :
    # 122. tr - Exercise 2:
    # Delete all digits from a text stream.
}

sol123() {
    :
    # 123. paste - Exercise 1:
    # Merge two files side by side line by line.
}

sol124() {
    :
    # 124. paste - Exercise 2:
    # Join two files using a custom delimiter.
}

sol125() {
    :
    # 125. xargs - Exercise 1:
    # Read a list of filenames from standard input and remove them.
}

# 126. xargs - Exercise 2:
# Use find and xargs together to count lines in multiple files.
sol126() {
    :
    echo 126
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
sol126

# =========================
# Package management
# =========================

sol127() {
    :
    # 127. apt - Exercise 1:
    # Refresh package lists on a Debian-based system.
    sudo apt update          # Updates the local list of available packages
    sudo apt upgrade         # Upgrades all installed packages to newer versions
    sudo apt full-upgrade    # Upgrades packages, handling changing dependencies
    sudo apt install <pkg>   # Downloads and installs a specific package
    sudo apt remove <pkg>    # Uninstalls a package but keeps its config files
    sudo apt purge <pkg>     # Completely removes a package and its config files
    apt search <keyword>     # Searches package names and descriptions for a term
    apt show <pkg>           # Displays detailed information about a package
    apt list --installed     # Lists all packages currently installed on the system
    sudo apt autoremove      # Removes leftover dependencies no longer needed
    sudo apt clean           # Clears cached installer files to free up disk space
}

sol128() {
    :
    # 128. apt - Exercise 2:
    # Install one package and then inspect whether it is installed.
}

sol129() {
    :
    # 129. yum - Exercise 1:
    # Install a package on a yum-based system.
}

sol130() {
    :
    # 130. yum - Exercise 2:
    # Search for packages matching the word docker.
}

sol131() {
    :
    # 131. dnf - Exercise 1:
    # Update package metadata on a dnf-based system.
}

sol132() {
    :
    # 132. dnf - Exercise 2:
    # Remove a package that is no longer needed.
}

sol133() {
    :
    # 133. pacman - Exercise 1:
    # Synchronize package databases on an Arch-based system.
}

sol134() {
    :
    # 134. pacman - Exercise 2:
    # Install a package and check its files.
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
    ps -eo pid=PID,user=USER,pcpu=%CPU,pmem=%MEM,comm=COMM --sort=-pcpu | head -n 6
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
    # Heredoc: pass multi-line Python code to stdin.
    # Call with: sol147 < todo1.txt
    python3 << 'EOF'
print("hello")
EOF
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
    if [[ -f $file ]]; then
        echo "FILE EXISTS"
    else
        echo "FILE DOES NOT EXIST"
    fi
    
}
# sol160

echo

