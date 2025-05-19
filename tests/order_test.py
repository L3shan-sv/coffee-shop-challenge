import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestOrder(unittest.TestCase):
    def setUp(self):
        Order.all_orders = []

    def test_valid_order(self):
        c = Customer("Bill")
        coffee = Coffee("Drip")
        order = Order(c, coffee, 4.0)
        self.assertEqual(order.customer, c)
        self.assertEqual(order.coffee, coffee)
        self.assertEqual(order.price, 4.0)

    def test_invalid_price(self):
        c = Customer("Ted")
        coffee = Coffee("Americano")
        with self.assertRaises(ValueError):
            Order(c, coffee, 15.0)

        with self.assertRaises(ValueError):
            Order(c, coffee, 0.5)

        with self.assertRaises(ValueError):
            Order(c, coffee, "free")
