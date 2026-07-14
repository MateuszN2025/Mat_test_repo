#!/usr/bin/env bash
# ============================================================
# Pre-interview practice — Linux / Bash for QA Automation
# Job offer focus point:
#   - Good familiarity with Linux systems, including command-line
#     operations, scripting, and troubleshooting.
#
# Rules:
#   - No solutions here on purpose — write your own commands/code below each task.
#   - Keep it short. If a task needs a 20-line script, you're overengineering it.
#   - Time yourself: aim for 5-10 min per exercise, this is interview prep, not a project.
#   - Some exercises ask you to just RUN a command in the terminal and note the
#     output as a comment — that's fine, not everything needs to live in this file.
# ============================================================


# ------------------------------------------------------------
# SECTION 1: Command-line navigation & file operations
# ------------------------------------------------------------

# Exercise 1.1
# From your home directory, using a single command, list all *.log files
# anywhere under the current directory tree (any depth), including hidden dirs.
# Write the command as a comment.


# Exercise 1.2
# You have a directory "test_results/" with hundreds of files named like:
#   run_2026-07-01.json, run_2026-07-02.json, ...
# Write a command to count how many such files exist, without opening any of them.


# Exercise 1.3
# Explain (as a comment) the difference between these three, and when you'd
# use each in a test-automation script:
#   cp file.txt /tmp/
#   mv file.txt /tmp/
#   ln -s file.txt /tmp/file.txt


# Exercise 1.4
# Write a command that makes a script "run_tests.sh" executable, then a
# second command that runs it using the current shell's PATH resolution
# (i.e., not by typing "bash run_tests.sh").


# ------------------------------------------------------------
# SECTION 2: Text processing (grep / sed / awk / cut / sort)
# ------------------------------------------------------------

# Exercise 2.1
# You have a pytest log file "pytest_output.log". Write a command that
# prints only the lines containing "FAILED", along with the line number
# in the file.


# Exercise 2.2
# From a CSV file "results.csv" with columns: test_name,status,duration
#   test_login,passed,0.42
#   test_logout,failed,1.10
#   test_signup,passed,0.35
# Write a single command (cut/awk) that prints only the test_name column
# for rows where status is "failed".


# Exercise 2.3
# Write a command that counts how many times each unique status value
# ("passed"/"failed"/"skipped") appears in the "status" column of results.csv,
# and prints a sorted summary (count + status).
# Hint: think about a pipeline combining cut, sort, and uniq.


# Exercise 2.4
# Write a sed one-liner that replaces all occurrences of "localhost" with
# "staging.example.com" in a file "config.env", editing the file in place
# (careful — mention as a comment why you'd want a backup flag here).


# ------------------------------------------------------------
# SECTION 3: Bash scripting fundamentals
# ------------------------------------------------------------

# Exercise 3.1
# Write a small script (function or standalone block) that takes a directory
# path as $1, and exits with an error message + non-zero exit code if the
# directory doesn't exist.

check_dir_exists() {
    :
}


# Exercise 3.2
# Write a loop that iterates over all ".json" files in a directory and
# prints each filename together with its size in bytes.


# Exercise 3.3
# Write a function `retry_command` that takes a command as arguments and
# retries running it up to 3 times if it fails (non-zero exit code),
# waiting 1 second between attempts. This is the bash equivalent of the
# Python `retry(func, attempts=3)` exercise — same idea, different language.

retry_command() {
    :
}


# Exercise 3.4
# Write a script snippet that reads a ".env"-style file line by line
# (KEY=VALUE format, skipping blank lines and lines starting with "#")
# and exports each variable.


# ------------------------------------------------------------
# SECTION 4: Process management & troubleshooting
# ------------------------------------------------------------

# Exercise 4.1
# Write a command to find the PID of a running process named "pytest",
# and a second command that kills it gracefully (not "kill -9" first).


# Exercise 4.2
# A test run seems to hang. Write down (as comments) the sequence of
# commands you'd run to investigate:
#   - is the process still alive and using CPU?
#   - what files/ports does it currently have open?
#   - what does the last N lines of its log say?


# Exercise 4.3
# Explain in a comment: what's the difference between exit code 0, 1, and
# 127 for a shell command? Why does a CI pipeline care about exit codes
# instead of parsing stdout text to decide pass/fail?


# Exercise 4.4
# Write a command that shows disk usage of the current directory's
# subfolders, sorted from largest to smallest (useful when a CI runner
# disk fills up from old test artifacts).


# ------------------------------------------------------------
# SECTION 5: Test-automation-flavored scripting
# ------------------------------------------------------------

# Exercise 5.1
# Write a script that runs "pytest" and captures its exit code, then
# prints "TESTS PASSED" or "TESTS FAILED" based on that exit code
# (don't parse the text output — use $?).


# Exercise 5.2
# Write a script that creates a timestamped results directory, e.g.
#   results/run_2026-07-14_15-30-00/
# and copies the latest test report file into it.


# Exercise 5.3
# Explain in a short comment: why is `set -euo pipefail` at the top of a
# bash test-runner script generally a good idea? What could go wrong if
# you skip it?


# ------------------------------------------------------------
# SECTION 6: Mini integration challenge
# ------------------------------------------------------------

# Exercise 6.1
# Write a single small script "smoke_check.sh" that:
#   - checks a required env var (e.g. BASE_URL) is set, exits with error if not
#   - checks a required command (e.g. "curl") is available
#   - runs "curl -s -o /dev/null -w '%{http_code}' $BASE_URL" and prints
#     PASS/FAIL based on whether the status code is 200
# Keep it under ~15 lines. If it's growing bigger, you're violating KISS.
