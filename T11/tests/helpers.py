from pathlib import Path
import allure
import subprocess

@allure.step
def execute_command(*args) -> str:
    # print(*args)
    # print(args)
    completed = subprocess.run(
        # args=args, # works because:
        # ('sshpass', '-p', 'changeme1@', 'ssh', 'vboxuser1@192.168.0.152', '/home/vboxuser1/calc2/b_calc', '-', '343', '898')
        args=[str(arg) for arg in args],
        capture_output=True,
        text=True,
        check=True
    )
    return completed.stdout.strip().replace(",", ".")
