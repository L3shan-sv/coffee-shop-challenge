import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCoffee(unittest.TestCase):
    def setUp(self):
        Order.all_orders = []

    def test_coffee_name_validation(self):
        with self.assertRaises(ValueError):
            Coffee("A")

    def test_num_orders_and_avg_price(self):
        c = Customer("Zara")
        coffee = Coffee("Cappuccino")
        c.create_order(coffee, 4.0)
        c.create_order(coffee, 6.0)
        self.assertEqual(coffee.num_orders(), 2)
        self.assertEqual(coffee.average_price(), 5.0)

    def test_customers(self):
        c1 = Customer("Jake")
        c2 = Customer("Lily")
        coffee = Coffee("Macchiato")
        c1.create_order(coffee, 5.0)
        c2.create_order(coffee, 6.0)
        self.assertEqual(len(coffee.customers()), 2)
