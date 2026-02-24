from typing import Optional
from queue import Queue


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def _check(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val != right.val:
            return False
        return self._check(left.left, right.right) and self._check(
            left.right, right.left
        )

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        return self._check(root.left, root.right)


def build_tree(input):
    fifo = Queue()
    root = TreeNode(input[0])
    fifo.put(root)
    index = 1
    while index < len(input) and not fifo.empty():
        node = fifo.get()
        if input[index] != None:
            left = TreeNode(input[index])
            node.left = left
            fifo.put(left)
        index += 1
        if index >= len(input):
            break
        if input[index] != None:
            right = TreeNode(input[index])
            node.right = right
            fifo.put(right)
        index += 1
    return root


class TestSolution:

    def setup_method(self):
        self.solution = Solution()

    def test_symmetric(self):
        sym = [1, 2, 2, 3, 4, 4, 3]
        root = build_tree(sym)
        assert self.solution.isSymmetric(root) == True
