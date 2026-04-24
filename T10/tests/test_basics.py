from pathlib import Path

from .helpers import execute_command


def test_1_addition(calculator_script: Path):
    result = execute_command(calculator_script, "+", "343", "898")

    assert result == "1241.0000"
