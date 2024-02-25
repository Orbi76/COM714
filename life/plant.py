from livingThing import LivingThing

class Plant(LivingThing):
    #
    # def __init__(self) -> None:
    #     pass
    #
    # def __repr__(self) -> str:
    #     return f'Plant repr def'
    #
    # def __str__(self) -> str:
    #     return f'Plant str def'


    def __init__(self, name, age, energy):
        super().__init__(name, age, energy)

    def __repr__(self):
        return f"Plant class: inherited from super Living thing {super().__repr__()} "


    def __str__(self):
        return f"Plant class:str method inherited from super Living thing str {super().__str__()} "

    def absorb(self, amount: int) -> int:
        self.energy += amount
        return self.energy

