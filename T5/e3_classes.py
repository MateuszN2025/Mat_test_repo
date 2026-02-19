class Car1:
    def __init__(self, name, year):
        self.name = name
        self.year = year

    def __str__(self):
        return f"Car {self.name} from {self.year} year"

    def __repr__(self):
        return f"{self.name},{self.year}"

    def sound(self):
        print("wrrrrrrrr")
        return "ret"


class Fiat(Car1):
    def __init__(self, name, year, power):
        super().__init__(name, year)
        # Call super().__init__ with only the parameters that the parent constructor needs.
        # Child-specific attributes can be assigned before or after the call to super().
        # super() ensures proper initialization of the parent class.
        # only name and year
        # because this is what Car1 __init__ demands
        self.power = power
        # additional from Fiat


    def sound(self):
        print("bzium")
    # without super
    # Car fiat from 1987 year
    # fiat,1987
    # bzium
    # None

    def __str__(self):
        return super().__str__() + f" with power {self.power} hp" + " |FIAT IS THE BEST"
    # with super
    # Car fiat from 1987 year|FIAT IS THE BEST
    # fiat,1987
    # bzium
    # None


c1 = Car1("saab", 2020)
print(c1)
print(repr(c1))
print(c1.sound())

print("--------------")


# c2 = Fiat()
# <__main__.Fiat object at 0x00000151E44B5E20>|FIAT IS THE BEST
# <__main__.Fiat object at 0x00000151E44B5E20>
# bzium
# None

c2 = Fiat("fiat", 1987, 400)
# class Fiat(Car1):
#     def __init__(self, name, year, power):
print(c2)
print(repr(c2))
print(c2.sound())