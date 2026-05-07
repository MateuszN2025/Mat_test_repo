# Bash Cheat Sheet

Quick goal: learn the Bash commands and patterns you will use most often as a QA automation engineer.

## Easy

### Print text

```bash
echo "Hello, Bash"
```

### Show current directory

```bash
pwd
```

### List files

```bash
ls
ls -la
```

### Create variables

```bash
name="Mateusz"
echo "$name"
```

### Read input

```bash
read -p "Enter environment: " env
echo "Running on: $env"
```

### Run a script

```bash
bash my_script.sh
./my_script.sh
```

### Positional arguments

```bash
echo "First: $1"
echo "Second: $2"
echo "All: $@"
echo "Count: $#"
```

### Basic file checks

```bash
if [[ -e "data.txt" ]]; then
    echo "File exists"
fi
```

### Common file tests

```bash
[[ -e file.txt ]]   # exists
[[ -f file.txt ]]   # regular file
[[ -d my_dir ]]     # directory
[[ -x script.sh ]]  # executable
```

## Medium

### If else

```bash
number=15

if [[ "$number" -gt 10 ]]; then
    echo "Greater than 10"
else
    echo "10 or less"
fi
```

### For loop

```bash
for i in 1 2 3 4 5; do
    echo "$i"
done
```

### Loop through files

```bash
for file in *.txt; do
    echo "$file"
done
```

### While loop

```bash
counter=5

while [[ "$counter" -gt 0 ]]; do
    echo "$counter"
    counter=$((counter - 1))
done
```

### Functions

```bash
greet() {
    echo "Hello, $1"
}

greet "Mateusz"
```

### Command substitution

```bash
today=$(date +%F)
echo "$today"
```

### Count files

```bash
count=$(find . -maxdepth 1 -type f | wc -l)
echo "$count"
```

### Exit codes

```bash
mkdir test_dir
echo "$?"
```

`0` usually means success. Anything else usually means failure.

### Redirect output

```bash
echo "test log" > log.txt
echo "next line" >> log.txt
cat log.txt
```

### Pipe commands

```bash
ls -la | grep ".sh"
```

## Advanced

### Safer script header

```bash
#!/bin/bash
set -euo pipefail
```

Short note: this stops the script on errors, unset variables, and failed pipes.

### Case statement

```bash
read -p "Choose env: " env

case "$env" in
    dev) echo "Using dev" ;;
    stage) echo "Using stage" ;;
    prod) echo "Using prod" ;;
    *) echo "Unknown env" ;;
esac
```

### Arrays

```bash
browsers=(chrome firefox edge)
echo "${browsers[0]}"
echo "${browsers[@]}"
```

### Process a file line by line

```bash
while read -r line; do
    echo "$line"
done < users.txt
```

### Check command success directly

```bash
if curl -s https://example.com > /dev/null; then
    echo "API is reachable"
else
    echo "API is down"
fi
```

### Find and act on files

```bash
find . -name "*.log" -type f
find . -name "*.log" -type f -exec rm {} \;
```

### Debug a script

```bash
bash -n my_script.sh
bash -x my_script.sh
```

Short note: use `-n` for syntax and `-x` to see each command as Bash executes it.

### Trap cleanup on exit

```bash
tmp_file=$(mktemp)
trap 'rm -f "$tmp_file"' EXIT
```

### Simple QA example

```bash
#!/bin/bash
set -euo pipefail

read -p "Enter environment: " env

if [[ "$env" != "dev" && "$env" != "stage" && "$env" != "prod" ]]; then
    echo "Invalid environment"
    exit 1
fi

pytest tests/ -m smoke --tb=short
```

## What Matters Most

- Learn `pwd`, `ls`, `cd`, `echo`, `read`, `if`, `for`, and `while` first.
- Quote variables like `"$file"` to avoid bugs with spaces.
- Use `bash -n` before debugging logic.
- Use `set -euo pipefail` in more serious scripts.

## Flags That Matter Most (Quick Reference)

### `if` with `[[ ... ]]` file/string checks

Important note: `if` itself has no flags. The checks below are test operators used inside `[[ ... ]]`.

```bash
[[ -e path ]]   # path exists
[[ -f path ]]   # regular file
[[ -d path ]]   # directory
[[ -s path ]]   # file exists and is not empty
[[ -r path ]]   # readable
[[ -w path ]]   # writable
[[ -x path ]]   # executable
[[ -L path ]]   # symbolic link
[[ -z "$var" ]] # string is empty
[[ -n "$var" ]] # string is not empty
```

QA example:

```bash
if [[ -f "results.xml" && -s "results.xml" ]]; then
    echo "Report exists and has content"
else
    echo "Missing or empty report"
    exit 1
fi
```

### `ls`

```bash
ls -la   # long format + show hidden files
ls -lh   # human-readable sizes
ls -lt   # sort by newest modification time
```

### `grep`

```bash
grep -i "error" app.log     # case-insensitive search
grep -n "timeout" app.log   # show line numbers
grep -r "TODO" .            # recursive search
grep -E "warn|error" app.log # extended regex
```

### `find`

```bash
find . -name "*.log" -type f      # files by name pattern
find . -maxdepth 2 -type d         # directories up to depth 2
find . -name "*.xml" -mtime -1    # changed in last 24h
find . -name "*.log" -exec rm {} \; # run action per result
```

### `head` / `tail`

```bash
head -n 20 run.log      # first 20 lines
tail -n 50 run.log      # last 50 lines
tail -f run.log         # follow live log updates
```

### `cat`

```bash
cat -n file.txt         # show line numbers
cat -A file.txt         # show hidden chars (tabs/endings)
```

### `read`

```bash
read -p "Env: " env    # prompt + input
read -r line            # raw read (no backslash escaping)
read -s -p "Token: " token # silent input (secrets)
```

### `mkdir`, `cp`, `mv`, `rm`

```bash
mkdir -p reports/archive      # create nested dirs if missing
cp -r artifacts backup_dir    # recursive copy
cp -n source.txt target.txt   # do not overwrite existing file
mv -n old.txt new.txt         # move/rename without overwrite
rm -r old_dir                 # remove directory recursively
rm -f temp.txt                # force remove without prompt
```

Safety tip: avoid `rm -rf` unless you are 100% sure about the path.

### `bash` (script checks and debugging)

```bash
bash -n script.sh   # syntax check only
bash -x script.sh   # trace execution line by line
```

### `pytest` (common QA run flags)

```bash
pytest -q                    # quieter output
pytest -k "smoke"           # run tests matching expression
pytest -m "api and not slow" # marker selection
pytest -x                    # stop after first failure
pytest --maxfail=2           # stop after N failures
pytest --tb=short            # shorter traceback
```

## Senior-Level Insight

Most Bash bugs in automation are not syntax problems. They come from unquoted variables, weak error handling, and assumptions about files that do not exist. If you build the habit of quoting variables and checking exit paths early, your scripts become much more reliable.

## Short Practice Task

Write a script that:

1. asks for an environment with `read`
2. checks if it is `dev`, `stage`, or `prod`
3. creates a log file named `run.log`
4. writes `Selected environment: ...` into that file