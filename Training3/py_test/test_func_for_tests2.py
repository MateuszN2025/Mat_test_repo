from func_for_tests import fun_sum, p_fix, p_fix2

class TestC:
    def test3(self, p_fix, p_fix2):
        assert fun_sum(p_fix2) == 5

    def test4(self, p_fix, p_fix2):
        assert fun_sum(p_fix2) == 5