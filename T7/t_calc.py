import subprocess  # noqa: E401
import re


# process = subprocess.Popen(
#     ["bash", "./calc.bash"],
#     stdin=subprocess.PIPE,
#     stdout=subprocess.PIPE,
#     stderr=subprocess.PIPE,
#     text=True,
#     # cwd=r"c:\Users\mniedziolka\PycharmProjects\Mat_test_repo\T7",
#     cwd="/mnt/c/Users/mniedziolka/PycharmProjects/Mat_test_repo/T7"
# )
#
# stdout, stderr = process.communicate("+\n5\n6\n")
# print(stdout)

r"=\s*\d+"
# = matches the equals sign
# \s* allows optional spaces after =
# \d+ matches one or more digits

r"=\s*-?\d+(?:\.\d+)?"
#
# sign = "/"
# a = -2234
# b = -432

test_data = ["/", -2234, -432, 5.1713]

response = subprocess.run(
    ["bash", "./calc.bash"],
    input=f"{test_data[0]}\n{test_data[1]}\n{test_data[2]}\n",
    text=True,
    capture_output=True,
    # cwd="/mnt/c/Users/mniedziolka/PycharmProjects/Mat_test_repo/T7",
    check=True,
)
# print(type(response.stdout))
# print(list[response.stdout])
result = response.stdout
# print(result)

match = re.search(r"=\s*(-?\d+\.\d+)$", result)
if match:
    print(match.group(1))
    # print(type(match.group(1)))

assert float(match.group(1)) == test_data[3]
