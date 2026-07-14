def power_to_dict(value: int, input_data: dict = {}) -> dict:
    # Domyślny {} tworzony jest tylko raz, w momencie definiowania funkcji —
    # a nie przy każdym jej wywołaniu.
    # Dlatego słownik „pamięta” poprzednie wywołania.
    input_data[str(value)] = value ** 2

    return input_data

nowy_słownik = {}

print(f'1. {power_to_dict(2)}')
# {"2": 4}
print(f"2. {power_to_dict(4, {'1': 1})}")
# Przekazujesz własny słownik {'1': 1}
# Funkcja nie używa domyślnego {} !!!!!!!!!!!!!
# {"1": 1, "4" : 16}
print(f'3. {power_to_dict(6)}')
# {'2': 4, '6': 36}

# 📌 Zasada do zapamiętania
# ❌ Nigdy nie używaj mutowalnych typów jako domyślnych argumentów
# ✅ Używaj None i twórz obiekt w środku funkcji