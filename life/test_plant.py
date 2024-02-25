import unittest
from plant import Plant

class Test_plant(unittest.TestCase):

    def test_absorb(self):
        suculant1 = Plant("aloe", 1, 50)
        self.assertEqual(suculant1.absorb(5), 55, "Energy increase with the absorb amount.")


