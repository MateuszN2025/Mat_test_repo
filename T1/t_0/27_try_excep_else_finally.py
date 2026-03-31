try:
    # kod mogący zgłosić wyjątek
    result = 0 / 0
except ZeroDivisionError as f:
    # obsługa konkretnego wyjątku
    print("Nie można dzielić przez zero")
    print("----------")
    print(f"this is f: {f}")
    print("----------")

except Exception as e:
    # obsługa ogólnego wyjątku
    print(f"Inny błąd: {e}")
else:
    # wykonuje się, gdy nie ma wyjątku
    print("Operacja zakończona sukcesem")
finally:
    # zawsze się wykonuje, niezależnie od wyniku
    print("Kończenie operacji")