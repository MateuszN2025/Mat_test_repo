from functions_for_tests import dodawanie

test_data1 = [
    [1,2,3],
    [2,3,5],
    [4,5,12]
]

test_data2 = [
    [1,2,3],
    [2,3,5],
    [4,5,9]
]

def test_1():
    for item in test_data1:
        assert dodawanie(item[0],item[1]) == item[2]

def test_2():
    for item in test_data2:
        assert dodawanie(item[0],item[1]) == item[2]