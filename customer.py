from order import Order

class Customer:
    def __init__(self, name):
        # Manual check BEFORE setting, to ensure early error
        if not isinstance(name, str) or not name.strip() or len(name) > 19:
            raise ValueError("Name must be a string between 1 and 19 characters.")
        self.name = name  # setter is still called, but this ensures safety

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 19:
            self._name = value
        else:
            raise ValueError("Name must be a string between 1 and 19 characters.")

    def orders(self):
        return [order for order in Order.all_orders if order.customer == self]

    def coffees(self):
        return list({order.coffee for order in self.orders()})

    def create_order(self, coffee, price):
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        customer_spend = {}
        for order in Order.all_orders:
            if order.coffee == coffee:
                customer_spend[order.customer] = customer_spend.get(order.customer, 0) + order.price
        return max(customer_spend, key=customer_spend.get) if customer_spend else None
