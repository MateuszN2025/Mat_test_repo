class Liczba:
    def __init__(self, wartosc):
        self.wartosc = wartosc

    # Dodawanie
    def __add__(self, other):
        return Liczba(self.wartosc + other.wartosc)

    # Metoda __call__ pozwala wywoływać obiekt jak funkcję
    def __call__(self, x):
        return Liczba(self.wartosc + x)

li = Liczba(5)
wynik = li(6)  # Teraz można

# bez

# Metoda __call__ pozwala wywoływać obiekt jak funkcję
# def __call__(self, x):
#     return Liczba(self.wartosc + x)

#  jest problem:
#     wynik = li(6)  # Teraz można
# TypeError: 'Liczba' object is not callable

print(wynik.wartosc)  # 11
wynik = li(7)  # Teraz można
print(wynik.wartosc)  # 12

class Liczba:
    # Konstruktor - inicjalizacja obiektu z wartością
    def __init__(self, wartosc):
        self.wartosc = wartosc

    # Metoda magiczna __add__ - definiuje zachowanie dla operatora '+'
    def __add__(self, other):
        # 'other' to drugi obiekt, który jest dodawany
        # Sumujemy wartości obu obiektów
        # Zwracamy NOWY obiekt Liczba z wynikiem dodawania
        return Liczba(self.wartosc + 2 * other.wartosc)

# Demonstracja
a = Liczba(5)   # Pierwszy obiekt
b = Liczba(3)   # Drugi obiekt
c = a + b       # Równoważne: c = a.__add__(b)


print(c.wartosc)  # 8
print("========")
print(a.__add__(b))
print("========")
print(a.__add__(b).wartosc)
