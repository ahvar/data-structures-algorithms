""" """

from linked_list.linked_queue import LinkedQueue

not_implemented = "must be implemented by subclass"


class Tree:
    """Abstract base class representing a tree structure"""

    # --------------- nested Position class -------------------
    class Position:
        """An abstraction representing the location of a single element."""

        def element(self):
            """Return the element stored at this position"""
            raise NotImplementedError(not_implemented)

        def __eq__(self, other):
            """Return True if other Position represents the same location."""
            raise NotImplementedError(not_implemented)

        def __ne__(self, other):
            """Return True if other does not represent the same location."""
            return not (self == other)

    # ----------------- abstract methods that concrete classes must support ---------------
    def root(self):
        """Return Position representing the tree's root (or None if empty)."""
        raise NotImplementedError(not_implemented)

    def parent(self, p):
        """Return Position representing p's parent (or None if p is root)."""
        raise NotImplementedError(not_implemented)

    def num_children(self, p):
        """Return number of children that Position p has."""
        raise NotImplementedError(not_implemented)

    def children(self):
        """Generate an iteration of Positions representing p's children."""
        raise NotImplementedError(not_implemented)

    def __len__(self):
        """Return the total number of elements in the tree."""
        raise NotImplementedError(not_implemented)

    # -------------- concrete methods implemented in this class -------------------
    def is_root(self, p):
        return self.root() == p

    def is_leaf(self, p):
        return self.num_children(p) == 0

    def is_empty(self):
        return len(self) == 0

    def depth(self, p):
        """Return the number of levels separating Position p from the root"""
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def _height1(self):
        """Return the height of the tree."""
        return max(self.depth(p) for p in self.positions() if self.is_leaf(p))

    def _height2(self, p):
        """Return the height of the subtree rooted at Position p."""
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height2(c) for c in self.children(p))

    def height(self, p=None):
        """Return the height of the subtree rooted at Position p.
        If p is None, return the height of the entire tree.
        """
        if p is None:
            p = self.root()
        return self._height2(p)

    def __iter__(self):
        for p in self.positions():
            yield p.element()

    def preorder(self):
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):
                yield p

    def _subtree_preorder(self, p):
        yield p
        for c in self.children(p):
            for other in self._subtree_preorder(c):
                yield other

    def postorder(self):
        if not self.is_empty():
            for p in self._subtree_postorder(self.root()):
                yield p

    def _subtree_postorder(self, p):
        for c in self.children(p):
            for other in self._subtree_postorder(c):
                yield other
        yield p

    def positions(self):
        return self.preorder()

    def breadthfirst(self):
        if not self.is_empty():
            fringe = LinkedQueue()
            fringe.enqueue(self.root())
            while not fringe.is_empty():
                p = fringe.dequeue()
                yield p
                for c in self.children(p):
                    fringe.enqueue(c)
