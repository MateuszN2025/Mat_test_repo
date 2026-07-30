import pytest

def adding(x:int = 0 , y:int = 0) -> int:
    print("ℹ️")
    return x + y

@pytest.mark.easy
@pytest.mark.parametrize("a, b, result", ((3, 4, 7),
                                          (5, 6, 11),
                                          (9, 9, 18)))
def test1(a, b, result):
    print("⚠️")
    assert adding(a, b) == result
    
@pytest.mark.hard
def test2_very_easy():
    assert adding(3, 4) == 7
    
# Quick flag meaning:
# -vv → very verbose
# -rP → extra summary info (including passed tests with output)
# -s → do not capture print() output
# -m <expr> → run tests matching marker expression