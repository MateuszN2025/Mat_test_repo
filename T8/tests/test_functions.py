import functions as f


def test_1():
    result = f.run_operation(operation="*", number_a=10, number_b=23)
    expected_result = 10 * 23
    assert expected_result == result