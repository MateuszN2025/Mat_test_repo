"""Standalone import example that uses only local modules.

Unlike the package-based `f21_myapp` example, this folder is intentionally kept
simple so it can be run directly with `python main.py`.
"""

import sys

from functions1.wrapping import wraping as w
from functions2.file_funcs import fun_funcs as f


@w
def main():
    """Print the import search path and call a helper from another module."""
    print("main")
    for entry in sys.path:
        print(entry)
    f()


if __name__ == "__main__":
    main()