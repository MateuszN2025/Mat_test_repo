import pytest


def fun_sum(a:list):
    return sum(a)

'''
In pytest, a fixture is a function that:
Provides setup data or resources for tests
Can optionally clean up after the test
Is reusable across multiple tests
Fixtures help manage:
Test setup
Test dependencies
Resource initialization (DB connections, files, APIs, etc.)
'''

# @pytest.fixture(autouse=True, scope="class")
@pytest.fixture(scope="class")
def p_fix():
    print("start test")
    yield print("in progress")
    print("stop test")

# A yield fixture is:
#
# A pytest fixture that uses yield to separate setup and teardown
# logic in a clean and automatic way.

# @pytest.fixture
# def p_fix2():
#     return [2,3]

@pytest.fixture
def p_fix2():
    print(">>>>>>>>>>>")
    yield [2,3]
    print("<<<<<<<<<<<")


'''
| Scope    | Created             | Destroyed              |
| -------- | ------------------- | ---------------------- |
| function | Before each test    | After each test        |
| class    | Once per test class | After class finishes   |
| -------- | ------------------- | ---------------------- |
🧠 What Is a Test Class Really?
It’s just a container for test functions.
The class just groups related tests.
class TestExample:
    def test_a(self):
        pass
    def test_b(self):
        pass
| -------- | ------------------- | ---------------------- |
| module   | Once per file       | After file finishes    |
| session  | Once per test run   | After all tests finish |
'''

@pytest.fixture
def first(): # higher fixture
    print("First")

@pytest.fixture
def second(first): # lower fixture
    print("Second")

'''
Pytest determines execution order based on dependencies, 
not order of definition.
Rules:
Fixtures are executed before the test.
If fixture A depends on fixture B → B runs first.
Higher scope fixtures run before lower scope fixtures.
'''