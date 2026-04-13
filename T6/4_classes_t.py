# shape, and different shapes, inheritance, and super
import math

class Thing:
    # print("THIS IS THING IN GENERAL")
    # Because that line is executed when the class is defined,
    # not when an object is created.
    # Python executes the class body immediately to build the class.
    """
    class Thing:
    x = 5
    print("hello")

    # pseudo-behavior
    namespace = {}
    namespace["x"] = 5
    print("hello")   # runs immediately
    Thing = type("Thing", (), namespace)
    """

    def __init__(self):
        print("========================")
        print("THIS IS THING IN GENERAL")

class Shape(Thing):
    def __init__(self, name, color, is_filled):
        self.name = name
        self.color = color
        self.is_filled = is_filled
        print("-----------")
        super().__init__()

    def describe(self):
        print("--- DESCRIPTION ---")
        print(f"{Shape.__name__}: {self.name}, color: {self.color}, is filled: {self.is_filled}")

# using super() without inheritance from Shape cause inheritance directly from class OBJECT:
# TypeError: object.__init__() takes exactly one argument (the instance to initialize)

class Circle(Shape):
    obj_counter = 0
    def __init__(self, name, color, is_filled, radius):
        super().__init__(name, color, is_filled)
        self.radius = radius
        Circle.obj_counter += 1

    def count_area(self):
        # circumference = 2 * math.pi * self.radius # obwód
        area = math.pi * self.radius ** 2
        return area

    def describe(self):
        # print("-------")
        # print(f"{Circle.__name__}:{self.name}, area: {self.count_area():.2f} cm2")
        # print("-------")
        super().describe()
        print(f"radius: {self.radius} cm, area: {self.count_area():.2f} cm2")


    # def __str__(self):
    #     return f"This is {Circle.__name__} {self.obj_counter}: color: " \
    #            f"{self.color}, filled: {self.is_filled}, radius: {self.radius} cm " \
    #            f"with area of {self.count_area():.2f} cm2"


class Square(Shape):
    obj_counter = 0
    def __init__(self, name, color, is_filled, width):
        super().__init__(name, color, is_filled)
        self.width = width
        Square.obj_counter += 1

    def count_area(self):
        return self.width ** 2

    def describe(self):
        # print("-------")
        # print(f"{Square.__name__}:{self.name}, area: {self.count_area():.2f} cm2")
        # print("-------")
        super().describe()
        print(f"width: {self.width} cm, area: {self.count_area():.2f} cm2")


    # def __str__(self):
    #     return f"This is {Square.__name__} {self.obj_counter}: color: " \
    #            f"{self.color}, filled: {self.is_filled}, width: {self.width} cm " \
    #            f"with area of {self.count_area():.2f} cm2"

def main():
    c1 = Circle(name="circle_1", color="blue", is_filled=True, radius=8)
    c1.describe()


    c2 = Circle(name="circle_2", color="blue", is_filled=True, radius=12)
    c2.describe()


    s1 = Square(name="square_1", color="yellow", is_filled=False, width=4)
    s1.describe()


if __name__ == "__main__":
    main()



