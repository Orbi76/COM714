import unittest
from livingThing import LivingThing

class Test_livingThing(unittest.TestCase):

    def test_grow(self):
        # age should increase by 1.
        thing1 = LivingThing("bird",3, 90)
        self.assertEqual(thing1.grow(), 4, "Age should increase by 1.")

    def test_reproduce(self):
        thing2 = LivingThing("cat", 10, 30)
        self.assertEqual(thing2.reproduce(), True, "Energy should be 10")

        thing3 = LivingThing("fish", 1, 10)
        self.assertEqual(thing3.reproduce(), False, "Cant reproduce")


