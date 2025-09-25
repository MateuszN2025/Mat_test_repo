class osoba:
    name = 'osoba'
    wiek = 2025

    def informacja_osobowa(self):
        print(f"name: {self.name}, wiek: {self.wiek}")


Mietek = osoba()
print(Mietek.name)
Mietek.informacja_osobowa()
print("===================================")


class osoba2:
    name = 'osoba2'
    wiek = 3000

    @staticmethod  # Nie ma dostępu do zmiennych klasowych/instancji bezpośrednio
    def informacje_osobowa2():
        print(f"name: {osoba2.name}, wiek: {osoba2.wiek}")


print(osoba2.name)
osoba2.informacje_osobowa2()

print("===================================")


class osoba3:
    name = 'osoba3'
    wiek = 4444

    @classmethod
    def informacje_osobowe3(cls):
        print(f"name: {cls.name}, wiek: {cls.wiek}")


Wladek = osoba3()
osoba3.informacje_osobowe3()

print("===================================")


class Matematyka:
    mnoznik = 2

    @classmethod
    def podwoj_liczbe(cls, x):
        # Może używać zmiennych klasowych
        return cls.mnoznik * x

    @staticmethod
    def dodaj(a, b):
        # Nie ma dostępu do zmiennych klasowych
        return a + b


# Użycie
print(Matematyka.podwoj_liczbe(5))  # 10
print(Matematyka.dodaj(3, 4))  # 7
