from pathlib import Path
import subprocess


def execute_command(script_path: Path, oper: str, a: str, b: str) -> str:
    completed = subprocess.run(
        args=[str(script_path), oper, a, b],
        capture_output=True,
        text=True,
        check=True,
        cwd=script_path.parent,
    )
    return completed.stdout.strip()
