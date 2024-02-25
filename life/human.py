from typing import List
from clothing import Clothing
from animal import Animal


class Human(Animal):
    MAX_ENERGY = 100
    MIN_ENERGY = 20
    REPRODUCE_ENERGY_COST = 10
    ENERGY_TO_MOVE = 10


    def __init__(self, name: str, age: int = 0, energy: int = 100) -> None:
        # the undefault arguments has to be before the default arguments.

        super().__init__(name, age, energy)
        self.__clothing = []


    # def __init__(self, name: str, clothing: List[str], age: int = 0,
    #              energy: int = 100) -> None:  # the undefault arguments has to be before the default arguments.
    #
    #     self.name = name
    #     self.clothing = clothing
    #     self.age = age
    #     self.energy = energy

    def __repr__(self) -> str:
        return f'human(name={self.name}, age={self.age}, energy={self.energy}, clothing = {self.clothing})'

    def __str__(self) -> str:
        return f'{self.name} is {self.age} year old with {self.energy} energy and cloths {self.clothing}'

    def grow(self) -> None:
        self.age += 1

    def eat(self, amount: int) -> int:
        self.energy += amount
        if self.energy >= self.MAX_ENERGY:
            excess_energy = self.energy - self.MAX_ENERGY
            self.energy = self.MAX_ENERGY
            return excess_energy
        else:
            return self.energy - self.MAX_ENERGY

            # return max(0, amount - self.MAX_ENERGY + self.energy)
    # def reproduce(self) -> bool:
    #     if self.energy >= self.REPRODUCE_ENERGY_COST:
    #         self.energy -= self.REPRODUCE_ENERGY_COST
    #         return True
    #     else:
    #         return False

    def move(self, distance: int) -> bool:
        if self.energy >= self.ENERGY_TO_MOVE:
            self.energy -= distance
            return True
        else:
            return False

    def dress(self, __clothing: Clothing) -> None:
        self.__clothing.append(__clothing)





