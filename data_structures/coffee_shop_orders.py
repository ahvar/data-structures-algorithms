from collections import deque
import unittest


class CoffeeShop:
    def __init__(self):
        self._orders = deque(["Latte", "Espresso", "Cappuccino"])

    def place_rush_order(self, drink):
        self._orders.appendleft(drink)

    def place_standard_order(self, drink):
        self._orders.append(drink)

    def move_next_to_end(self):
        self._orders.rotate(3)

    def serve(self):
        return self._orders.popleft()

    def cancel_last_order(self):
        self._orders.pop()

    @property
    def orders(self) -> deque:
        return self._orders


class TestCoffeeShop(unittest.TestCase):
    def setUp(self):
        self.coffee_shop = CoffeeShop()

    def test_place_rush_order(self):
        expected = deque(["frappa", "Latte", "Espresso", "Cappuccino"])
        self.coffee_shop.place_rush_order("frappa")
        self.assertEqual(self.coffee_shop.orders, expected)

    def test_place_standard_order(self):
        expected = deque(["Latte", "Espresso", "Cappuccino", "frappa"])
        self.coffee_shop.place_standard_order("frappa")
        self.assertEqual(self.coffee_shop.orders, expected)

    def test_move_next_to_end(self):
        expected = "Latte"
        self.coffee_shop.move_next_to_end()
        self.assertEqual(self.coffee_shop.orders[3], "Latte")

    def test_serve(self):
        self.assertEqual(self.coffee_shop.serve(), "")

    def test_cancel_last_order(self):
        pass


# TODO: Create a deque for coffee shop orders with initial orders 'Latte', 'Espresso', 'Cappuccino'
orders = deque(["Latte", "Espresso", "Cappuccino"])

# TODO: A new customer orders a 'Mocha', add it to the end of the queue
orders.appendleft("Mocha")

# TODO: Realize a customer wants their 'Latte' order moved to the end of the queue. Implement it.
orders.rotate(1)

# TODO: Process (remove and print) the first order in the queue. Which drink is it?
print(orders.popleft())
