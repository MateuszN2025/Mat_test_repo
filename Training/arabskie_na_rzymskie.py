def arabic_to_roman(num):
    if not (0 < num <= 10000):
        return "Liczba spoza zakresu (1–10000)"

    # Specjalny przypadek dla 10000 (nie ma standardowego zapisu)
    if num == 10000:
        return "ↂ"  # symbol oznaczający 10 000 (czasem używany)

    roman_numerals = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]

    result = ""
    for value, symbol in roman_numerals:
        while num >= value:
            result += symbol
            num -= value
    return result


# --- Główna część programu ---
if __name__ == "__main__":
    try:
        liczba = int(input("Podaj liczbę (1–10000): "))
        print(f"Liczba rzymska: {arabic_to_roman(liczba)}")
    except ValueError:
        print("Błąd: podaj poprawną liczbę całkowitą.")
