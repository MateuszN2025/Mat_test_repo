from pathlib import Path
import allure
from .helpers import execute_command
# subprocess.run(args="clear")
print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n")

pwd = "changeme1@"
user = "vboxuser1"
ip = "192.168.0.152"
path = "/home/vboxuser1/calc2/b_calc"

command = ["sshpass",
           "-p",
           pwd,
           "ssh",
           f"{user}@{ip}",
           path]


def step_assert_eq(actual, expected, label):
    print(f"\n[CHECK] {label}: expected={expected!r}, actual={actual!r} -> "
          f"{'OK' if actual == expected else 'FAIL'}")
    with allure.step(f"{label}: expected={expected!r}, actual={actual!r}"):
        assert actual == expected

@allure.step
def test_1_addition():
    print(f"\ncalculator_script:{command}")
    expected = "1241.0000"
    print(f"\nPath(__file__):{Path(__file__)}")
    result = execute_command(*command, "+", "343", "898")
    step_assert_eq(result, expected, "addition result")



# print(execute_command(APPLICATION_DIR, "+", "343", "898"))
# ['/home/mniedziolka/PP/Mat_test_repo/T11/application/b_calc', '+', '343', '898']
# command = "sshpass -p 'changeme1@' ssh vboxuser1@192.168.0.152 /home/vboxuser1/calc2/b_calc"

# ####################################################
# print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
# print(execute_command(*command, "+", "343", "898"))
# ####################################################

# print("------------------------------------------")
# print(Path(__file__).resolve().parents[0])
# print(Path(__file__).resolve().parents[1])
# print(Path(__file__).resolve().parents[2])
# print("------------------------------------------")

# ####################################################
# PROJECT_ROOT = Path(__file__).resolve().parents[1]
# APPLICATION_DIR = PROJECT_ROOT / "application" / "b_calc"
# print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
# print(execute_command(APPLICATION_DIR, "+", "343", "898"))
# ####################################################

print("\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")  # noqa: E303
