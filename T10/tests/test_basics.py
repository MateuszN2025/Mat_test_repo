from pathlib import Path
import allure
import pytest

from .helpers import execute_command
# . Relative — look in the current package (same folder)

def step_assert_eq(actual, expected, label):
    print(f"\n[CHECK] {label}: expected={expected!r}, actual={actual!r} -> "
          f"{'OK' if actual == expected else 'FAIL'}")
    with allure.step(f"{label}: expected={expected!r}, actual={actual!r}"):
        assert actual == expected

@allure.step
@pytest.mark.theone
def test_1_a(calculator_script: Path):
    expected = "1241.0000"
    result = execute_command(calculator_script, "+", "343", "898")

    step_assert_eq(result, expected, "addition result")
    
@allure.step
def test_2(calculator_script: Path):
    expected = "102.0000"
    result = execute_command(calculator_script, "-", "1000", "898")

    step_assert_eq(result, expected, "addition result")
    
@allure.step
def test_3(calculator_script: Path):
    expected = "102.0000"
    result = execute_command(calculator_script, "*", "12", "12")

    step_assert_eq(result, expected, "addition result")

@allure.step
def test_4(calculator_script: Path):
    expected = "225.0000"
    result = execute_command(calculator_script, "*", "15", "15")

    step_assert_eq(result, expected, "addition result")
    

@allure.step
def test_5(calculator_script: Path):
    expected = "1.0000"
    result = execute_command(calculator_script, "/", "15", "15")

    step_assert_eq(result, expected, "addition result")