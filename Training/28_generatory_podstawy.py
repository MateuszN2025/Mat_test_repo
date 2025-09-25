# Poprawiony generator
def generator_liczb(n):
    for i in range(n):
        yield i  # Zwraca wartość, a nie drukuje

# Poprawiona funkcja listy
def lista_liczb(n):
    wynik = []
    for i in range(n):
        wynik.append(i)
    return wynik

# Różnice w pamięci
import sys

# Generator - małe zużycie pamięci
gen = generator_liczb(1000000)
print(sys.getsizeof(gen))  # Mały rozmiar obiektu generatora

# Wyświetlenie wartości generatora
for liczba in generator_liczb(5):
    print(liczba)

# Lista - duże zużycie pamięci
lista = lista_liczb(1000000)
print(sys.getsizeof(lista))  # Duży rozmiar listy

# Wyświetlenie wartości listy
print(lista_liczb(5))

"""
# Duży plik - generator
def czytaj_duzy_plik(nazwa_pliku):
    with open(nazwa_pliku, 'r') as plik:
        for linia in plik:
            yield linia.strip()

# Przetwarzanie bez wczytywania całego pliku
for linia in czytaj_duzy_plik('bardzo_duzy_plik.txt'):
    # Przetwarzanie linii bez ładowania całego pliku
    print(linia)
"""
print("===================================")

# Return - funkcja kończy działanie
def funkcja_return(n):
    for i in range(n):
        return i  # Zwraca tylko pierwszą wartość i kończy

# Yield - funkcja tworzy generator
def funkcja_yield(n):
    for i in range(n):
        yield i  # Zwraca kolejne wartości

# Porównanie
print(funkcja_return(5))  # 0
print(list(funkcja_yield(5)))  # [0, 1, 2, 3, 4]
