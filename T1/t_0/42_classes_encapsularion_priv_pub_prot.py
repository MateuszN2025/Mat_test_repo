# ############################
# public
class Car:
    def __init__(self, brand):
        self.brand = brand   # public

c = Car("BMW")
print(c.brand)  # ✅ allowed

print("###########################")
# ############################
# protected
class Car:
    def __init__(self, brand):
        self._brand = brand   # protected (by convention)

c = Car("Audi")
print(c._brand)  # ⚠️ possible, but not recommended

print("###########################")
# ############################
# protected
class Car:
    def __init__(self, brand):
        self.__brand = brand   # private

    def get_brand(self):   # getter
        return self.__brand

c = Car("Tesla")
print(c.get_brand())   # ✅ Tesla
# print(c.__brand)     # ❌ AttributeError
print(c._Car__brand)   # ⚠️ possible (name mangling)
