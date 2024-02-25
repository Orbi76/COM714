from livingThing import LivingThing

class Animal(LivingThing):
    ENERGY_TO_MOVE: int = 10
    MAX_ENERGY = 100

    def __init__(self, name, age, energy):
        super().__init__(name, age, energy)

    def __repr__(self):
        return f"Anial class: inherited from super Living thing {super().__repr__()} "


    def __str__(self):
        return f"Animal class:str method inherited from super Living thing str {super().__str__()} "

    # def move(self) -> None:
    #     pass

    def move(self, distance: int) -> bool:
        if self.energy >= self.ENERGY_TO_MOVE:
            self.energy -= distance
            move: bool = True
        else:
            move = False
        return move

    def eat(self, amount: int) -> int:
        self.energy += amount
        if self.energy > self.MAX_ENERGY:
            excess_energy = self.energy - self.MAX_ENERGY
            self.energy = self.MAX_ENERGY
            return excess_energy
        else:
             # return self.energy - self.MAX_ENERGY
           return max(0, amount - self.MAX_ENERGY + self.energy)

