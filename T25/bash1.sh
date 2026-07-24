# 1. ls - Exercise 1:
# Show all files in the current directory, including hidden ones, in long format.

    echo -e "\n > 1 < \n"
    ls -al

# 2. ls - Exercise 2:
# List files in a target directory sorted by size from largest to smallest.

    echo -e "\n > 2 < \n"
    ls -lS | grep '^-'
