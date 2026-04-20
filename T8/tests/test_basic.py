import functions as f

def test_1():
    result = f.run_operation(operation="*", number_a=10, number_b=23)
    print(type(result))
    print(result)
    expected_result = 10 * 23
    print(type(expected_result))
    print(expected_result)
    # assert expected_result == result

test_1()