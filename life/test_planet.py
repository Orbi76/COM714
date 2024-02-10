import unittest
from human import Human
from planet import Planet

class TestPlanet(unittest.TestCase):

    def test_add_human(self):

        # check: 0 population
        earth = Planet("Earth")
        self.assertEqual(earth.population(), 0, "Population should be 0.")

        # check: single human
        chuck = Human("Chuck Noland")
        earth.add(chuck)
        self.assertEqual(earth.population(), 1, "Population should be 1.")

        # check: two human
      #  chuck = Human("Chuck Noland")
        wilson = Human("Wilson")
       # earth.add(chuck)
        earth.add(wilson)
        self.assertEqual(earth.population(), 2, "Population should be 2.")

    def test_has(self):

        # check: does not have specified human
        earth = Planet("Earth")
        chuck = Human("Chuck")
        self.assertFalse(earth.has(chuck), "Should be false.")


        # check: has specified human
        earth.add(chuck)
        self.assertTrue(earth.has(chuck), "Should be true.")

    def test_population(self):
        # check: no population
        earth = Planet("Earth")
        self.assertEqual(earth.population(), 0, "Population should be 0.")

        # check: no population of one
        chuck = Human("Chuck")
        earth.add(chuck)
        self.assertEqual(earth.population(), 1, "Population should be 1")







if __name__ == '__main__':
    unittest.main()