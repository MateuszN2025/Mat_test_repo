import pytest

from api_func import response_get, response_post
exp_dict = {'userId': 1, 'id': 1, 'title': 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit', 'body': 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto'}

@pytest.fixture
def fix_test():
    print("\nstart test")
    yield
    print("\nstop test")

@pytest.mark.kkk
def test1(fix_test):
    assert response_get.status_code == 200

@pytest.mark.parametrize("a",[202])
def test2(a, fix_test):
    assert response_post.status_code == a

@pytest.mark.kkk
def test3(fix_test):
    assert response_get.json() == exp_dict

"""
@pytest.mark.parametrize(
    "a,b,expected",
    [
        (1, 2, 3),
        (2, 3, 5),
        (10, 5, 15),
    ]
)
def test_add(a, b, expected):
    assert a + b == expected

"""