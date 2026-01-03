"""
Implement the BSTIterator class that represents an iterator over the in-order traversal of a
binary search tree (BST):

BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the
BST is given as part of the constructor. The pointer should be initialized to a non-existent
number smaller than any element in the BST.

boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer,
otherwise returns false.
int next() Moves the pointer to the right, then returns the number at the pointer.
Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will
return the smallest element in the BST.

You may assume that next() calls will always be valid. That is, there will be at least a next number
in the in-order traversal when next() is called.


"""
from typing import Optional
from queue import Queue
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator:

    def _push_from_left(self, node):
        self.stack.append(node)
        if node.left: self._push_from_left(node.left)

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        if root: self._push_from_left(root)

    def next(self) -> int:
        node = self.stack.pop()
        val = node.val
        if node.right: self._push_from_left(node.right)
        return val
        

    def hasNext(self) -> bool:
        return len(self.stack) > 0

def build_tree(input):
    if not input: return None
    fifo = Queue()
    if input[0]: root = TreeNode(input[0])
    fifo.put(root)
    index = 1
    while index < len(input) and not fifo.empty():
        node = fifo.get()
        if input[index] is not None:
            left = TreeNode(input[index])
            node.left = left
            fifo.put(left)
        index += 1
        if index >= len(input) - 1: break
        if input[index] is not None:
            right = TreeNode(input[index])
            node.right = right
            fifo.put(right)
        index += 1
    return root


if __name__ == "__main__":
    input = [7, 3, 15, None, None, 9, 20]
    root = build_tree(input)
    bst_iterator = BSTIterator(root)