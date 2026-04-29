import allure
from .helpers import execute_command
import subprocess
import pytest

def step_assert_eq(result, expected, label):
    result = float(result)
    expected = float(expected)
    print(f"\n[CHECK] {label}: expected={expected!r}, actual={result!r} -> "
          f"{'OK' if result == expected else 'FAIL'}")
    with allure.step(f"{label}: expected={expected!r}, actual={result!r}"):
        assert result == expected

# When pytest runs it as a package (via run_test):
#   pytest is invoked from T11/ (the cd "$PROJECT_ROOT" in your script).
#   tests/ is a PACKAGE because tests/__init__.py exists.
#   from helpers import execute_command would fail because 
#       helpers is not on sys.path from that working directory.
#   from .helpers import execute_command works because 
#       it resolves within the tests package.

@allure.step
@pytest.mark.parametrize(argnames=["oper", "a", "b", "expected"],
                         argvalues=[("+", 343, 898, 1241),
                                    (r"\*", 10, 20, 200),
                                    ("-", 10, 3, 7),
                                    ("/", 10, 4, 2.5)])
def test_1(remote_calc_command, oper, a, b, expected):
    try:
        result = execute_command(*remote_calc_command, oper, a, b)
    except subprocess.CalledProcessError as e:      
        print(f"⚠️ {e}") 
        result = None 
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
# When you run python test_basics.py directly:
#   Python adds the file's directory (tests/) to sys.path automatically.
#   So from helpers import execute_command finds tests/helpers.py as a top-level module.
#   No package context exists, so the relative .helpers would fail.

# from pathlib import Path
# PROJECT_ROOT = Path(__file__).resolve().parents[1]
# APPLICATION_DIR = PROJECT_ROOT / "application" / "b_calc"
# print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
# print(execute_command(APPLICATION_DIR, "+", "343", "898"))
# ####################################################


