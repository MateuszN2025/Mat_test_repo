class Auto:
    name = "Auto"
    cena = 10000

    def informacje(self):
        print(f"Name: {self.name}")
        print(f"Cena: {self.cena}")


# Utworzenie instancji klasy
auto = Auto()

print(auto)  # Wyświetli informacje o obiekcie
print(auto.name)  # Wyświetli "Auto"
print(auto.cena)  # Wyświetli 10000
auto.informacje()  # Wywoła metodę informacje()
print("===================================")
print(Auto)  # Wyświetli informacje o obiekcie
print(Auto.name)  # Wyświetli "Auto"
print(Auto.cena)  # Wyświetli 10000
print("===================================")

class Auto2:
    name = "Auto"
    cena = 10000

    @staticmethod
    def informacje():
        print(f"Name: {Auto.name}")
        print(f"Cena: {Auto.cena}")

# Wywołanie
Auto2.informacje()

print("===================================")
class Auto3:
    name = "Auto"
    cena = 10000

    @classmethod
    def informacje(cls):
        print(f"Name: {cls.name}")
        print(f"Cena: {cls.cena}")

# Wywołanie
print("Auto3.informacje()")
Auto3.informacje()
print("a2.informacje()")
a2 = Auto2()
a2.informacje()
