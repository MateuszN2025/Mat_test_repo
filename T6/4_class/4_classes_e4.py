# properties

class Human:
    def __init__(self, name, age, pesel):
        self.name = name
        self.age = age
        if len(str(pesel)) == 11:
            self._pesel = pesel
        else:
            # raise AssertionError("Pesel should have 11 chars ⚠️")
            raise ValueError("PESEL must be exactly 11 digits")

    @property
    def pesel(self):
        return self._pesel

    @pesel.setter
    def pesel(self, new_pesel: int):
        if len(str(new_pesel)) == 11:
            self._pesel = new_pesel
        else:
            # raise AssertionError("Pesel should have 11 chars ❌️")
            raise ValueError("PESEL must be exactly 11 digits")

    @pesel.deleter
    def pesel(self):
        # del self._pesel
        self._pesel = 0


h1 = None

try:
    h1 = Human("Jan", 33, 31233432432)
except ValueError as e:
    print("Oops:", e)

print(h1.name)
print(h1.age)
print(h1.pesel)
h1.pesel = 99999999991
print(h1.pesel)



#################################################


class Car:

    def __init__(self, vin: str):
        self._vin = Car.check_vin(vin)

    @staticmethod
    def check_vin(vin):
        if len(vin) == 4:
            if vin.isdigit():
                return vin
            else:
                raise ValueError("At least 1 char is not a digit")
        else:
            raise ValueError("Incorrect num of chars")

        # if len(vin) != 4:
        #     raise ValueError("Incorrect number of characters")
        # if not vin.isdigit():
        #     raise ValueError("VIN must contain only digits")
        # return vin

    @property
    def get_vin(self): # This works, but it is not Pythonic. You should want: car.vin
        return self._vin

    @get_vin.setter
    def get_vin(self,new_vin):
        self._vin = Car.check_vin(new_vin)

    @get_vin.deleter
    def get_vin(self):
        # self._vin = "0"
        self._vin = None

print("---------------")
c = Car("0323")
print(c.get_vin)
c.get_vin = "4454"
print(c.get_vin)
del c.get_vin
print(c.get_vin, "<=== del")
print("---------------")
c = Car("1112")
c.get_vin = "4145"





































