def dodawanie(a, b):
    return a + b


print(dodawanie(5, 4))

suma = lambda xxx, yyy: xxx + yyy

print(suma(54, 54))


# Podnoszenie liczb do kwadratu
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # Wynik: [1, 4, 9, 16, 25]