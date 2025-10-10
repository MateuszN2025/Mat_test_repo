from time import sleep


def licz_do_trzech():
    yield 1
    yield 2
    yield 3

# Użycie generatora
for liczba in licz_do_trzech():
    print(liczba)

print("######")
generator = (x for x in range(3))

for liczba in generator:
    print(liczba)

# Zamiast tworzyć dużą listę wszystkich wyników, generator zwraca jeden element na raz.
# ➡️ Dzięki temu można przetwarzać np. miliony rekordów bez zajmowania dużej ilości RAM-u.


# def czytaj_linie(plik):
#     with open(plik, 'r') as f:
#         for linia in f:
#             yield linia.strip()
# Tu generator oddaje linie pliku jedna po drugiej — idealne np. dla dużych logów.


print("######")
# def nieskonczone_liczby():
#     i = 0
#     while True:
#         yield i
#         i += 1
#         sleep(1)
#         print(i)
#
# nieskonczone_liczby()
# Samo wywołanie nieskonczone_liczby() nie uruchamia generatora — ono tylko tworzy obiekt generatora.
# Generator zaczyna działać dopiero wtedy, gdy po nim iterujesz, np. w pętli for lub wywołując next().


from time import sleep

def nieskonczone_liczby():
    i = 0
    while True:
        yield i
        i += 1
        sleep(1)
        print(i)

# Utworzenie generatora
gen = nieskonczone_liczby()

# Iteracja po generatorze
for liczba in gen:
    print("Zwrócono:", liczba)
