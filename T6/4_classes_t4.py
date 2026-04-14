# @property

# class Shape:
#
#     is_proceeding_w = None
#     is_proceeding_h = None
#
#     def __init__(self, name, width, height):
#         self.name = name
#         self._width = width
#         self._height = height
#
#     @property
#     def width(self):
#         if self._width <= 0:
#             print("width can't be negative")
#             Shape.is_proceeding_w = False
#         else:
#             Shape.is_proceeding_w = True
#             return self._width
#
#     @property
#     def height(self):
#         if self._height <= 0:
#             print("height can't be negative")
#             Shape.is_proceeding_h = False
#         else:
#             Shape.is_proceeding_h = True
#             return self._height
#
#     def describe(self):
#         print(f"{Shape.is_proceeding_w} {Shape.is_proceeding_h}")
#         if Shape.is_proceeding_w and Shape.is_proceeding_h:
#             print(f"{self.name} {self.width} {self.height}")
#             print(f"Area: {self.width * self.height} cm²")
#         else:
#             print("cannot proceed - at least one dimension is negative")


# class Shape:
#     def __init__(self, name, width, height):
#         self.name = name
#         self.width = width
#         self.height = height
#
#     def is_valid(self):
#         return self.width > 0 and self.height > 0
#
#     def describe(self):
#         if self.width <= 0:
#             print("width can't be negative")
#         if self.height <= 0:
#             print("height can't be negative")
#
#         if self.is_valid():
#             print(f"{self.name} {self.width} {self.height}")
#             print(f"Area: {self.width * self.height} cm²")
#         else:
#             print("cannot proceed - at least one dimension is negative")

# class Shape:
#     def __init__(self, name, width, height):
#         self.name = name
#         self._width = width
#         self._height = height
#
#     @property
#     def width(self):
#         if self._width <= 0:
#             print("width can't be negative")
#             return None
#         else:
#             return self._width
#
#     @property
#     def height(self):
#         if self._height <= 0:
#             print("height can't be negative")
#             return None
#         else:
#             return self._height
#
#     def describe(self):
#         w = self.width  # type(Shape.width) <class 'property'>
#         h = self.height # type(self.width)  <class 'int'>
#         print(f"type(Shape.width) {type(Shape.width)}")
#         print(f"type(self.width) {type(self.width)}")
#
#         """
#         Key takeaway
#             👉 @property = method that behaves like an attribute
#             👉 Class access → gives the property object
#             👉 Instance access → executes the method
#         """
#
#         if w is not None and h is not None:
#             print(f"{self.name} {w} {h}")
#             print(f"Area: {w * h} cm²")
#         else:
#             print("cannot proceed - at least one dimension is negative")
#
#
# square = Shape(name="square", width=5, height=5)
# square.describe()


class Shape:

    def __init__(self, name, width, height):
        self.name = name
        self._width = width
        self._height = height
        self.maybe_reset = True

    @property
    def width(self):
        if self._width <= 0:
            print("width can't be negative")
            return None
        else:
            return self._width

    @property
    def height(self):
        if self._height <= 0:
            print("height can't be negative")
            return None
        else:
            return self._height

    @width.setter
    def width(self, value):
        if value <= 0:
            print("width can't be negative")
        else:
            self._width = value

    @width.deleter
    def width(self):
        if self.maybe_reset:
            print("Resetting width")
            self._width = 0
        else:
            print("Deleting width")
            del self._width

    @height.setter
    def height(self, value):
        if value <= 0:
            print("height can't be negative")
        else:
            self._height = value

    @height.deleter
    def height(self):
       if self.maybe_reset:
           print("Resetting width")
           self._height = 0
       else:
           print("Deleting width")
           del self._height

    def describe(self):
        w = self.width  # type(Shape.width) <class 'property'>
        # calls getter → returns value
        h = self.height # type(self.width)  <class 'int'>

        if w is not None and h is not None:
            print(f"{self.name} {w} {h}")
            print(f"Area: {w * h} cm²")
        else:
            print("cannot proceed - at least one dimension is negative")


square = Shape(name="square", width=5, height=5)
square.describe()

# With @property setters, you assign like a normal attribute:
square.width = -10 # calls setter
square.height = -10 # calls setter
square.describe()

# square.width(10)
# ❌ tries to call returned value

del square.width
del square.height
square.describe()

# square.width        # getter
# square.width = 10   # setter
# del square.width    # deleter



"""
r = Rectangle(5, 10)
print(r.area())  # 50

# Later in code…
r.width = -20   # no restriction
print(r.area()) # -200 😐 nonsense
"""