def dekorator_z_argumentami(funkcja):
    def wrapper(*args, **kwargs):
        print("Argumenty:", args, kwargs)
        return funkcja(*args, **kwargs)
    return wrapper

@dekorator_z_argumentami
def suma(a, b):
    return a + b

print(suma(3, 5))  # Wypisze argumenty i wynik