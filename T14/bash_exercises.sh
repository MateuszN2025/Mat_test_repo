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
for i in 1 2 3 4; do
    echo "$i"
done


# Exercise 12
# Level: Medium
# Loop through all `.txt` files in the current directory and print each filename.
echo --12--
for x in *.txt; do
    echo "$x"
done

# Exercise 13
# Level: Medium
# Count how many files are in the current directory and print the result.
echo --13--
COUNTER=0
for x in *.txt; do
    COUNTER=$((COUNTER + 1))
done
echo "$COUNTER"


# Exercise 14
# Level: Medium
# Read a filename from the user and print its contents only if the file exists.
echo --14--
# for x in *.txt; do
#     echo "context $x " > $x
# done
FILE3="file1.txt"
if [[ -e $FILE3 ]]; then
    cat $FILE3 
fi
# echo "--"
# cat file3.txt
# echo "--"
# head -2 file3.txt

# Exercise 15
# Level: Medium
# Create a script that accepts a directory path and prints whether it is a valid directory.
echo --15--
DIRECT="./practice_dir/"
if [[ -d $DIRECT ]]; then
    echo "It is a valid dir"
else
    echo "Wrong dir"
fi

# Exercise 16
# Level: Medium
# Use a `while` loop to print numbers from 5 down to 1.
echo --16--
COUNTER2=5
while [[ $COUNTER2 -gt 0 ]]; do
    echo $COUNTER2
    COUNTER2=$((COUNTER2 - 1))
done

# Exercise 17
# Level: Medium
# Write a script that creates 5 files named `file_1.log` to `file_5.log`.
echo --17--
# for j in 1 2 3 4 5; do
#     touch "file_$j.log"
# done

# Exercise 18
# Level: Medium
# Write a script that renames all `.log` files in the current directory by adding `_old` before the extension.
echo --18--
# for file in *.log; do
#     mv "$file" "${file%.log}_old.log"
#     # ${file%.log} strips the .log extension from the end of the filename (so app.log becomes app).
# done

# Exercise 19
# Level: Medium
# Create a function called `greet` that takes one argument and prints a greeting with that name.
echo --19--
greet(){
    echo "Hello to $1 $2"
    echo "$#"
}
greet "MMaatt" "NNied"

# Exercise 20
# Level: Medium
# Ask the user for a path and print whether it is a file, a directory, or does not exist.
echo --20--
# read -p "Give a path: " PATH2
# PATH2="./file1.txt"
# PATH2="./practice_dir"
# PATH2="./practice_dira"
PATH2="./file221.txt"

if [[ -d $PATH2 ]];then
    echo "it is a dir"
elif [[ -f $PATH2 ]];then
     echo "it is a file"
elif [[ -n $PATH2 ]];then
     echo "it does not exist"
fi

# Exercise 21
# Level: Medium
# Write a while read loop that prints only lines containing the word ERROR.
echo --20--
for line in file3.txt;do
    echo "$line"
done < file3.txt

echo "------"

while read line; do
    echo "$line"
done < file3.txt

echo
echo ➖➖➖➖➖➖➖➖➖