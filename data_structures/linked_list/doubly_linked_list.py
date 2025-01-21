# %% [markdown]
# ### Doubly Linked Lists
#  - singly linked lists do not provide an efficient method for deleting a node from the list tail or an arbitrary node from the list interior because we cannot determine the node that immediately precedes the node to be deleted
#  - Sentinel Nodes: header and trailer nodes, which do not store elements of primary sequence
#  - In an empty list, the `next` field of the header points to the trailer the `prev` field of the trailer points to the header


# %%
class _DoublyLinkedBase:

    class _Node:
        __slot__ = "_element", "_prev", "_next"  # streamline memory

        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next

    def __init__(self):
        """Create empty list"""
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, element, predecessor, successor):
        newest = self._Node(element, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None  # deprecate node
        return element


# %% [markdown]
# ### Implementing a Deque (doubly-ended queue) with a Doubly Linked list; Inheriting from _DoublyLinkedBase
#  - With the use of sentinels, the `header` does not store the first element of the deque and the `trailer` does not store the last
#  - Use inherited `_insert_between` method to insert at either end of the deque
#  - Use inherited `_delete_node` method to remove an element from a nonempty deque, knowing that the designated node is assured to have neighbors on each side


# %%
class Empty(Exception):
    """"""


class LinkedDeque(_DoublyLinkedBase):

    def first(self):
        """Return but do not remove the element at the front of the deque"""
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._header._next._element

    def last(self):
        if self.is_empty():
            raise Empty("Deque is empty")

    def insert_first(self, element):
        self._insert_between(element, self._header, self._header._next)  # after header

    def insert_last(self, element):
        self._insert_between(element, self._trailer._prev, self._trailer)

    def delete_first(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._delete_node(self._header._next)

    def delete_last(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._delete_node(self._trailer._prev)
