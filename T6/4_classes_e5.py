

class SpaceShip:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def __gt__(self, other):
        return self.power > other.power

    def __lt__(self, other):
        return self.power < other.power

    def __eq__(self, other):
        return len(self.name) == len(other.name)


s1 = SpaceShip("Appollo", 5000)
s2 = SpaceShip("Artemid", 6000)

print(s1 > s2)
print(s1 < s2)
print(s1 == s2)