"""
List Operations with:
 - arrays
 - linked lists
 - stacks
 - queues
"""

from collections import deque
from typing import List


class Order:
    def __init__(self, name: str) -> None:
        self._name = name

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name) -> None:
        self._name = name


class OrderManager:
    """
    NOTE:
        In Python it is also possible to use a list as a queue, where the first element added is the first element retrieved (“first-in, first-out”);
        however, lists are not efficient for this purpose. While appends and pops from the end of list are fast, doing inserts or pops from the
        beginning of a list is slow (because all of the other elements have to be shifted by one).
    """

    def __init__(self, order: Order) -> None:
        """
        Deques are a generalization of stacks and queues (the name is pronounced “deck” and is short for “double-ended queue”).
        Deques support thread-safe, memory efficient appends and pops from either side of the deque with approximately the same
        O(1) performance in either direction.

        :params order: the Order
        """
        self._size = 0
        self._orders = []
        self._orders_deque = deque([order])

    def insert_order(self, order: Order) -> None:
        if self._orders:
            self._orders.append(order)
        else:
            self._orders_deque.append(order)

    def add_rush_order(self, order: Order) -> None:
        """
        This implementation creates a new list with additional space for the rush order and adds it.
        Then, all existing orders are moved to the new list. self._orders and self._size are updated.

        :params order: the rush order
        """
        # there are no orders; add this one and increment size
        if not self._size:
            self._orders[0] = order
            self._size += 1
        else:
            # make an empty list with space for the rush order
            new_orders = [None for i in range(self._size + 1)]
            # add the rush order to the front of new_orders
            new_orders[0] = order
            # add existing orders after the rush order in new_orders
            for i in range(self._size):
                new_orders[i + 1] = self._orders[i]
            self._orders = new_orders
            self._size = len(new_orders)

    def add_rush_order_alternate(self, order: Order) -> None:
        """
        Modify self._orders "in place":
         1. Add a None placeholder to indicate an empty spot at the end of self._orders
         2. Point to the end of the list (currently None)
         3. Move all existing orders to the right
         4. When we get to the beginning of self._orders, add the rush order
         5. Update size
        """
        if not self._size:
            self._orders.append(order)
            self._size += 1
        self._orders.append(None)
        right = len(self._orders) - 1
        while right >= 0:
            if right == 0:
                self._orders[right] = order
            else:
                self._orders[right] = self._orders[right - 1]
            right -= 1
        self._size = len(self._orders)

    def delete_order(self, order: Order) -> None:
        if self._orders:
            self._orders.append(order)
        else:
            self._orders_deque.append(order)

    @property
    def orders(self) -> List:
        return self._orders


if __name__ == "__main__":
    fried_rice = Order("fried rice")
    manager = OrderManager()
    manager.add_order(fried_rice)
