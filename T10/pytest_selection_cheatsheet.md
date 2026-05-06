# Pytest Test Selection Cheat Sheet for T10

Run these commands from the `T10/` directory.

## Most common commands

Run one exact test by node id:

```bash
pytest -vv -rP -s tests/test_basics.py::test_1_a
```

Run all tests from one file:

```bash
pytest -vv -rP -s tests/test_basics.py
```

Run all tests from the current pytest project:

```bash
pytest -vv -rP -s
```

Run tests by name substring with `-k`:

```bash
pytest -vv -rP -s -k "test_1"
```

Try to run tests by marker name with `-m "test_1"`:

```bash
pytest -vv -rP -s -m "test_1"
```

In `T10`, this usually selects nothing, because `test_1` is not a marker.

Run tests marked with `theone`:

```bash
pytest -vv -rP -s -m theone
```

This matches `@pytest.mark.theone` in `tests/test_basics.py`.

## What the options mean

`-vv`

- Very verbose output.
- Shows more details for collected tests and execution.

`-rP`

- Adds extra reporting summary information.
- `P` shows captured output for passing tests in the summary.

`-s`

- Disables output capturing.
- Useful when you want to see `print()` output live during the run.

`-k`

- Selects tests by keyword expression.
- Matches parts of test names, class names, file names, and node ids.
- Good for quick filtering when you remember part of a test name.

Examples:

```bash
pytest -vv -rP -s -k "test_1"
pytest -vv -rP -s -k "test_1_a or test_2"
pytest -vv -rP -s -k "not test_2"
```

`-m`

- Selects tests by pytest marker.
- Works only with markers added in code, for example `@pytest.mark.theone`.
- Best when you want stable groups such as smoke, api, slow, or regression.

Examples:

```bash
pytest -vv -rP -s -m theone
pytest -vv -rP -s -m "theone"
pytest -vv -rP -s -m "not theone"
```

## `-k` vs `-m`

Use `-k` when you want to match a test name.

```bash
pytest -vv -rP -s -k "test_1"
```

Use `-m` when you want to match a marker.

```bash
pytest -vv -rP -s -m theone
```

Important: `-m "test_1"` does not mean "run the test named `test_1`". It means "run tests marked with `@pytest.mark.test_1`".

## If you later add parametrized tests

For parametrized tests, pytest creates one node id per case.

Example pattern:

```bash
pytest -vv -rP -s tests/test_math.py::test_add[positive-numbers]
```

That is the most precise way to run one parametrized case.

## Recommended shortcuts for T10

Run the single marked test:

```bash
pytest -vv -rP -s -m theone
```

Run the exact test by name:

```bash
pytest -vv -rP -s tests/test_basics.py::test_1_a
```

Run both tests from the file:

```bash
pytest -vv -rP -s tests/test_basics.py
```

## Pytest fixture scopes

Fixture scope controls how often pytest creates a fixture object.

Common scopes:

- `function`: created for every test function.
- `class`: created once for all tests in one test class.
- `module`: created once for all tests in one file.
- `package`: created once for all tests in one package.
- `session`: created once for the whole pytest run.

Basic syntax:

```python
import pytest

@pytest.fixture(scope="function")
def calculator_data():
	# Use function scope when each test must start with clean data
	return {"a": 10, "b": 20}
```

Example with `session` scope:

```python
import pytest
from pathlib import Path

@pytest.fixture(scope="session")
def calculator_script() -> Path:
	return Path(__file__).resolve().parents[1] / "application" / "calculator.py"
```

How to choose a scope:

- Use `function` for maximum isolation and safest tests.
- Use `module` when setup is expensive and can be shared inside one file.
- Use `session` for very expensive setup shared by the whole suite, like one API client or one database container.

Important tradeoff:

- Bigger scope is faster.
- Smaller scope is safer.
- If shared state can leak between tests, prefer `function` scope.

Example with setup and teardown:

```python
import pytest

@pytest.fixture(scope="module")
def api_client():
	client = create_client()
	yield client
	client.close()
```

In this example, `api_client` is created once per test module and closed after all tests in that file finish.

Typical QA automation rule:

- Start with `function` scope.
- Move to `module` or `session` only when setup time is clearly too expensive.