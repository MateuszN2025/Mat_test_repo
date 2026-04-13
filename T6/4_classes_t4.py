# __lt__ # magic methods with books
# @property

class Shape:
    def __init__(self, name, width, height):
        self.name = name
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    def describe(self):
        print(f"{self.name} {self.width} {self.height }")

square = Shape(name="square", width=5, height=5)
print(square.width)
print(square.height)
square.describe()


"""
r = Rectangle(5, 10)
print(r.area())  # 50

# Later in code…
r.width = -20   # no restriction
print(r.area()) # -200 😐 nonsense
"""