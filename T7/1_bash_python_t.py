import subprocess

# print("-------------------")
# process = subprocess.Popen(
# 	["bash", "-lc", "while true; do date; sleep 1; done"],
# 	stdout=subprocess.PIPE,
# 	text=True,
# )
#
# try:
# 	for line in process.stdout:
# 		print(line, end="")
# except KeyboardInterrupt:
# 	process.terminate()
# 	process.wait()
#
# print("-------------------")

print("-------------------")
# text=True -> Returns output as Python strings instead of bytes.
print("=== cmd1 pwd ===")
cmd1 = subprocess.run(args=["pwd"],
                      capture_output=True,
                      text=True,
                      check=True)
# print(type(pwd.stdout))
print(cmd1.stdout, end="")
print("=== cmd2 simple.bash ===")
path_to_simple = "/mnt/c/Users/mniedziolka/PycharmProjects/Mat_test_repo/T7/simple.bash"
subprocess.run(args=["./simple.bash"],
               capture_output=False,
               text=True,
               check=True)
print("-------------------")
# vboxuser1 # changeme1@
print("=== cmd3 vboxuser1 ===")
cmd3=subprocess.run(
    args=[
        "sshpass",
        "-p", "changeme1@",
        "ssh",
        "vboxuser1@192.168.0.152",
        "ip a | grep 192",
    ],
    capture_output=True,
    text=True,
    check=True,
)
print(cmd3.stdout)
print(repr(cmd3.stdout))
print("-------------------")