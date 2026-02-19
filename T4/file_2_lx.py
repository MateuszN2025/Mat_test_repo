def interval_intersection(a, b):
    # Rozpakuj dane
    start1, end1 = a
    start2, end2 = b

    # Krok 1: Sprawdzenie poprawności przedziałów
    if start1 > end1 or start2 > end2:
        return None  # Jeden z przedziałów jest błędny

    # Krok 2: Oblicz początek i koniec przecięcia
    start = max(start1, start2)
    end = min(end1, end2)

    # Krok 3: Sprawdź, czy mają część wspólną
    if start <= end:
        return (start, end)
    else:
        return None


print(interval_intersection(a=(2,8), b=(4, 10)))
print("================")
print(interval_intersection(a=(5, 5), b=(5, 5)))
print("================")
print(interval_intersection((10, 2), (3, 4)))