"""
Design your implementation of the circular double-ended queue (deque).

Implement the MyCircularDeque class:

 - MyCircularDeque(int k) Initializes the deque with a maximum size of k.
 - boolean insertFront() Adds an item at the front of Deque. Returns true if the operation is successful, or false otherwise.
 - boolean insertLast() Adds an item at the rear of Deque. Returns true if the operation is successful, or false otherwise.
 - boolean deleteFront() Deletes an item from the front of Deque. Returns true if the operation is successful, or false otherwise.
 - boolean deleteLast() Deletes an item from the rear of Deque. Returns true if the operation is successful, or false otherwise.
 - int getFront() Returns the front item from the Deque. Returns -1 if the deque is empty.
 - int getRear() Returns the last item from Deque. Returns -1 if the deque is empty.
 - boolean isEmpty() Returns true if the deque is empty, or false otherwise.
 - boolean isFull() Returns true if the deque is full, or false otherwise.

"""


class MyCircularDeque:

    class _Node:
        __slots__ = "_value", "_prev", "_next"

        def __init__(self, value: None, prev: None, next: None):
            self._value = value
            self._prev = prev
            self._next = next

        def __eq__(self, other) -> bool:
            if not isinstance(other, MyCircularDeque._Node):
                return False
            return self._value == other._value

    def __init__(self, k: int):
        self._head = self._Node(None, None, None)
        self._tail = self._Node(None, self._head, None)
        self._head._next = self._tail
        self._tail._prev = self._head
        self._head._prev = self._tail
        self._tail._next = self._head
        self._capacity = k
        self._size = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        new = self._Node(value, self._head, self._head._next)
        self._head._next._prev = new
        self._head._next = new

        self._size += 1

        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        new = self._Node(value, self._tail._prev, self._tail)
        self._tail._prev._next = new
        self._tail._prev = new
        self._size += 1

        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        delete = self._head._next
        self._head._next = delete._next
        delete._next._prev = self._head
        delete._next = None
        delete._prev = None
        self._size -= 1

        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        delete = self._tail._prev
        delete._prev._next = self._tail
        self._tail._prev = delete._prev
        delete._next = None
        delete._prev = None
        self._size -= 1
        return True

    def getFront(self) -> int:
        return -1 if self.isEmpty() else self._head._next._value

    def getRear(self) -> int:
        return -1 if self.isEmpty() else self._tail._prev._value

    def isEmpty(self) -> bool:
        return self._size == 0

    def isFull(self) -> bool:
        return self._size >= self._capacity

    def __len__(self) -> int:
        return self._size


if __name__ == "__main__":
    k = 10
    obj = MyCircularDeque(k)
    param_1 = obj.insertFront(1)
    param_2 = obj.insertLast(2)
    param_3 = obj.deleteFront()
    param_4 = obj.deleteLast()
    param_5 = obj.getFront()
    param_6 = obj.getRear()
    param_7 = obj.isEmpty()
    param_8 = obj.isFull()
