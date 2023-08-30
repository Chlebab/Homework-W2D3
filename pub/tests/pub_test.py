import unittest
from src.pub import Pub
from src.customer import Customer
from src.drinks import Drink 
from src.food import Food

class TestPub(unittest.TestCase):

    def setUp(self):
        self.pub = Pub("Bocian", 0, "wine")
        self.drink_1 = Drink("wine", 15, 1,)
        self.drink_2 = Drink("beer", 5, 1,)
        self.drink_3 = Drink("vodka", 10, 3,)
        self.customer_1 = Customer("Marek", 100, 23, 0)
        self.customer_2 = Customer("Piotrek", 50, 16, 0)
        self.customer_3 = Customer("Alek", 80, 40, 0)
        self.food_1 = Food("burger", 10, 1)
        self.food_2 = Food("sandwich", 5, 1)
        self.food_3 = Food("pasta", 15, 1)

    def test_pub_has_name(self):
        self.assertEqual("Bocian", self.pub.name)

    def test_sell_drink(self):
        self.pub.sell_drink(self.customer_1, "beer", 5, 1)
        self.pub.sell_drink(self.customer_1, "wine", 15, 1)
        self.pub.sell_food(self.customer_1, "burger", 10, 1)
        # self.pub.sell_drink(self.customer_2, "wine", 15, 1)
        # self.pub.sell_drink(self.customer_3, "vodka", 10, 3)
        self.assertEqual(30, self.pub.till)
        self.assertEqual(70, self.customer_1.wallet)
        # self.assertEqual(50, self.customer_2.wallet)
        # self.assertEqual(70, self.customer_3.wallet)
        self.assertEqual(1, self.customer_1.drunkness)
        # self.assertEqual(3, self.customer_3.drunkness)

