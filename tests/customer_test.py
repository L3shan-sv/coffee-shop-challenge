import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCustomer(unittest.TestCase):
    def setUp(self):
        Order.all_orders = []

    def test_customer_name_validation(self):
        with self.assertRaises(ValueError):
            Customer("")

        with self.assertRaises(ValueError):
            Customer("a" * 20)

    def test_create_order(self):
        c = Customer("Ava")
        coffee = Coffee("Espresso")
        order = c.create_order(coffee, 5.0)
        self.assertIn(order, Order.all_orders)

    def test_customer_coffees(self):
        c = Customer("Tom")
        coffee1 = Coffee("Latte")
        coffee2 = Coffee("Mocha")
        c.create_order(coffee1, 4.0)
        c.create_order(coffee2, 5.0)
        c.create_order(coffee1, 6.0)
        self.assertEqual(len(c.coffees()), 2)

    def test_most_aficionado(self):
        c1 = Customer("Mike")
        c2 = Customer("Nina")
        coffee = Coffee("Flat White")
        c1.create_order(coffee, 3.0)
        c2.create_order(coffee, 5.0)
        c2.create_order(coffee, 4.0)
        self.assertEqual(Customer.most_aficionado(coffee), c2)
