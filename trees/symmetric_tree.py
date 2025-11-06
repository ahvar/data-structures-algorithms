"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional
from queue import Queue


class Solution:

    def _check(self, left, right):
        if left == None and right == None:
            return True
        if left == None or right == None:
            return False
        if left.val == right.val:
            return True
        return (
            left.val == right.val
            and self._check(left.left, right.right)
            and self._check(left.right, right.left)
        )

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        return self._check(root.left, root.right)

    def build_tree(self, input_vals):
        if input_vals == None or len(input_vals) == 0 or input_vals[0] == None:
            return
        root = TreeNode(input[0])
        fifo = Queue()
        fifo.put(root)
        index = 1
        while index < len(input) and not fifo.empty():
            node = fifo.get()
            if input[index] != None:
                left = TreeNode(input[index])
                node.left = left
                fifo.put(left)
            index += 1
            if index >= len(input_vals):
                break
            if input[index] != None:
                right = TreeNode(input[index])
                node.right = right
                fifo.put(right)
            index += 1
        return root


if __name__ == "__main__":
    input_vals = [1, 2, 2, 3, 4, 4, 3]
    solution = Solution()
    root = solution.build_tree(input_vals)
    # result = solution.isSymmetric(root)
