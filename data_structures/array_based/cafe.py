from collections import deque


class CafeOrderQueue:
    def __init__(self):
        # TODO: Initialize the order queue using deque
        self._order_queue = deque()

    def add_order(self, order_id):
        # TODO: Add an order to the queue
        self._order_queue.appendleft(order_id)

    def serve_order(self):
        # TODO: Serve (remove) the first order in the queue; raise an exception if there are no orders
        return self._order_queue.pop()


cafe_order_queue = CafeOrderQueue()
# TODO: Initialize an instance of CafeOrderQueue

# TODO: Add at least three orders by their ID
cafe_order_queue.add_order(1)
cafe_order_queue.add_order(2)
cafe_order_queue.add_order(3)
cafe_order_queue.add_order(4)

# TODO: Serve an order and print the ID of the order served
order_id = cafe_order_queue.serve_order()
print(order_id)
