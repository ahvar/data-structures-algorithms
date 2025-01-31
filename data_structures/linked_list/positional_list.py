# %% [markdown]
# ### Abstract Data Type: The Positional List
# - Provide for a general abstraction of a sequence of elements with the ability to identify the location of an element.
# - A position acts as a marker or token within the broader positional list.
# - numeric indicies are not a good abstraction for describing local position in applications where the index of an entry is changing over time due to insertions/deletions happening earlier in the sequence
# - for example, a word processor uses the abstraction of a `cursor` to describe a position within the document without explicit use of an integer index, allowing operations such as "delete the character at the cursor" or "insert a new character just after the cursor."
#
# #### A Node Reference as Position
# - Direct use of nodes (as in `_DoublyLinkedBase`) would violate object-oriented design principles: abstraction and encapsulation
# - It is simpler if the lower-level manipulation of nodes and reliance on sentienls is hidden from users. This also ensures users cannot invalidate the consistency of the list by mismanaging the linking of nodes.
# - Better encapsulation -> greater flexibility to redesign a data structure: independent `position` abstraction

# %%
from doubly_linked_list import _DoublyLinkedBase


# %% [markdown]
#  - Each method of the positional list ADT runs in worst-case `O(1)` time when implemented with a doubly linked list
#  - Public `Position` class nested within `PositionalList`
#  - To handle redundant `Position` instances, like when `first` and `last` are the same, `Position` defines `__eq__` and `__ne__` methods so `first == last` evaluates to `True`
#  -  The `_validate` method verifies a position is valid. A position maintains a reference to the associated node of the linked list, and also a reference to the list instance containing the specified node
#  - Access methods of `PositionalList` rely on `_validate` to "unwrap" a position and `_make_position` to "wrap" nodes as a `Position`


# %%
class PositionalList(_DoublyLinkedBase):

    class Position:
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            """Return True if other is a Position representing the same location"""
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            """Return True if other does not represent the same location"""
            return not (self == other)

    # ----------------------------- utility method ----------------------------
    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError("p must be proper POsition type")
        if p._container is not self:
            raise ValueError("p does not belong to this container")
        if p._node._next is None:
            raise ValueError("p is no longer valid")
        return p._node

    def _make_position(self, node):
        """Return Position instance for a given node (or None if sentinel)"""
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self, node)

    # -------------------------------- accessors ---------------------------------
    def first(self):
        """Return the first Position in the list (or None if list is empty)"""
        return self._make_position(self._header._next)

    def last(self):
        """Return the last Position in the list (or None if list is empty)"""
        return self._make_position(self._trailer._prev)

    def before(self, p):
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):
        """Generate a forward iteration of the elements of the list"""
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    # -------------------------------- mutators ---------------------------------
    # override inherited version to return Position, rather than Node
    def _insert_between(self, element, predecessor, successor):
        node = super()._insert_between(element, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        return self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        return self._insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, p, e):
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)

    def add_after(self, p, e):
        original = self._validate(p)
        return self._insert_between(e, original, original._next)

    def delete(self, p):
        original = self._validate(p)
        return self._delete_node(original)

    def replace(self, p, e):
        original = self._validate(p)
        old_value = original._element
        original._element = e
        return old_value


# %% [markdown]
# ### Sorting a Positional List
#  - a variable `marker` represents the rightmost position of the currently sorted portion of the list
#  - during each pass we consider the position just past the `marker` as the `pivot` and consider where the
#  `pivot`'s element belongs relative to the sorted position
#  - another variable, `walk`, moves leftward from the `marker` as long as there remains a preceeding element with a value larger than the `pivot`'s

# %%
L = PositionalList()
L.add_first(15)
L.add_first(22)
L.add_first(25)
L.add_last(53)
L.add_last(11)
L.add_last(42)


def insertion_sort(L):
    if len(L) > 1:
        marker = L.first()
        while marker != L.last():
            pivot = L.after(marker)
            value = pivot.element()
            if value > marker.element():
                marker = pivot
            else:
                walk = marker
                while walk != L.first() and L.before(walk).element() > value:
                    walk = L.before(walk)
                L.delete(pivot)
                L.add_before(walk, value)


# %% [markdown]
# #### Case Study: Maintaining Access Frequencies
#  - Model a person's hand in a game of cards
#  - The positional insertion and deletion operations performed relative to a cursor representing the current position in the list of characters.
#  - Additionally, examples such as a web browser that keeps track of a user's most accessed URLs, or a music collection that maintains a list of favorites, maintain a collection of elements while keeping track of the number of times an element is accessed
#  - Elements stored in nonincreasing order of access counts; access by searching the list from the most frequently accessed to the least
#  - `k` most accessed elements == first `k` entries in the list
#
# #### Using the Compositional Pattern
#  - A single object composed of two or more other objects
#  - `_Item`: a nested class storing the element and access count
#  - Maintain favorites list as a `PositionalList` of `item` instances


# %%
class FavoritesList:
    """Elements ordered from frequently accessed to least"""

    # ------------------------------- nested _Item class --------------------------
    class _Item:
        __slots__ = "_value", "_count"

        def __init__(self, element):
            self._value = element
            self._count = 0

    # ------------------------------ public methods -------------------------------
    def __init__(self):
        self._data = PositionalList()

    def __len__(self):
        return len(self._data) == 0

    def is_empty(self):
        return len(self._data) == 0

    def access(self, element):
        position = self._find_position(element)
        if position is None:
            position = self._data.add_last(self._Item(element))
        position.element()._count += 1
        self._move_up(position)

    def remove(self, element):
        position = self._find_position(element)
        if position is not None:
            self._data.delete(position)

    def top(self, k):
        """Generate a sequence of top k elements in terms of access counts"""
        if not 1 <= k <= len(self):
            raise ValueError("Illegal value for k")
        walk = self._data.first()
        for j in range(k):
            item = walk.element()
            yield item._value
            walk = self._data.after(walk)

    # ------------------------------ nonpublic utilities --------------------------
    def _find_position(self, element):
        """Search for element and return its Position (or None if not found)"""
        walk = self._data.first()
        while walk is not None and walk.element()._value != element:
            walk = self._data.after(walk)
        return walk

    def _move_up(self, position):
        """Move item at position earlier in the list based on access count"""
        if position != self._data.first():
            count = position.element()._count
            walk = self._data.before(position)
            if count > walk.element()._count:
                while (
                    walk != self._data.first()
                    and count > self._data.before(walk).element()._count
                ):
                    walk = self._data.before(walk)
                self._data.add_before(walk, self._data.delete(position))


# %% [markdown]
# #### Using a List with the Move-to-Front Heuristic
#  - In many real-life access sequences, once an element is accessed it is more likely to be accessed in the future. Such scenarios are said to possess `locality of reference`
#  - A heuristic attempting to take advantage of the `locality of reference` present in an access sequence is the `move-to-front heuristic`
#  - To apply: each time an element is accessed we move it all the way to the front of the list
