from life.planet import Planet
from life.nonplanet import NonPlanet

class Universe:

    def __init__(self, name: str = ''):
        self.__name = name
        self.__planets = []
        self.__non_planets = []


 #   def __repr__(self):
 #       return f"Univers has (name='{self.__planets}' planets)"

 #   def __str__(self):
 #       return f"This universe has something."


    def generate(self,name: str = '') -> Planet:
        planet = Planet(name)
        self.__planets.append(planet)
        return planet

    def generate2(self, entity_type: str, name: str ='', population: int = 0):
        if entity_type == 'planet':
            planet = Planet(name)
            self.__planets.append(planet)
            return planet
        elif entity_type == 'non-planet':
            non_planet = NonPlanet(name, population)
            self.__non_planets.append(non_planet)
            return non_planet


    def display(self) -> None:
        for planet in self.__planets:
            print(planet)

    def display2(self):
        print("Planets:")
        for planet in self.__planets:
            print(planet)
        print("\nNon-Planets:")
        for non_planet in self.__non_planets:
            print(non_planet)

    def __repr__(self):
        return f"Universe(name='{self.__name}', planets={self.__planets}, non_planets={self.__non_planets})"

    def __str__(self):
        return f"This is the {self.__name} universe with {len(self.__planets)} planets and {len(self.__non_planets)} non-planets."


    def numberOfPlanets(self) -> int:
        return len(self.__planets)


    def get_name(self) -> str:
        return  self.__name


vilag = Universe("Vilag")
univ = Universe("Univ")

planet1 = vilag.generate("Earth")
planet2 = vilag.generate("Mars")
planet3 = vilag.generate("Jupiter")
planet4 = vilag.generate("Neptunus")
planet5 = univ.generate2("planet", "Venus", 20)
planet6 = univ.generate2("planet", "Pluto", 30)
planet7 = univ.generate2("non-planet", "Pluttto", 30)
planet1.add("Gabor")
planet1.add("Gabor2")
planet1.add("Gabor3")


#vilag.display()
print ( "Hello. This", vilag._Universe__name, "univers has", vilag.numberOfPlanets(), "planet(s)!", )
print ( "Hello. This", vilag.get_name(), "univers has", vilag.numberOfPlanets(), "planet(s)!", )
vilag.display2()
univ.display2()

#print(repr(vilag))
#print(str(vilag))
