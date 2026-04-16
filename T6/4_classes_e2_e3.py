# polymorphism: inheritance, duck typing
# abstarct method
# shapes = [Circle(4), Square(5), Triangle(6,7), Pizza("pepperoni", 15)]

from abc import ABC, abstractmethod

class Shape(ABC):

    shape_counter = 0

    def __init__(self, parameter):
        self.parameter = parameter
        Shape.shape_counter += 1

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def describe(self):
        pass

    # @staticmethod
    # def shape_counter_func():
    #     return f"We have {Shape.shape_counter} shapes in general"

    @classmethod
    def shape_counter_func(cls):
        return f"We have {cls.shape_counter} shapes in general"


class Circle(Shape):

    counter = 0

    def __init__(self, param):
        super().__init__(parameter=param)
        Circle.counter += 1

    def area(self):
        return 3.14 * self.parameter ** 2

    def describe(self):
        # print(f"Object is '{Circle.__name__}'. Area is {self.area()} cm2")
        # This makes it automatically correct even if subclassed further.
        print(f"Object is '{self.__class__.__name__}'. Area is {self.area()} cm2")

    @classmethod
    def shape_counter_func(cls):
        return super().shape_counter_func() + \
            f" but we have {cls.counter} circles"

class Square(Shape):

    counter = 0

    def __init__(self, param):
        super().__init__(parameter=param)
        Square.counter += 1

    def area(self):
        return self.parameter ** 2

    def describe(self):
        # print(f"Object is '{Square.__name__}'. Area is {self.area()} cm2")
        # This makes it automatically correct even if subclassed further.
        print(f"Object is '{self.__class__.__name__}'. Area is {self.area()} cm2")
    @classmethod
    def shape_counter_func(cls):
        return super().shape_counter_func() + \
            f" but we have {cls.counter} squares"


class Pizza:
    def __init__(self, topping, size):
        self.topping = topping
        self.size = size

    # duck typing
    # Pizza does not inherit from other classes but
    # when it has the same method it will call it
    # Because Python only cares that shape has an .area() method — not its type.
    def area(self):
        return 3.14 * self.size ** 2

def main():
    c1 = Circle(6)
    c1.describe()
    c2 = Circle(600)
    c2.describe()
    s1 = Square(10)
    s1.describe()

    print("============== duck ==================")
    p1 = Pizza("cheese", 15)
    shapes = [c1, s1, p1]
    for shape in shapes:
        print(shape, "|", shape.area())
    print("======================================")

    print("---------")
    print(Shape.shape_counter_func())

    print("---------")
    print(Circle.shape_counter_func())

    print("---------")
    print(Square.shape_counter_func())


if __name__ == '__main__':
    main()



