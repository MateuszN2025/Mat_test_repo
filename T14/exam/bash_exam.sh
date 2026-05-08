#!/bin/bash

# Bash / Linux practice exam
# Rules:
# - Solve each task with the named command when possible.
# - Do not write solutions here.
# - Add your commands below each exercise if you want to practice later.

# =========================
# File and directory commands
# =========================

# ls - Exercise 1:
# Show all files in the current directory, including hidden ones, in long format.
# ls - Exercise 2:
# List files in a target directory sorted by size from largest to smallest.

# cd - Exercise 1:
# Move from your current directory into T14.
# cd - Exercise 2:
# Move back to the previous directory without typing its full path again.

# pwd - Exercise 1:
# Print the absolute path of your current working directory.
# pwd - Exercise 2:
# Confirm that you are inside the expected project folder before running a script.

# mkdir - Exercise 1:
# Create a directory named exam_practice.
# mkdir - Exercise 2:
# Create nested directories logs/archive/2026 in one command.

# rmdir - Exercise 1:
# Remove an empty directory named temp_empty.
# rmdir - Exercise 2:
# Remove two empty directories with one command.

# cp - Exercise 1:
# Copy file1.txt to file1_backup.txt.
# cp - Exercise 2:
# Copy all .sh files from one directory into another directory.

# mv - Exercise 1:
# Rename notes.txt to notes_old.txt.
# mv - Exercise 2:
# Move all .log files into a directory named logs.

# rm - Exercise 1:
# Remove a file named old_report.txt.
# rm - Exercise 2:
# Remove a directory with all its contents.

# touch - Exercise 1:
# Create an empty file named todo.txt.
# touch - Exercise 2:
# Create three empty files in one command.

# find - Exercise 1:
# Find all .sh files under the current directory.
# find - Exercise 2:
# Find directories modified in the last 2 days.

# locate - Exercise 1:
# Search for a file named compose.yaml using the locate database.
# locate - Exercise 2:
# Find all paths containing the word jenkins.

# tree - Exercise 1:
# Show the directory tree of T14.
# tree - Exercise 2:
# Show only directories up to depth 2 in the current path.

# =========================
# Viewing and reading files
# =========================

# cat - Exercise 1:
# Display the full content of file1.txt.
# cat - Exercise 2:
# Combine two text files and print them to standard output.

# less - Exercise 1:
# Open a long text file and search for the word error.
# less - Exercise 2:
# Open a file and jump to the end of it for quick inspection.

# more - Exercise 1:
# View a long file one screen at a time.
# more - Exercise 2:
# Open a text file and move page by page through the output.

# head - Exercise 1:
# Show the first 5 lines of file2.txt.
# head - Exercise 2:
# Print the first 20 lines from every .log file in a directory.

# tail - Exercise 1:
# Show the last 10 lines of a log file.
# tail - Exercise 2:
# Follow a log file in real time as new lines are added.

# grep - Exercise 1:
# Search recursively for the word pytest in the current directory.
# grep - Exercise 2:
# Print only lines that start with ERROR from a log file.

# sort - Exercise 1:
# Sort the lines of names.txt alphabetically.
# sort - Exercise 2:
# Sort a file of numbers from largest to smallest.

# uniq - Exercise 1:
# Remove duplicate adjacent lines from a sorted file.
# uniq - Exercise 2:
# Count how many times each repeated line appears.

# wc - Exercise 1:
# Count the number of lines in file3.txt.
# wc - Exercise 2:
# Show the number of lines, words, and bytes in a file.

# nano - Exercise 1:
# Open a new file and write three short notes.
# nano - Exercise 2:
# Edit a script and save it under the same name.

# vim - Exercise 1:
# Open a file, add one new line, save, and quit.
# vim - Exercise 2:
# Search for a word inside a file and move to the next match.

# =========================
# Permissions and ownership
# =========================

# chmod - Exercise 1:
# Give the owner execute permission on script.sh.
# chmod - Exercise 2:
# Remove write permission for group and others from a file.

# chown - Exercise 1:
# Change the owner of report.txt to bob.
# chown - Exercise 2:
# Change owner recursively for a directory and everything inside it.

# chgrp - Exercise 1:
# Change the group of notes.txt to developers.
# chgrp - Exercise 2:
# Change the group recursively for a project directory.

# umask - Exercise 1:
# Display the current umask value.
# umask - Exercise 2:
# Temporarily set a umask so new files are not writable by group or others.

# =========================
# Processes and jobs
# =========================

# ps - Exercise 1:
# Show processes running for the current user.
# ps - Exercise 2:
# Display the top CPU-consuming processes in a sorted list.

# top - Exercise 1:
# Open a live process monitor and inspect CPU usage.
# top - Exercise 2:
# Sort running processes by memory usage while top is open.

# htop - Exercise 1:
# Open htop and inspect processes for your user.
# htop - Exercise 2:
# Use htop to find a process consuming the most CPU.

# kill - Exercise 1:
# Stop a process by its PID using the default signal.
# kill - Exercise 2:
# Force stop a process that does not exit normally.

# pkill - Exercise 1:
# Stop all processes with a given name.
# pkill - Exercise 2:
# Stop all processes owned by a specific user for one command name.

# jobs - Exercise 1:
# Show background and stopped jobs in the current shell.
# jobs - Exercise 2:
# Start a long command in the background and confirm it appears in jobs.

# bg - Exercise 1:
# Resume a stopped job in the background.
# bg - Exercise 2:
# Send the second stopped job to the background.

# fg - Exercise 1:
# Bring the most recent background job to the foreground.
# fg - Exercise 2:
# Bring a specific job number back to the foreground.

# =========================
# System information
# =========================

# uname - Exercise 1:
# Print the kernel name of your system.
# uname - Exercise 2:
# Show all available system information in one command.

# df - Exercise 1:
# Show disk usage for all mounted filesystems in human-readable format.
# df - Exercise 2:
# Check disk usage only for the filesystem containing your home directory.

# du - Exercise 1:
# Show the size of the current directory in human-readable format.
# du - Exercise 2:
# Find the sizes of immediate subdirectories only.

# free - Exercise 1:
# Show memory usage in human-readable format.
# free - Exercise 2:
# Display memory usage repeatedly with a short delay.

# uptime - Exercise 1:
# Show how long the system has been running.
# uptime - Exercise 2:
# Check the current load average of the machine.

# whoami - Exercise 1:
# Print the current username.
# whoami - Exercise 2:
# Confirm which user is running a script before doing admin actions.

# id - Exercise 1:
# Show your UID, GID, and groups.
# id - Exercise 2:
# Print only the username of the current user.

# env - Exercise 1:
# Print all environment variables.
# env - Exercise 2:
# Check the values of PATH and HOME during a shell session.

# history - Exercise 1:
# Show the last 20 commands from your shell history.
# history - Exercise 2:
# Find previous commands related to pytest or docker.

# =========================
# Networking
# =========================

# ping - Exercise 1:
# Check whether google.com responds to network requests.
# ping - Exercise 2:
# Send only 4 ping packets to a target host.

# ip - Exercise 1:
# Show all IP addresses assigned to your machine.
# ip - Exercise 2:
# Display routing information for the system.

# ifconfig - Exercise 1:
# Show network interface details on a system where ifconfig is available.
# ifconfig - Exercise 2:
# Inspect a single network interface and read its IP address.

# netstat - Exercise 1:
# Show listening TCP ports on the machine.
# netstat - Exercise 2:
# Display established network connections with numeric addresses.

# curl - Exercise 1:
# Send a GET request to a public API endpoint.
# curl - Exercise 2:
# Download only the response headers from a URL.

# wget - Exercise 1:
# Download a file from a URL into the current directory.
# wget - Exercise 2:
# Save a downloaded file under a custom name.

# ssh - Exercise 1:
# Connect to a remote host with a specific username.
# ssh - Exercise 2:
# Run one remote command over SSH without opening an interactive shell.

# scp - Exercise 1:
# Copy a local file to a remote host.
# scp - Exercise 2:
# Copy a remote directory to your local machine recursively.

# =========================
# Archiving and compression
# =========================

# tar - Exercise 1:
# Create an archive from a directory named project.
# tar - Exercise 2:
# Extract an existing tar archive into a target directory.

# gzip - Exercise 1:
# Compress a file named big.log.
# gzip - Exercise 2:
# Compress every .txt file in the current directory.

# gunzip - Exercise 1:
# Decompress a file named report.txt.gz.
# gunzip - Exercise 2:
# Decompress all .gz files in one directory.

# zip - Exercise 1:
# Create a zip archive from two text files.
# zip - Exercise 2:
# Create a recursive zip archive of a whole directory.

# unzip - Exercise 1:
# Extract archive.zip into the current directory.
# unzip - Exercise 2:
# Extract an archive into a directory named extracted_files.

# =========================
# Text processing
# =========================

# awk - Exercise 1:
# Print the first and third columns from a text file.
# awk - Exercise 2:
# Print only the second line of a file.

# sed - Exercise 1:
# Replace every occurrence of foo with bar in a file output.
# sed - Exercise 2:
# Print only lines 5 to 10 from a file.

# cut - Exercise 1:
# Print the first field from /etc/passwd using : as the delimiter.
# cut - Exercise 2:
# Extract characters 1 to 5 from every line in a file.

# tr - Exercise 1:
# Convert lowercase letters to uppercase from standard input.
# tr - Exercise 2:
# Delete all digits from a text stream.

# paste - Exercise 1:
# Merge two files side by side line by line.
# paste - Exercise 2:
# Join two files using a custom delimiter.

# xargs - Exercise 1:
# Read a list of filenames from standard input and remove them.
# xargs - Exercise 2:
# Use find and xargs together to count lines in multiple files.

# =========================
# Package management
# =========================

# apt - Exercise 1:
# Refresh package lists on a Debian-based system.
# apt - Exercise 2:
# Install one package and then inspect whether it is installed.

# yum - Exercise 1:
# Install a package on a yum-based system.
# yum - Exercise 2:
# Search for packages matching the word docker.

# dnf - Exercise 1:
# Update package metadata on a dnf-based system.
# dnf - Exercise 2:
# Remove a package that is no longer needed.

# pacman - Exercise 1:
# Synchronize package databases on an Arch-based system.
# pacman - Exercise 2:
# Install a package and check its files.

# =========================
# User management
# =========================

# useradd - Exercise 1:
# Create a new user named trainee.
# useradd - Exercise 2:
# Create a new user with a home directory and a specific shell.

# userdel - Exercise 1:
# Remove a user named trainee.
# userdel - Exercise 2:
# Remove a user together with the home directory.

# passwd - Exercise 1:
# Set a password for a newly created user.
# passwd - Exercise 2:
# Expire a user's password and force a change on next login if your system supports it.

# groups - Exercise 1:
# Show all groups for the current user.
# groups - Exercise 2:
# Check which groups a target user belongs to.

# =========================
# Core shell skills
# =========================

# pipes | - Exercise 1:
# Count how many .py files exist under the current directory using a pipeline.
# pipes | - Exercise 2:
# Show unique logged-in usernames in sorted order using multiple commands.

# redirection > and >> - Exercise 1:
# Save the output of ls -l into a new file.
# redirection > and >> - Exercise 2:
# Append the current date to an existing log file.

# input redirection < - Exercise 1:
# Pass a file into a command that can read from standard input.
# input redirection < - Exercise 2:
# Compare behavior of a command with direct filename input versus input redirection.

# command substitution $() - Exercise 1:
# Store the current date in a variable using command substitution.
# command substitution $() - Exercise 2:
# Build a filename that contains the current username.

# variables - Exercise 1:
# Create a variable with a directory path and use it in a command.
# variables - Exercise 2:
# Print two variables inside one sentence.

# if / else - Exercise 1:
# Check whether a file exists and print one message if it does and another if it does not.
# if / else - Exercise 2:
# Check whether the current user is root before running an admin command.

# for loop - Exercise 1:
# Loop through all .txt files and print each filename.
# for loop - Exercise 2:
# Loop through numbers 1 to 5 and create files based on those numbers.

# while loop - Exercise 1:
# Print the current time every second for five iterations.
# while loop - Exercise 2:
# Read a file line by line and print each line with a prefix.

# functions - Exercise 1:
# Write a function that prints a separator line.
# functions - Exercise 2:
# Write a function that accepts one filename argument and checks whether it exists.
