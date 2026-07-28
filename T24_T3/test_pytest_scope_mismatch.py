import pytest

# 1. Function-scoped fixture (default scope)
@pytest.fixture(scope="function")
def user_credentials():
    return {"username": "alice", "password": "password123"}

# 2. Session-scoped fixture attempting to depend on a function-scoped fixture
@pytest.fixture(scope="session")
def authenticated_session(user_credentials):  # <--- Scope mismatch happens here
    # Pytest cannot run this because 'user_credentials' doesn't exist 
    # at the start of the session.
    return f"AuthToken_for_{user_credentials['username']}"

def test_login(authenticated_session):
    assert "AuthToken" in authenticated_session
    
# ScopeMismatch: You tried to access the 'function' scoped fixture 'user_credentials' 
# with a 'session' scoped request fixture 'authenticated_session', 
# we cannot request more limited scope fixtures in broader scope fixtures

# A fixture can only request fixtures of an equal or broader scope:
#   A function fixture can depend on a session fixture.
#   A session fixture CANNOT ⚠️ depend on a function fixture.