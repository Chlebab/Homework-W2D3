import unittest
from src.customer import Customer
from src.drinks import Drink

class TestCustomer(unittest.TestCase):
    
    def setUp(self):
        self.customer = Customer("Marek", 100, 23, 0)
        self.drink_1 = Drink("wine", 15, 1)
        self.drink_2 = Drink("beer", 5, 1)
        self.drink_3 = Drink("vodka", 10, 3)

    def test_customer_has_name(self):
        self.assertEqual("Marek", self.customer.name)

    def test_buy_drink(self):
        self.customer.buy_drink("wine", 15)
        self.assertEqual(85, self.customer.wallet)

    def test_buy_drink(self):
        self.customer.buy_drink("beer", 5)
        self.assertEqual(95, self.customer.wallet)