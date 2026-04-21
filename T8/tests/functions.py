import re
import subprocess
from pathlib import Path


APPLICATION_DIR = Path(__file__).resolve().parents[1] / "project" / "application"


def run_operation(
    operation: str,
    number_a: float,
    number_b: float,
) -> float | None:

    test_data = [
        operation,
        number_a,
        number_b
    ]

    command_data = [
        "bash",
        "./calc.bash",
    ]
    input_data = f"{test_data[0]}\n{test_data[1]}\n{test_data[2]}\n"

    request = subprocess.run(
        args=command_data,
        input=input_data,
        text=True,
        capture_output=True,
        cwd=APPLICATION_DIR,
        check=True,
    )

    match = re.search(r"=\s*(-?\d+\.\d+)$", request.stdout)
    if match:
        return float(match.group(1))

    return None