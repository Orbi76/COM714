class Human:
    MAX_ENERGY = 100
    REPRODUCE_ENERGY_COST = 20
    ENERGY_TO_MOVE = 10

    def __int__(self, name: str, age: int = 0, energy: int = 100) -> None:
        self.name = name
        self.age = age
        self.energy = energy


    def __repr__(self) -> str:
        return f'human(name={self.name}, age={self.age}, energy={self.energy})'

    def __str__(self) -> str:
        return f'{self.name} is {self.age} year old with {self.energy}'

    def grow(self) -> None:
        self.age += 1

    def eat(self, amount: int) -> int:
        self.energy += amount
        if self.energy > self.MAX_ENERGY:
            excess_energy = self.energy - self.MAX_ENERGY
            self.energy = self.MAX_ENERGY
            return  excess_energy
        return max(0, amount - self.MAX_ENERGY + self.energy)


    def reproduce(self) -> bool:
        if self.energy >= self.REPRODUCE_ENERGY_COST:
            self.energy -= self.REPRODUCE_ENERGY_COST
            return True
        return False

    def move(self, distance: int) -> bool:
        if self.energy >= self.ENERGY_TO_MOVE:
            self.energy -= distance
            return True
        return False



