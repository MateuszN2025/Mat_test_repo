from pathlib import Path
import sys

# Build an absolute path to the repository root directory (`Mat_test_repo`).
#
# Step-by-step:
# 1) `Path(__file__)` -> path to this script file (`.../T6/16_monkey/16_monkey_e.py`).
# 2) `.resolve()` -> normalize to an absolute canonical path.
# 3) `.parents[2]` -> go up 3 levels:
#    - parents[0] = `.../T6/16_monkey`
#    - parents[1] = `.../T6`
#    - parents[2] = `.../Mat_test_repo`
# We need this root so imports like `from T0.wrapping import ...` can be resolved.
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Ensure Python can import top-level folders under `Mat_test_repo`.
# `sys.path` is the module search path checked from left to right.
# We insert at index 0 to prioritize this project root over similarly named
# modules that could exist elsewhere in the environment.
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))



from T0.wrapping import wraping as w

@w
def main():
    print("main")

main()