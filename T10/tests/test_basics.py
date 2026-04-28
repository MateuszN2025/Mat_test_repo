from pathlib import Path
import allure

from .helpers import execute_command
# . Relative — look in the current package (same folder)

def step_assert_eq(actual, expected, label):
    print(f"\n[CHECK] {label}: expected={expected!r}, actual={actual!r} -> "
          f"{'OK' if actual == expected else 'FAIL'}")
    with allure.step(f"{label}: expected={expected!r}, actual={actual!r}"):
        assert actual == expected

@allure.step
def test_1_addition(calculator_script: Path):
    expected = "1241.0000"
    result = execute_command(calculator_script, "+", "343", "898")

    step_assert_eq(result, expected, "addition result")
