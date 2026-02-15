# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self._min_diff = float("inf")
        self._prev_val = None

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            if self._prev_val != None:
                self._min_diff = min(self._min_diff, node.val - self._prev_val)
            self._prev_val = node.val
            inorder(node.right)

        inorder(root)
        return self._min_diff
