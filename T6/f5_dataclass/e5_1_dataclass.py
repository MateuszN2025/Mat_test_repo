from dataclasses import dataclass

@dataclass
class Human:
    name: str
    age: int

h1 = Human("Jaś", 5)
h2 = Human("Jaś", 6)

print(h1)
print(h2)
print(h1 == h2)