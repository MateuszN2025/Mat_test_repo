class Car:
    name = "Car"   # class attribute

    def __init__(self, name=None):
        if name:
            self.name = name   # instance attribute

    def sound(self):
        print(self.name, "rrrr")

c1 = Car()         # no instance attr → uses class attr
c2 = Car("BMW")    # has instance attr → overrides class attr

c1.sound()  # Car rrrr
c2.sound()  # BMW rrrr

class Fiat(Car):
    def sound(self):
        print(self.name, "wwwwwwww")

print("#################")

f1 = Fiat()
f2 = Fiat("Masseratii")

f1.sound()
f2.sound()