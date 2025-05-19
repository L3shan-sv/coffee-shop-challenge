from customer import Customer
from coffee import Coffee
from order import Order

c1 = Customer("Anna")
c2 = Customer("Joe")
latte = Coffee("Latte")
mocha = Coffee("Mocha")

c1.create_order(latte, 4.5)
c1.create_order(mocha, 6.0)
c2.create_order(latte, 5.0)

print("Anna's Coffees:", [c.name for c in c1.coffees()])
print("Latte Orders:", latte.num_orders())
print("Latte Average Price:", latte.average_price())
print("Aficionado for Latte:", Customer.most_aficionado(latte).name)
