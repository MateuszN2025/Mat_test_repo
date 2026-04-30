"""Local decorator helpers for the standalone import example."""

import subprocess

"""Clear the terminal and frame the wrapped function output."""
def wraping(func):
    def wraping_():
        sep = "➖"
        subprocess.run(["clear"], check=False)
        print(sep * 20)
        func()
        print(sep * 20)
    return wraping_

