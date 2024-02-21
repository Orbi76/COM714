

class livingThing:
    age = 0
    energy = 0
    name = ""
    def __init__(self, name, age, energy) -> None:
        self.name = name
        self.age = age
        self.energy = energy


    def __repr__(self) -> str:
        return f'Living thig name (name={self.name})'

    def __str__(self) -> str:
        return  f'{self.name} is a living thing.'


    def grow(self) -> None:
        self.age += 1

    def reproduce(self) -> bool:
        if self.energy >= self.reproduceEnergyCost:
            self.energy -= self.reproduceEnergyCost
            return True
        else:
            return False

