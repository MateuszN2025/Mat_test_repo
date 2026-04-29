# Python Import Cheat Sheet

## Setup that matters

```
T11/
├── pytest.ini          ← testpaths = tests
├── tests/
│   ├── __init__.py     ← makes tests/ a PACKAGE
│   ├── conftest.py
│   ├── helpers.py
│   └── test_basics.py
```

---

## Rule 1: `__init__.py` presence

| `__init__.py` exists | `tests/` is a... | relative imports allowed |
|---|---|---|
| Yes | package | Yes |
| No | plain directory | No |

---

## Rule 2: How you run determines `sys.path`

| How you run | cwd added to `sys.path` | file's dir added |
|---|---|---|
| `python tests/test_basics.py` | No | Yes (`tests/`) |
| `pytest` from `T11/` | Yes (`T11/`) | No |
| `python -m pytest` from `T11/` | Yes (`T11/`) | No |

---

## Rule 3: Which import works where

| Import style | `python test_basics.py` direct | `pytest` from `T11/` |
|---|---|---|
| `from helpers import x` | ✅ `tests/` on path | ❌ `tests/` not on path |
| `from .helpers import x` | ❌ no package context | ✅ resolves within package |
| `from tests.helpers import x` | ❌ `tests/` not a package here | ✅ if `T11/` on path |

---

## Rule 4: Golden rule for pytest projects

Always use **relative imports** (`from .helpers import x`) in test files.
Always run via `pytest`, never via `python test_file.py` directly.

---

## Rule 5: `conftest.py` is special

- pytest finds and loads it automatically.
- Fixtures defined there are available to all tests in that directory and below.
- No import needed in test files.

---

## This project: correct setup

```python
# test_basics.py  ✅
from .helpers import execute_command   # relative, correct for pytest package run
```

```bash
# run_test  ✅
cd "$PROJECT_ROOT"   # T11/ — makes tests a package visible to pytest
python -m pytest
```
