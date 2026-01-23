class Przyklad:
    # Publiczny atrybut - domyślny, dostępny wszędzie
    public_atrybut = 10

    # Chroniony atrybut - konwencja oznaczania przez '_'
    _chroniony_atrybut = 20

    # Prywatny atrybut - oznaczany przez '__'
    __prywatny_atrybut = 30

    def __init__(self):
        self.publiczny = 1
        self._chroniony = 2
        self.__prywatny = 3

    # Publiczna metoda
    def publiczna_metoda(self):
        print("Publiczna metoda")

    # Chroniona metoda
    def _chroniona_metoda(self):
        print("Chroniona metoda")

    # Prywatna metoda
    def __prywatna_metoda(self):
        print("Prywatna metoda")

obj = Przyklad()

obj.publiczna_metoda()
obj._chroniona_metoda()
obj._Przyklad__prywatna_metoda()
# obj.__prywatna_metoda()  # Błąd