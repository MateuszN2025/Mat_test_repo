# Pytest Top 8 To Master First (Calculator Project)

This guide is tailored to your calculator setup in `T11/tests` where commands are executed through `execute_command` and `remote_calc_command`.

## 1. Fixtures (Reusable Setup)
Why first: fixtures remove duplication and keep tests clean.

```python
# tests/conftest.py
import pytest

@pytest.fixture
def calc_cmd(remote_calc_command):
    return remote_calc_command
```

```python
# tests/test_basic_ops.py
from .helpers import execute_command

def test_add(calc_cmd):
    out = execute_command(*calc_cmd, "+", 2, 3)
    assert float(out) == 5.0
```

What to practice:
- Move repeated setup into fixtures.
- Keep test bodies short and focused on assertions.

## 2. Parametrize (Data-Driven Tests)
Why second: calculators are operation+input matrices, so this scales naturally.

```python
import pytest
from .helpers import execute_command

@pytest.mark.parametrize(
    "oper,a,b,expected",
    [
        ("+", 10, 5, 15.0),
        ("*", 10, 5, 50.0),
        ("-", 10, 5, 5.0),
        ("/", 10, 4, 2.5),
    ],
    ids=["add", "mul", "sub", "div"],
)
def test_operations(calc_cmd, oper, a, b, expected):
    out = execute_command(*calc_cmd, oper, a, b)
    assert float(out) == pytest.approx(expected)
```

What to practice:
- Add edge rows: zero, negatives, decimal inputs.
- Always use readable `ids`.

## 3. Assertions + `pytest.approx`
Why third: numeric checks become robust for floating-point behavior.

```python
def test_fraction(calc_cmd):
    out = execute_command(*calc_cmd, "/", 1, 3)
    assert float(out) == pytest.approx(0.333333, rel=1e-4)
```

What to practice:
- Use exact compare for integers.
- Use `approx` for non-terminating or formatted decimals.

## 4. `raises` for Error Cases
Why fourth: a calculator test suite is incomplete without invalid-input behavior.

```python
import subprocess
import pytest
from .helpers import execute_command


def test_divide_by_zero_fails(calc_cmd):
    with pytest.raises(subprocess.CalledProcessError):
        execute_command(*calc_cmd, "/", 10, 0)
```

What to practice:
- Invalid operator.
- Non-numeric input.
- Divide by zero.

## 5. Markers + Selection (`-m`, `-k`)
Why fifth: lets you run just smoke/optimal/slow subsets.

```python
import pytest

@pytest.mark.smoke
def test_smoke_add(calc_cmd):
    ...

@pytest.mark.optimal
def test_optimal_matrix(calc_cmd):
    ...
```

Register markers in `pytest.ini`:

```ini
[pytest]
markers =
    smoke: quick confidence tests
    optimal: broader operation matrix
```

Run examples:

```bash
pytest -m smoke
pytest -m optimal -q
pytest -k "div or mul"
```

What to practice:
- Keep smoke tests very fast.
- Use marker names that reflect intent, not implementation.

## 6. Fixture Scope (Speed Up Test Runs)
Why sixth: remote commands can be expensive; scope helps performance.

```python
import pytest

@pytest.fixture(scope="session")
def remote_calc_command_session(remote_calc_command):
    return remote_calc_command
```

What to practice:
- Use wider scope only for immutable, safe shared setup.
- Keep function scope when state may leak between tests.

## 7. `monkeypatch` for Environment Control
Why seventh: your remote fixture depends on env vars.

```python
def test_remote_fixture_skips_without_password(monkeypatch, request):
    monkeypatch.delenv("CALC_SSH_PASSWORD", raising=False)
    fixture = request.getfixturevalue("remote_calc_command")
    # In your current setup this path triggers skip; run this as behavior check in dedicated tests.
```

Better pattern for isolated testing of env logic:

```python
# Extract env parsing into a helper function and unit-test it with monkeypatch.
```

What to practice:
- `setenv`, `delenv` for deterministic fixture behavior.
- Avoid dependence on machine-local settings in unit tests.

## 8. Capturing Logs/Output (`capsys`, `caplog`)
Why eighth: useful when your command wrapper prints diagnostics.

```python
def test_diagnostic_output(capsys):
    print("[CHECK] add")
    captured = capsys.readouterr()
    assert "[CHECK]" in captured.out
```

What to practice:
- Verify helpful error messages.
- Keep logs readable for CI failures.

---

## 2-Week Practical Plan (Short)
Week 1:
1. Convert all basic operations to parametrized tests with IDs.
2. Add 4-6 error-case tests using `pytest.raises`.
3. Split into `smoke` and `optimal` markers.

Week 2:
1. Add float-sensitive tests with `pytest.approx`.
2. Refactor fixture scopes for speed where safe.
3. Add env-driven behavior checks with `monkeypatch`.
4. Add minimal output checks for diagnostics.

---

## Suggested Starter Files
- `tests/test_basic_ops.py`: happy-path operation matrix.
- `tests/test_errors.py`: invalid input and divide-by-zero.
- `tests/test_marked_smoke.py`: small high-signal smoke set.
- `tests/test_env_behavior.py`: fixture/env behavior with monkeypatch.

This progression gives you reliability first, then speed, then maintainability.
