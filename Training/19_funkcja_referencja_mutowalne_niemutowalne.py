# Typy niemutowalne (int, str, tuple)
def modyfikuj_niemutowalny(x):
    # x = 10  # Tworzy nowy obiekt
    x += 1
    print("Wewnątrz funkcji:", x)

a = 5
modyfikuj_niemutowalny(a)
print("Poza funkcją:", a)  # Wartość nie zmienia się

# Typy mutowalne (list, dict, set)
def modyfikuj_mutowalny(lista1, lista2):
    kopia_listy = lista1.copy()
    kopia_listy.append(4)  # Modyfikacja oryginalnej listy
    lista2.append(223123)
    print("Wewnątrz funkcji:", kopia_listy)


b = [1, 2, 3]
c = ['a', 3, [], 333]
modyfikuj_mutowalny(b, c)
print("Poza funkcją:", b, c)  # Lista zostaje zmieniona