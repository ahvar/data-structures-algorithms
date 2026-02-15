from typing import Optional


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
            return True
        return self._check(root.left, root.right)
