class Zwierze:
    def dzwiek(self):
        pass


class Pies(Zwierze):
    # Nadpisanie metody - polimorfizm
    def dzwiek(self):
        return "Hau hau"


class Kot(Zwierze):
    def dzwiek(self):
        return "Miau"


class Krowa(Zwierze):
    def dzwiek(self):
        return "Muuu"


# Funkcja korzystająca z polimorfizmu
def wydaj_dzwiek(zwierze):
    print(zwierze.dzwiek())


# Użycie
pies = Pies()
kot = Kot()
krowa = Krowa()

wydaj_dzwiek(pies)  # Wypisze "Hau hau"
wydaj_dzwiek(kot)  # Wypisze "Miau"
wydaj_dzwiek(krowa)  # Wypisze "Muuu"
