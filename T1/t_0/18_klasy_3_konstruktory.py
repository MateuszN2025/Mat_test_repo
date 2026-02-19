class samochod_zwykły:
    nazwa = 'samochod'
    przebieg = 100

    def opis(self):
        print(f'nazwa: {self.nazwa}, przebieg {self.przebieg}')


przeciętne_auto = samochod_zwykły()
przeciętne_auto.opis()

print("===================================")

class samochod_mod():
    def __init__(self, nazwa, przebieg):
        self.nazwa = nazwa
        self.przebieg = przebieg
        self.cena = 888888

    zawory = 12

    kolor = 'czerwony'

    def opis_mod(self):
        print(f'nazwa: {self.nazwa}, przebieg {self.przebieg}')

    def opis_szczegolowy(self):
        print(f'Ilość zaworów : {self.zawory}')
        return "return z opis_szczegolowy"


niezwykle_auto = samochod_mod('pontiac', 22323)
niezwykle_auto.opis_mod()
niezwykle_auto.opis_szczegolowy()

print("===================================")

class samochod_super(samochod_mod):
    def __init__(self, nazwa, przebieg):
        ######################################################################
        # self.nazwa = nazwa
        # self.przebieg = przebieg
        # AttributeError: 'samochod_super' object has no attribute 'cena'
        ######################################################################
        # Solution:
        super().__init__(nazwa, przebieg)

    def __str__(self):
        return f'nazwa: {self.nazwa}, przebieg {self.przebieg}'


super_auto = samochod_super('porsze', 911911)
print(super_auto)
print(super_auto.cena)
print(super_auto.opis_szczegolowy())


