import os
import subprocess
from pathlib import Path

path1 = "/home/mateusz/repo/Mat_test_repo/Training/t_200/ex1_1/b_curl_api.bash"

result = subprocess.run(
    [path1],
    capture_output=True,
    text=True
)
print("---------------------")
print(result.stdout)
print(result.stderr)
print(result.returncode)
print("---------------------")
print(os.getcwd())
print("---------------------")
print(Path.cwd())
print("---------------------")
files = os.listdir()
print("---------------------")

