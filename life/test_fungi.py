import unittest
from fungi import Fungi

class Test_fungi(unittest.TestCase):

    def test_scattersSpore(self):
        gomba = Fungi("Champion",1, 70, 7)
        self.assertEqual(gomba.scattersSpores(5),12 , "Fungi spore is 12")

