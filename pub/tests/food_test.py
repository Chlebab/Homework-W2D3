import unittest
from src.food import Food

class TestFood(unittest.TestCase):

    def setUp(self):
        self.food_1 = Food("burger", 10, 1)
        self.food_2 = Food("sandwich", 5, 1)
        self.food_3 = Food("pasta", 15, 1)
        
