from collections import deque


class Queue:
    def __init__(self):
        # Initializing an empty queue
        self.buffer = deque()

    def enqueue(self, val):
        # Adding (enqueueing) an item to the queue
        self.buffer.appendleft(val)

    def dequeue(self):
        # Removing (dequeuing) an item from the queue
        return self.buffer.pop()

    # Checking if the queue is empty
    def is_empty(self):
        return len(self.buffer) == 0

    # Checking the size (number of items) in the queue
    def size(self):
        return len(self.buffer)
