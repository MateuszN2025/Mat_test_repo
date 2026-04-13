#  @staticmethod
# Why this is useful (practical reasoning)
# Keeps related logic grouped inside the class
# Avoids polluting global functions
# Makes code more readable and maintainable
# Clearly signals: “this method doesn’t depend on object state”
# @classmethod


class Animal:

    animal_counter = 0

    def __init__(self, aaa):
        self.aaa = aaa
        Animal.animal_counter += 1

    def __str__(self):
        return f"{self.aaa}"

    # Use @staticmethod when:
    # You don’t need class or instance info
    # It’s just a utility function

    @staticmethod
    def get_animal_num():
        print(f"|{Animal.__name__}|We have {Animal.animal_counter} animals")

    # this will work: zxy is not a usual name but can be
    # @classmethod
    # def get_animal_num_alternative(zxy):
    #     print(f"We have {zxy.animal_counter} animals. How nice.")

    # Use @classmethod when:
    # You need to work with the class
    # You want inheritance to behave correctly
    # You might override class variables

    @classmethod
    def get_animal_num_alternative(cls, kind = " Animals"):
        print("------------------")
        # print(f"[{cls.__name__}] We have {cls.animal_counter} animals. How nice.")
        return f"[{cls.__name__}] We have {cls.animal_counter} animals. How nice." + kind




class Dog(Animal):

    animal_counter = 0

    def __init__(self):
        super().__init__(aaa="Dog")
        Dog.animal_counter += 1

    def __str__(self):
        return super().__str__() + " and WOW!"

    @classmethod
    def get_animal_num_alternative(cls, kind=" DOGS"):
        # super().get_animal_num_alternative()
        # print("DOGS !!!")
        # print("------------------")
        return super().get_animal_num_alternative(kind)

class Cat(Animal):

    animal_counter = 0
    c = "CATS"

    def __init__(self):
        super().__init__(aaa="Cat")
        Cat.animal_counter += 1

    def __str__(self):
        return super().__str__() + " and MEOW!"

    @classmethod
    def get_animal_num_alternative(cls, kind=" CATS"):
        # super().get_animal_num_alternative()
        # print("CATS !!!")
        # print("------------------")
        return super().get_animal_num_alternative(kind)


print(Cat())
print(Cat())
print(Cat())
print(Dog())
print()

Animal.get_animal_num()
print(Animal.get_animal_num_alternative())


Dog.get_animal_num()
print(Dog.get_animal_num_alternative())


Cat.get_animal_num()
print(Cat.get_animal_num_alternative())
