try:
    # kod mogący zgłosić wyjątek
    result = 10 / 2
except ZeroDivisionError:
    # obsługa konkretnego wyjątku
    print("Nie można dzielić przez zero")
except Exception as e:
    # obsługa ogólnego wyjątku
    print(f"Inny błąd: {e}")
else:
    # wykonuje się, gdy nie ma wyjątku
    print("Operacja zakończona sukcesem")
finally:
    # zawsze się wykonuje, niezależnie od wyniku
    print("Kończenie operacji")