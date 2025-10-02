class Fruit:
    fruit = "fruit"
    _fruit: str = "special_fruit"
    __fruit = "forbidden_fruit"

    def __init__(self, name, country):
        self.name = name
        self.country = country


    def __str__(self):
        return f"This is generally a {Fruit.fruit} and also {self.name} from {self.country}"

    def getter_of_ff(self):
        return Fruit.__fruit

class Pricer(Fruit):
    def __init__(self, name, country, price):
        super().__init__(name, country)
        self.price = price

    def __str__(self):
        return  f"{super().__str__()} and has a price of {self.price}"


f1 = Fruit("apple", "Poland")
f2 = Fruit("orange", "Brasil")
print(f1)
print(f2)
f3 = Pricer("banana", "Chile", 2)
print(f3)
print("===============")
print(f3.fruit)
print(f3._fruit)
#print(f3.__fruit) # AttributeError: 'Pricer' object has no attribute '__fruit'
print(f3._Fruit__fruit)
print(f3.getter_of_ff())
