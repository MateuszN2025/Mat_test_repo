#!/bin/bash

set -euo pipefail

path_to_file="${BASH_SOURCE[0]}"
echo "$path_to_file"
dir_name="$(dirname $path_to_file)"
echo "$dir_name"
cd "$dir_name/.."
source ./.venv/bin/activate
cd "$dir_name/python"
python3 v01_e3_paramiko.py

arr=(a b c)
echo $arr        # → a         (first element, short form)
echo $arr[1]     # → a[1]      (bug: "[1]" is literal text)
echo ${arr[1]}   # → b         (correct: index 1)
echo ${arr[@]}   # → a b c     (all elements)

echo $?