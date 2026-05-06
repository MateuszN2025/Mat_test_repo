import pytest

@pytest.mark.usefixtures("f_module")
def test_a():
    pass

@pytest.mark.usefixtures("f_module")
def test_b():
    pass


class TestGroup:
    def test_c(self, f_class):
        pass

    def test_d(self, f_class):
        pass


def test_e(f_session):
    print(f"id(f_session): {id(f_session)}")
    print(f"ℹ️ {f_session['aaa']}")
    print(f"ℹ️ {f_session['bbb']}")
    pass

def test_f(f_session):
    print(f"id(f_session): {id(f_session)}")
    print(f"ℹ️ {f_session['aaa']}")
    print(f"ℹ️ {f_session['bbb']}")
    pass

# scope="function": test_e gets one fresh fixture, test_f gets another fresh fixture
# scope="session": test_e and test_f get the same fixture INSTANCE ❗


def test_g(f_function):
    print(f"id(f_session): {id(f_function)}")
    print(f"ℹ️ {f_function['ccc']}")
    print(f"ℹ️ {f_function['ddd']}")
    pass

def test_h(f_function):
    print(f"id(f_session): {id(f_function)}")
    print(f"ℹ️ {f_function['ccc']}")
    print(f"ℹ️ {f_function['ddd']}")
    pass


def test_i(f_package):
    pass

def test_j(f_package):
    pass