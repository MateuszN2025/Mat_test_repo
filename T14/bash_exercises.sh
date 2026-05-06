#!/bin/bash
echo ➖➖➖➖➖➖➖➖➖
# Exercise 01
# Level: Easy
# Print `Hello, Bash!` to the terminal.
echo --1--
echo Hello Bash

# Exercise 02
# Level: Easy
# Print your current working directory.
echo --2--
pwd
# Exercise 03
# Level: Easy
# List all files and folders in the current directory.
echo --3--
ls
# Exercise 04
# Level: Easy
# Create a variable called `name`, assign your name to it, and print it.
echo --4--
NAME=Mateusz
echo $NAME
# Exercise 05
# Level: Easy
# Ask the user for their city using `read` and print: `You live in <city>`.
# #RepeatLater
echo --5--
# PLACE=""
# echo "Where do You live?"
# read PLACE
# echo "You live in $PLACE"
# read -p "Where do You live? " PLACE
# echo "You live in $PLACE"
# read -p "What is your city? " city
# echo "You live in $city"

# Exercise 06
# Level: Easy
# Create a folder called `practice_dir` and inside it create an empty file called `notes.txt`.
echo --6--
FOLDER1="practice_dir"
if [[ -e $FOLDER1 ]]; then
    echo Folder $FOLDER1 exists. ✅
else
    echo Folder $FOLDER1 does not exist. ❌
    echo Create a folder. ℹ️
    mkdir $FOLDER1
fi

FILE1="notes.txt"

if [[ -e "./$FOLDER1/$FILE1" ]]; then
    echo "File ./$FOLDER1/$FILE1 exists." ✅
else
    echo File ./$FOLDER1/$FILE1 does not exist. ❌
    echo Create a file. ℹ️
    touch ./$FOLDER1/$FILE1
fi

# Exercise 07
# Level: Easy
# Check whether a file called `data.txt` exists and print a message depending on the result.
# #RepeatLater
echo --7--
FILE2="data.txt"
if [[ -e $FILE2 ]]; then
    echo File $FILE2 exists. ✅
else
    echo File $FILE2 does not exist. ❌
fi

# Exercise 08
# Level: Easy
# Write a script that prints the number of arguments passed to it.
echo --8--
bash ./exe8.sh a b c d e 
# Exercise 09
# Level: Easy
# Write a script that prints the first and second positional arguments.
echo --9--
bash ./exe9.sh a b c d e 
# Exercise 10
# Level: Easy
# Use an `if` statement to check whether a number is greater than 10.
echo --10--
NUMBER=11
if [[ $NUMBER -gt 10 ]]; then
    echo "Number is grater than 10"
else
    echo "Number is lower or equal 10"
fi
# Exercise 11
# Level: Medium
# Use a `for` loop to print numbers from 1 to 5.
# #RepeatLater
echo --11--


# Exercise 12
# Level: Medium
# Loop through all `.txt` files in the current directory and print each filename.

# Exercise 13
# Level: Medium
# Count how many files are in the current directory and print the result.

# Exercise 14
# Level: Medium
# Read a filename from the user and print its contents only if the file exists.

# Exercise 15
# Level: Medium
# Create a script that accepts a directory path and prints whether it is a valid directory.

# Exercise 16
# Level: Medium
# Use a `while` loop to print numbers from 5 down to 1.

# Exercise 17
# Level: Medium
# Write a script that creates 5 files named `file_1.txt` to `file_5.txt`.

# Exercise 18
# Level: Medium
# Write a script that renames all `.log` files in the current directory by adding `_old` before the extension.

# Exercise 19
# Level: Medium
# Create a function called `greet` that takes one argument and prints a greeting with that name.

# Exercise 20
# Level: Medium
# Ask the user for a path and print whether it is a file, a directory, or does not exist.
echo
echo ➖➖➖➖➖➖➖➖➖