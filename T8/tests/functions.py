import subprocess, re

path = "/mnt/c/Users/mniedziolka/PycharmProjects/Mat_test_repo/T8/project/application/"
# path = "C:\\Users\\mniedziolka\\PycharmProjects\\Mat_test_repo\\T8"

def run_operation(
        operation :str,
        number_a: float,
        number_b: float) -> str:

    test_data = [
        operation,
        number_a,
        number_b
    ]

    command_data = [
        "bash",
        f"./calc.bash"
    ]
    input_data = f"{test_data[0]}\n{test_data[1]}\n{test_data[2]}\n"

    request = subprocess.run(
        args=command_data,
        input=input_data,
        text=True,
        capture_output=True,
        cwd = path,
        check=True
    )

    match = re.search(r"=\s*(-?\d+\.\d+)$", request.stdout)
    if match:
        return float(match.group(1))
    else:
        return None