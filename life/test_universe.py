import unittest
from human import Human
from planet import Planet
from universe import Universe


class TestUniverse(unittest.TestCase):

    def test_add_planet(self):

        #check empty universe
        vilag = Universe("Vilag")
        self.assertEqual(vilag.numberOfPlanets(), 0, "Planets numbers should be 0.")

        #check planet added to Universe

        planet1 = vilag.generate("Earth")

        self.assertEqual(vilag.numberOfPlanets(), 1, "one planet")

        planet2 = vilag.generate("Mars")
        self.assertEqual(vilag.numberOfPlanets(), 2, "two planet")





if __name__ == '__main__':
    unittest.main()