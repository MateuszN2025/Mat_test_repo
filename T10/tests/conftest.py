from pathlib import Path
import sys

# print("------------------------------------------")
# conftest.py is loaded by pytest before test modules are imported.
# That makes it a good place to do small test-environment setup like
# adjusting Python's import path for this test suite.

# __file__ is the full path to this file, for example:
# /home/mniedziolka/PP/Mat_test_repo/T10/tests/conftest.py
#
# Path(__file__) turns that string path into a Path object.
# .resolve() converts it to an absolute normalized path.
current_file = Path(__file__).resolve()
# print(f"current_file {current_file}")

# parents[0] -> .../T10/tests
# parents[1] -> .../T10
#
# We need the T10 directory on sys.path, because that directory contains
# the helpers folder used by imports like:
# import helpers.helpers_functions as h
PROJECT_ROOT = current_file.parents[1]
# print(f"PROJECT_ROOT {PROJECT_ROOT}")

# sys.path is the list of directories Python searches when resolving imports.
#
# When pytest is run from the tests directory, Python may only search from:
# .../T10/tests
# and not from:
# .../T10
#
# Because of that, `import helpers.helpers_functions` can fail with
# ModuleNotFoundError, even though the helpers folder exists one level above.

# insert(0, ...) adds the project root at the beginning of sys.path.
# Position 0 matters: Python searches sys.path from left to right, so this
# makes the T10 directory one of the first places checked during imports.
sys.path.insert(0, str(PROJECT_ROOT))
# print(f"sys.path.insert(0, str(PROJECT_ROOT)) {sys.path.insert(0, str(PROJECT_ROOT))}")
# print("------------------------------------------")