class Human:
    _feature_1 = "Has body."
    __feature_2 = "Has secret"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Human with name {self.name} and age {self.age}"

    def getter_of_secret(self):
        return Human.__feature_2

    def setter_of_secret(self):
        Human.__feature_2 = "Gold"
        return Human.__feature_2

    def setter_of_secret_2(self, secret):
        Human.__feature_2 = secret
        return Human.__feature_2

class Worker(Human):
    def __init__(self, name, age, job):
        super().__init__(name, age)
        self.job = job

    def __str__(self):
        return super().__str__() + f" and it is a {self.job}"

h1 = Human("Larry", 26)
print(Human.mro())
h2 = Worker("Barry", 45, "Plumber")
print(h1)
print(h2)
print("#########")
print(h1._feature_1)
print(h2._feature_1)
print("#########")
print(h1._Human__feature_2)
# print(h2._Worker__feature_2) # AttributeError: 'Worker' object has no attribute '_Worker__feature_2'
print(Human._Human__feature_2)
print("#########")
print(h1.getter_of_secret())
print(h2.getter_of_secret())
print("#########")
print(h1.setter_of_secret_2("Silver"))
print(h2.setter_of_secret())
print("#########")
print(h1.getter_of_secret())
print(h2.getter_of_secret())
