"""
It is also possible to use a list as a queue, where the first element added is the first element retrieved (“first-in, first-out”); however, lists are not efficient
for this purpose. While appends and pops from the end of list are fast, doing inserts or pops from the beginning of a list is slow (because all of the other elements
have to be shifted by one).
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
    def __init__(self, order: Order) -> None:
        """
        Deques are a generalization of stacks and queues (the name is pronounced “deck” and is short for “double-ended queue”).
        Deques support thread-safe, memory efficient appends and pops from either side of the deque with approximately the same
        O(1) performance in either direction.

        :params order: the Order
        """
        self._orders = []
        self._orders_deque = deque([order])

    def add_order(self, order: Order) -> None:
        if self._orders:
            self._orders.append(order)
        else:
            self._orders_deque.append(order)


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