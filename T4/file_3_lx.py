def power_to_dict(value: int, input_data: dict = {}) -> dict:
    input_data[str(value)] = value ** 2

    return input_data

nowy_słownik = {}

print(f'1. {power_to_dict(2)}')   # power_to_dict(2) -> {"2": 4}
print(f"2. {power_to_dict(4, {'1': 1})}")  # power_to_dict(4, {'1': 1}) -> {"2": 4, "1": 1, "4" : 16}
print(f'3. {power_to_dict(6)}') # power_to_dict(6) -> {"2": 4, "1": 1, "4" : 16, "6": 36}