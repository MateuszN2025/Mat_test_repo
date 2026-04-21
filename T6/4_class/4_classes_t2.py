# polymorphism: inheritance, duck typing
# abstarct method
# shapes = [Circle(4), Square(5), Triangle(6,7), Pizza("pepperoni", 15)]
#


from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return f"{3.14 * self.radius ** 2} cm²"


class Square(Shape):

    def __init__(self, width):
        self.width = width

    def area(self):
        return f"{self.width ** 2} cm²"


class Triangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height


    def area(self):
        return f"{self.width * self.height * 0.5} cm²"

class Q_shape:

    @staticmethod
    def area():
        return f"fake method e.g. of duck typing"
    # no direct inheritance
    # if class has a area method - it will be call anyway

class Q_shape2:

    counter = 0

    def __init__(self):
        Q_shape2.counter += 1

    def area(self):
        return f"fake method e.g. of duck typing"
    # no direct inheritance
    # if class has a area method - it will be call anyway

class Pizza(Circle):

    def __init__(self, topping, size):
        self.topping = topping
        self.size = size
        # soltuion 2:
        super().__init__(radius=self.size)

    # solution 1:
    # def area(self):
    #     return 3.14 * self.size ** 2




pizza1 = Pizza("4cheeses", 20)
pizza1.area() # AttributeError: 'Pizza' object has no attribute 'radius'

q2 = Q_shape2() # instance creation

# shapes = [Circle(5), Square(6), Triangle(6,5), Q_shape, Q_shape2] # Q_shape2 -> TypeError: area() missing 1 required positional argument: 'self'
"""
# WORKS FINE
shapes = [Circle(5), Square(6), Triangle(6,5), Q_shape, q2]
for shape in shapes:
    print(shape.area())
"""

# shapes = [Circle(5), Square(6), Triangle(6,5), Q_shape, Q_shape2()]
shapes = [Circle(5), Square(6), Triangle(6,5), Q_shape, pizza1]
for shape in shapes:
    print(shape.area())

print("------------")
print(Q_shape2.counter)
print("------Q_shape2.counter------")

