import pytest

'''
    request
    It gives you access to:
    -The current test function
    -The test module
    -The test class
    -Markers
    -Fixture scope info
    -Finalizer registration
    -Parametrization data
    It is basically:
    -Context information about the currently running test.
    '''

@pytest.fixture
def resource(request): # request is a built-in pytest fixture.
    print("Setup")

    def ccc_cleanup():
        print("TTTTeardown")

    request.addfinalizer(ccc_cleanup)
    return "Resource" # Everything after return is unreachable.

'''
What happens:
Fixture runs → prints "Setup"
Fixture returns "Resource"
Test runs
After test finishes → pytest calls all finalizers
cleanup() runs → prints "Teardown"
So request.addfinalizer() registers teardown logic.

Pytest stores this cleanup function internally.

4️⃣ Fixture returns value
return "Resource"
Now the test runs.
5️⃣ After test finishes
Pytest calls all registered finalizers.
'''

def test_hi(resource):
    print("Hi")



@pytest.fixture
def fix(request):
    print("-> Start setup")

    def cleannnn():
        print("-> Cleaning resources")

    request.addfinalizer(cleannnn)

    return "-> resources"

def test_hi_2(fix):
    print("test_hi_2")

'''
🏆 Final Rule
Use:
✅ yield for simple setup/teardown
✅ addfinalizer() for dynamic, conditional, or loop-based cleanup

💥 Real-World Example (More Practical)
Imagine:
conn = connect()
cursor = conn.open_cursor()
temp_table = create_table()

If create_table() fails:
conn and cursor still need cleanup.
With addfinalizer(), you can register cleanup right after each step.
'''