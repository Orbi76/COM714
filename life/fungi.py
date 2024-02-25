from livingThing import LivingThing

class Fungi(LivingThing):
    def __init__(self, name, age=0, energy=100, spore_count=0):
        super().__init__(name, age, energy)
        self.spore_count = spore_count

    def scattersSpores(self, spore) -> int:
        self.spore_count += spore
        return self.spore_count




