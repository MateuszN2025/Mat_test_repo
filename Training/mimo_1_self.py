class Musician:
    def __init__(self, name, instrument):
        self.name = name
        self.instrument = instrument

    def play_instrument(self):
        print(f"{self.name} is playing the {self.instrument}.")

class Band:
    def __init__(self, name):
        self.name = name
        self.musicians = []

    def add_musician(self, musician):
        print(f">>>{musician.name}>>>{musician.instrument}")
        self.musicians.append(musician)

    def perform(self):
        print(f"{self.name} is starting the performance!")
        for musician in self.musicians:
            musician.play_instrument()


guitarist = Musician("John", "guitar")
drummer = Musician("Sarah", "drums")

band = Band("Baangtron")
band.add_musician(guitarist)
band.add_musician(drummer)

band.perform()
print(band.musicians)