

class LivingThing:
    # reproduceEnergyCost = 10
    REPRODUCE_ENERGY_COST = 20
    def __init__(self, name: str, age: int = 0, energy: int = 100) -> None:
        self.name = name
        self.age = age
        self.energy = energy


    def __repr__(self) -> str:
        return f'Living thing name (name={self.name}), age {self.age} and energy {self.energy}'

    def __str__(self) -> str:
        return  f'{self.name} is a living thing which is {self.age} old with {self.energy} level.'


    def grow(self) -> int:
        self.age += 1
        return self.age

    def reproduce(self) -> bool:
        if self.energy >= LivingThing.REPRODUCE_ENERGY_COST:
            self.energy -= LivingThing.REPRODUCE_ENERGY_COST
            return True
        else:
            return False

