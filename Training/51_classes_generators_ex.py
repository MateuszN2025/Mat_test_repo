class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"This is animal {self.name} which is {self.age} years old"

anima = Animal("henry", 234)

print(anima)

class Dog(Animal):
    def __init__(self, name, age, sound):
        super().__init__(name, age)
        self.sound = sound

    def __str__(self):
        return super().__str__() + f" and make a {self.sound}"

hotdog = Dog("miami", 43434, "hau")

print(hotdog)

class A:
    pass
class B(A):
    pass
class C(A):
    pass
class D(B,C):
    pass
print(D.mro())

a = []
for item in range(0,20,3):
    a.append(item)

print(a)

def gen():
    for j in range(100):
        yield j

b = []

for item2 in gen():
    b.append(item2)

print(b)