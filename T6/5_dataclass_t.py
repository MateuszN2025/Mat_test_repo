from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

"""
This automatically gives you:
__init__(self, name, age)
__repr__
__eq__
"""

p1 = Person("z",14)
print(p1.name)
print(p1.age)
print(p1)

p2 = Person("z",14)
print(p2.name)
print(p2.age)
print(p2)

print(p1.name == p2.name)
print("z" == "z")
print(p1 == p2)