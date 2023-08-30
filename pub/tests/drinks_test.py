import unittest
from src.drinks import Drink

class TestDrink(unittest.TestCase):

    def setUp(self):
        self.drink_1 = Drink("wine", 15, 1)
        self.drink_2 = Drink("beer", 5, 1)
        self.drink_3 = Drink("vodka", 10, 3)
#drinks = [beer, vodka, wine]
