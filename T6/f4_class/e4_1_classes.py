# shape, and different shapes, inheritance, and super


# class Square(Shape):
#
#     shape_picture = "▢"
#     # is_square = None ❌
#     square_counter = 0
#
#     def __init__(self, name, color, width, height):
#         super().__init__(name, color, width, height)
#         if width == height and width > 0 and height > 0:
#             """
#             ❌
#             s1 = Square(name = "Crazy square", color="red", width=-5, height=-5)
#             # Square.is_square = False
#             s2 = Square(name = "Lazy square", color="green", width=10, height=10)
#             # Square.is_square = True
#             print(s1) ->
#                     def __str__(self):
#                     if Square.is_square: # Square.is_square = True
#                         return super().__str__() ->
#                              def __str__(self):
#                                 return f"--------------------"
#                                        f"This is a shape:name: {self.name} " \ # BUT s1 was not initialized
#                                          so: AttributeError: 'Square' object has no attribute 'name'
#             """
#             # Square.is_square = True ❌
#             self.is_square = True # ✅
#             self.comment = Square.shape_picture
#             Square.square_counter += 1
#         else:
#             print("----------------")
#             # Square.is_square = False ❌
#             self.is_square = False # ✅
#             self.comment = "NOT A SQUARE SHAPE"
#
#     def count_area(self):
#         if self.is_square: # ✅ # Square.is_square: ❌
#             return self.width * self.height
#         return None


class Shape:

    shape_counter = 0

    def __init__(self, name, color, width, height):
        self.name = name
        self.color = color
        self.width = width
        self.height = height
        Shape.shape_counter += 1
        # print("----------------")

    def __str__(self):
        print("----------------")
        # return f"--------------------\n" \
        return f"This is a shape:\nname: {self.name} \n" \
               f"color: {self.color}, \n" \
               f"width: {self.width} cm, \n" \
               f"height: {self.height} cm, \n"

    @staticmethod
    def how_many_shapes():
        sss = ""
        if Shape.shape_counter > 1:
            sss = "s"
        print(f"======================")
        print(f"We have {Shape.shape_counter} shape{sss}")


class Square(Shape):

    shape_picture = "▢"
    square_counter = 0

    def __init__(self, name, color, width, height):
        super().__init__(name, color, width, height)
        if width == height and width > 0 and height > 0:
            self.is_square = True
            self.comment = Square.shape_picture
            Square.square_counter += 1
        else:
            print("----------------")
            self.is_square = False
            self.comment = "NOT A SQUARE SHAPE"

    def count_area(self):
        if self.is_square:
            return self.width * self.height
        return None

    @staticmethod
    def how_many_squares():
        sss = ""
        if Square.square_counter > 1:
            sss = "s"
        print(f"======================")
        print(f"We have {Square.square_counter} square{sss}")

    def __str__(self):
        if self.is_square:
            return super().__str__() + \
                f"class: {Square.__name__}: {self.comment},\n" \
                f"Area: {self.count_area()} cm²"
        return self.comment


s1 = Square(name = "Crazy square", color="red", width=7, height=7)
s2 = Square(name = "Lazy square", color="green", width=10, height=10)


print(s1)
print(s2)
# print(t1)
Shape.how_many_shapes()
Square.how_many_squares()





