import pytest
from functions_for_tests import dodawanie, odejmowanie, mnozenie
import pytest
import time

@pytest.fixture
def performance_tracker():
    start_time = time.time()
    yield
    end_time = time.time()
    print(f"\nCzas wykonania testu: {end_time - start_time} sekund")

# Używamy parametryzacji Pytest
@pytest.mark.parametrize("a, b, expected", [(1, 2, 3), (2, 3, 5), (4, 5, 9)])
@pytest.mark.nice11
def test_dodawanie(a, b, expected, performance_tracker):
    assert dodawanie(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [(1, 2, 3), (2, 3, 5), (4, 5, 9)])
@pytest.mark.nice11
def test_odejmowanie(a, b, expected, performance_tracker):
    assert odejmowanie(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [(1, 2, 2), (2, 3, 6), (4, 5, 20)])
@pytest.mark.not_nice11
def test_mnozenie(a, b, expected, performance_tracker):
    assert mnozenie(a, b) == expected
