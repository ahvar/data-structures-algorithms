# %% [markdown]
# ## Implementing a Queue with a Singly Linked List
# We will enqueue elements at the back, and dequeue them from the front: First In First Out (FIFO). We cannot easily delete the last node of a singly linked list, even with the tail reference, because we must be able to access the node before the last node
#
# - When `dequeue` is invoked on a queue with one element, we are simultaneously removing the tail of the list, so set `self._tail` to `None`

# %%
from typing import Optional


class Empty(Exception):
    def __init__(self, *args):
        super().__init__(*args)


class LinkedQueue:
    """FIFO queue implementation using a singly linked list"""

    class _Node:
        __slot__ = "_element", "_next"

        def __init__(self, element: Optional["element"], next: Optional["_Node"]):
            self._element = element
            self._next = next

    def __init__(self) -> None:
        self._head = None
        self._size = 0
        self._tail = None

    def __len__(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self._size == 0

    def first(self) -> Optional["_Node._element"]:
        if self.is_empty():
            raise Empty("Empty Queue")
        return self._head._element

    def dequeue(self) -> Optional["_Node._element"]:
        if self.is_empty():
            raise Empty("Empty Queue")
        element = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return element

    def enqueue(self, element: Optional["_Node._element"]) -> None:
        newest = self._Node(element=element, next=None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
            self._tail = newest
            self._size += 1
