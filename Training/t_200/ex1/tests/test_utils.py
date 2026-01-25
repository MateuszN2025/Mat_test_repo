from src.utils import is_valid_email

def test_1():
    assert is_valid_email('sd@.com') == True

def test_missing_dot():
    assert is_valid_email("user@examplecom") is False