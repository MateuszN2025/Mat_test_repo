import pytest
import allure
from .helpers import execute_command

@pytest.mark.optimal
@pytest.mark.parametrize(
    "oper,a,b,expected",
    [
        ("+", 343, 898, 1241.0),
        (r"\*", 10, 20, 200.0),
        ("-", 10, 3, 7.0),
        ("/", 10, 4, 2.5),
    ],
    ids=["add", "mul", "sub", "div"],
)
def test_3(remote_calc_command, oper, a, b, expected):
    result = execute_command(*remote_calc_command, oper, a, b)
    with allure.step(f"{a} {oper} {b} == {expected}"):
        assert float(result) == pytest.approx(expected)
        
@pytest.mark.parametrize(
    "oper,a,b,expected",
    [
        ("+", 0, 0, 0),
        (r"\*", 0, 0, 0),
        ("-", 0, 0, 0),
        ("/", 0, 1, 0),
    ],
    ids=["adding", "multiplication", "subtraction", "division"],
)
def test_7(remote_calc_command, oper, a, b, expected):
    result = execute_command(*remote_calc_command, oper, a, b)
    with allure.step(f"{a} {oper} {b} == {expected}"):
        assert float(result) == pytest.approx(expected)