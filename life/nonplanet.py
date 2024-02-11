class NonPlanet:

    def __init__(self, name: str='', population: int = 0):
        self.name = name
        self.population = population

    def __repr__(self):
        return f"NonPlanet(name='{self.name}', population={self.population})"

    def __str__(self):
        return f"This is a non-planet called {self.name} with a population of {self.population}."
