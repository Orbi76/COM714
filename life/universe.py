from life.planet import Planet

class Universe:

    def __init__(self, name: str = ''):
        self.__name = name
        self.__planets = []


    def __repr__(self):
        return f"Univers has (name='{self.__planets}' planets)"

    def __str__(self):
        return f"This universe has something."


    def generate(self,name: str = '') -> Planet:
        planet = Planet(name)
        self.__planets.append(planet)
        return planet

    def display(self) -> None:
        for planet in self.__planets:
            print(planet)


    def numberOfPlanets(self) -> int:
        return len(self.__planets)


    def get_name(self) -> str:
        return  self.__name


vilag = Universe("Vilag")

planet1 = vilag.generate("Earth")
planet2 = vilag.generate("Mars")

vilag.display()
print ( "Hello. This", vilag._Universe__name, "univers has", vilag.numberOfPlanets(), "planet(s)!", )
print ( "Hello. This", vilag.get_name(), "univers has", vilag.numberOfPlanets(), "planet(s)!", )
