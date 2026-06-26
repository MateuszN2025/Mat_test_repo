import importlib
import subprocess

try:
	paramiko = importlib.import_module("paramiko")
except ImportError:
	paramiko = None


def run_with_paramiko() -> None:
	if paramiko is None:
		print("paramiko is not installed")
		return

	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.connect(hostname="192.168.1.10", username="user", password="pass")

	stdin, stdout, stderr = client.exec_command("systemctl is-active app")
	output = stdout.read().decode().strip()
	print(output)

	client.close()


# The same idea without paramiko: use the system ssh command via subprocess.
# This does not use a Python SSH library. It runs the local "ssh" binary.
# run_with_paramiko() is library-based
"""
client = paramiko.SSHClient()
client.connect(hostname="192.168.1.10", username="user", password="pass")
stdin, stdout, stderr = client.exec_command("systemctl is-active app")
"""
# run_with_subprocess_ssh() is command-based
"""
result = subprocess.run(
    ["ssh", "user@192.168.1.10", "systemctl is-active app"],
    capture_output=True,
    text=True,
)
"""


def run_with_subprocess_ssh() -> None:
	result = subprocess.run(
		["ssh", "user@192.168.1.10", "systemctl is-active app"],
		capture_output=True,
		text=True,
		check=False,
	)

	output = result.stdout.strip()
	error_output = result.stderr.strip()

	if output:
		print(output)
	if error_output:
		print(error_output)


# Example usage:
# run_with_paramiko()
# run_with_subprocess_ssh()