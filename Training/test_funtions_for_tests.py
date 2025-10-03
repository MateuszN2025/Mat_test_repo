import pytest

import functions_for_tests

@pytest.fixture
def fix1():
    return "Start testu"

def test_1(fix1):
    assert functions_for_tests.dodawanie(1,2) == 3

def test_2(fix1):
    assert functions_for_tests.dodawanie(2,2) == 5