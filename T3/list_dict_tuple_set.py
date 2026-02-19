lst = [1, 2, 3]

# dodawanie
lst.append(4)        # koniec
lst.insert(1, 99)    # pod indeks
lst.extend([5,6])    # wiele

# usuwanie
lst.pop()            # ostatni
lst.pop(1)           # pod indeks
lst.remove(2)        # pierwsze wystąpienie
lst.clear()          # wszystko


lst = ["a", "b", "c", "d"]

removed = lst.pop(2)  # usuwa element na indeksie 2 ("c")
print(lst)            # ['a', 'b', 'd']
print(removed)        # 'c'

del lst[1]            # usuwa element na indeksie 1 ("b")
print(lst)            # ['a', 'd']




tpl = (1, 2, 3)

# tuple nie można zmieniać ani dodawać/usunąć elementów
tpl.count(2)          # ile razy 2
tpl.index(3)          # indeks wartości



d = {"a":1, "b":2}

# dodawanie / aktualizacja
d["c"] = 3
d.update({"b":99, "d":4})

# usuwanie
d.pop("a")            # usuwa i zwraca
d.popitem()           # usuwa ostatnią parę
d.clear()             # wszystko

# dostęp
v = d.get("x")        # bez błędu

d = {"a": 1, "b": 2, "c": 3}

removed = d.pop("b")  # usuwa klucz "b"
print(d)              # {'a': 1, 'c': 3}
print(removed)        # 2

del d["c"]            # usuwa klucz "c"
print(d)              # {'a': 1}



s = {1,2,3}

# dodawanie
s.add(4)

# usuwanie
s.remove(2)           # KeyError jeśli brak
s.discard(5)          # bez błędu
s.pop()               # usuwa losowy element
s.clear()             # wszystko

"""# operacje zbiorów
a | b    # union
a & b    # intersection
a - b    # difference
a ^ b    # symmetric difference"""
