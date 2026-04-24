import helpers.helpers_functions as h


def test_1_addition():
    path = "/home/mniedziolka/PP/Mat_test_repo/T10/application/"
    b_script = "b_calc"
    oper = "+"
    a = "343"
    b = "898"
    assert h.execute_command(path, b_script, oper, a, b)
    