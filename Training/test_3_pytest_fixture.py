import pytest
import time
from functions_for_tests import dodawanie


@pytest.fixture
def performance_tracker():
    # Przed testem: wykonuje kod do yield
    start_time = time.time()
    print(f'\nstart_time {start_time}')
    # ##########################################

    # W teście: podstawia wartość z yield
    yield 3
    # ##########################################

    # Po teście: wykonuje kod po yield
    end_time = time.time()
    print(f'\nend_time {end_time}')
    print(f"\nCzas wykonania testu: {end_time - start_time} sekund")
    # ##########################################


@pytest.mark.parametrize("a, b, expected", [(1, 2, 2)])
def test_dodawanie_z_pomiarem(a, b, expected, performance_tracker):
    assert dodawanie(a, b) == performance_tracker
