import pytest

# In pytest, use one test function and feed multiple input/expected sets
# via @pytest.mark.parametrize, so each case is reported separately.
@pytest.mark.parametrize(["a", "b", "result"],
                         ((1, 2, 3),
                          (2, 3, 5),
                          (4, 5, 9),
                          (6, 7, 13),
                          (8, 9, 17)))
def test_1(a, b, result):
    assert a + b == result
    
@pytest.mark.easy
def test_sum_cases_plain_loop():
    cases = [(1, 2, 3), (2, 3, 5)]
    for a, b, expected in cases:
        assert a + b == expected


@pytest.fixture
def user(request):
    role = request.param
    return {"role": role}


@pytest.mark.parametrize("user,expected",
                         [("admin", 200), ("guest", 403)], indirect=["user"])
def test_access(user, expected):
    status = 200 if user["role"] == "admin" else 403
    assert status == expected
    
    
@pytest.fixture(scope="session")
def logged_in_user():
    # pseudo-login: create a user/session object once per test session
    user = {"username": "qa_user", "token": "fake-token"}
    print("Logging in", user["username"])
    yield user
    print("Logging out", user["username"])


def test_verify_user(logged_in_user):
    assert logged_in_user["token"]
    # It means:
    # take the value of logged_in_user["token"]
    # pass if it is truthy (for example, "fake-token")
    # fail if it is falsy (for example, "", None, 0, False)


def test_verify_admin(logged_in_user):
    assert logged_in_user["username"] == "qa_user"
