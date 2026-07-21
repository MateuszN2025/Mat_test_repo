"""Short learning file for subprocess usage in QA automation.

Run:
    python3 T20_V/python/01_subprocess_learning.py
"""

# from __future__ import annotations
# It postpones evaluation of the annotation.
# So Python stores the annotation without trying to fully 
# execute subprocess.CompletedProcess[str] immediately.
# That makes type hints safer and more flexible at runtime.
# In modern Python, from __future__ import annotations is mostly 
# about making annotations cheaper and less fragile at runtime.
# It is not the source of generic typing itself.


"""
Your output shows the real difference very clearly.

With from __future__ import annotations:
{'command': 'str', 'return': 'subprocess.CompletedProcess[str]'}

Python stores annotations as unevaluated strings.

Without it:
{'command': <class 'str'>, 'return': subprocess.CompletedProcess[str]}
Python evaluates annotations immediately and stores real objects.
"""


import shlex
import subprocess
import w_r


def run_command(command: str) -> subprocess.CompletedProcess[str]:
    """Run a shell-like command safely and capture output.

    Important: shlex.split keeps the example close to terminal usage,
    but still avoids shell=True for better safety and predictability.
    """
    return subprocess.run(
        shlex.split(command),
        # "python3 --version" -> shlex.split(command) -> ["python3", "--version"]
        text=True,
        capture_output=True, # capture stdout/stderr
        check=False, # do not raise an exception automatically on non-zero exit
        timeout=5,
    )


def print_result(title: str, result: subprocess.CompletedProcess[str]) -> None:
    # Return code is the first thing to inspect in CI or device checks.
    print(f"\n=== {title} ===")
    print(f"return code: {result.returncode}")
    print(f"stdout: {result.stdout.strip() or '<empty>'}")
    print(f"stderr: {result.stderr.strip() or '<empty>'}")

@w_r
def main():
    print("Subprocess learning example for QA automation")

    hostname_result = run_command("hostname")
    print_result("hostname", hostname_result)

    # This style is common in smoke tests: run command, inspect code, log output.
    python_result = run_command("python3 --version")
    print_result("python version", python_result)

    if python_result.returncode != 0:
        print("Important: a non-zero return code should fail the test or pipeline stage.")
        
    print("------------------------------------------")
    print(run_command.__annotations__)
        
        
if __name__ == "__main__":
    main()