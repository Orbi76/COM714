import unittest
from animal import Animal

class TestAnimal(unittest.TestCase):

    def test_grow(self):
        # age should increase by 1.
        dog_alex = Animal("Alex",3, 60)
        self.assertEqual(dog_alex.grow(), 4, "Age should increase by 1.")

    def test_reproduce(self):
        dog_flofy = Animal("Flofy", 3, 80)
        self.assertEqual(dog_flofy.reproduce(), True, "Energy should be 60")

        dog_bob = Animal("Bob", 1, 10)
        self.assertEqual(dog_bob.reproduce(), False, "Cant reproduce")

    def test_eat(self):

        # energy is below 100 and eat more than required

        animal_dog = Animal("Elvis", 7, 50)
        gerSep = Animal("Cesar",2,60)
        print(repr(animal_dog))
        print(repr(gerSep))
        print(str(animal_dog))
        print(str(gerSep))

        # Test the eat method
        new_excess_energy = animal_dog.eat(20)
        # Assert that the new excess energy is as expected
        self.assertEqual(new_excess_energy, 0, "Excess energy should be 0.")

        # Test the eat method
        new_excess_energy = animal_dog.eat(100)
        # Assert that the new excess energy is as expected
        self.assertEqual(new_excess_energy, 70, "Excess energy should be 70.")
        # Test the eat method
        new_excess_energy = animal_dog.eat(20)
        # Assert that the new excess energy is as expected
        self.assertEqual(new_excess_energy, 20, "Excess energy should be 20.")

    def test_move(self):
        pass


if __name__ == '__main__':
    unittest.main()