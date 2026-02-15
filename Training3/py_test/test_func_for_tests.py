from func_for_tests import \
    fun_sum, p_fix, p_fix2, first, second

def test1(p_fix, p_fix2):
    assert fun_sum(p_fix2) == 5

def test2(p_fix, p_fix2):
    assert fun_sum(p_fix2) == 5

def test_example(second):
    print("Test")
