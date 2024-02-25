from plant import Plant

class VenusFlytrap(Plant):

    def __init__(self, name, age, energy):
        super().__init__(name, age, energy)

    def catch(self, insect):
        if insect == "fly":
            self.energy += 50
            return self.energy
        elif insect == "bug":
            self.energy += 10
            return self.energy
        else:
            return f"No luck this time. It is not digestible! Still {self.energy} energy left!"
        








