class Order:
    all_orders = []

    def __init__(self, customer, coffee, price):
        if not hasattr(customer, 'name') or not hasattr(coffee, 'name'):
            raise TypeError("Invalid customer or coffee.")
        if not isinstance(price, float) or not (1.0 <= price <= 10.0):
            raise ValueError("Price must be a float between 1.0 and 10.0.")

        self._customer = customer
        self._coffee = coffee
        self._price = price

        Order.all_orders.append(self)

    @property
    def price(self):
        return self._price

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee
