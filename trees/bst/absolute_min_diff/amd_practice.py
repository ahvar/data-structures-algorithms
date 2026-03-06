# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        min_diff = float("inf")
        prev_val = None

        def inorder(node):
            if not node:
                return

            inorder(node.left)

            if prev_val is not None:
                min_diff = min(min_diff, node.val - prev_val)
            prev_val = node.val

            inorder(node.right)

        inorder(root)
        return min_diff
