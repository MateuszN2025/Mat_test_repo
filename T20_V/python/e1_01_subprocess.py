import subprocess

command = ["ls"]

result = subprocess.run(args=command, check=True, text=True, capture_output=True, timeout=5)

# args=command — the command to execute (e.g., ["ls", "-la"] or "ls -la")
# check=True — raise an exception if the command fails
# text=True — decode output as strings instead of raw bytes
# capture_output=True — capture both stdout and stderr

print(result.stdout)