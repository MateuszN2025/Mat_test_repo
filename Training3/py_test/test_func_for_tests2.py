from func_for_tests import fun_sum, p_fix, p_fix2

def test1(p_fix2):
    assert fun_sum(p_fix2) == 7

def test2(p_fix2):
    assert fun_sum(p_fix2) == 5