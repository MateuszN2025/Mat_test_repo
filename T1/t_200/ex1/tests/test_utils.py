import pytest

from src.utils import is_valid_email, calc_sum

# def test_1():
#     assert is_valid_email('sd@.com') == True
#
# def test_missing_dot():
#     assert is_valid_email("user@examplecom") is False


@pytest.fixture
def desc_test():
    print("start test")
    yield
    print("end test")


@pytest.mark.parametrize("a, b, expected", [(10, 20, 30), (121, 213, 334), (12.31, 12.33, 24.64)])
def test_1_calc(a, b, expected, desc_test):
    assert calc_sum(a,b) == expected