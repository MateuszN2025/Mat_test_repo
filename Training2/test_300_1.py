
add = lambda x,y: x+y
print(add(3,4))

def test_add():
    # Arrange
    a, b = 2, 3

    # Act
    result = add(a, b)

    # Assert
    assert result == 5
