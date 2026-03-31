class Matematyka:
    # Metoda statyczna
    @staticmethod
    def dodaj(a, b):
        # Nie ma dostępu do instancji ani klasy
        return a + b

    # Metoda statyczna bez dostępu do self/cls
    @staticmethod
    def przywitaj():
        print("Witaj w klasie Matematyka!")

# Wywołanie bez tworzenia instancji
print(Matematyka.dodaj(5, 3))  # 8
Matematyka.przywitaj()  # Witaj w klasie Matematyka!


class Fabryka:
    bazowa_cena = 100

    # Metoda klasy
    @classmethod
    def utworz_premium(cls, dodatek):
        # 'cls' wskazuje na samą klasę
        print(f"cls: {cls}")
        return cls(cls.bazowa_cena + dodatek)

    def __init__(self, cena):
        self.cena = cena

# Użycie metody klasy
produkt_premium = Fabryka.utworz_premium(50)
print(produkt_premium.cena)  # 150

print("===================================")
class Klasa1:
    wartosc_klasy = 10

    # Metoda statyczna
    @staticmethod
    def metoda_statyczna():
        # Brak dostępu do atrybutów klasy/instancji
        # print(f"Metoda statyczna {wartosc_klasy}") # Unresolved reference 'wartosc_klasy'
        print(f"Metoda statyczna")
        # Nie może używać self ani cls

    # Metoda klasy
    @classmethod
    def metoda_klasy(cls):
        # Dostęp do atrybutów klasy
        print(f"Wartość klasy: {cls.wartosc_klasy}")
        # Może modyfikować atrybuty klasy

    # Metoda instancji
    def metoda_instancji(self):
        # Dostęp do atrybutów instancji
        print("Metoda instancji")

ooo = Klasa1()

ooo.metoda_statyczna()
Klasa1.metoda_statyczna()
ooo.metoda_klasy()

Klasa1.metoda_klasy()
# Klasa1.metoda_instancji() # TypeError: metoda_instancji() missing 1 required positional argument: 'self'
ooo.metoda_instancji()