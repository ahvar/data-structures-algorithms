# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.min_diff = float("inf")
        self.prev_val = None

        def dfs(node):
            if not node:
                return

            dfs(node.left)

            if self.prev_val is not None:
                self.min_diff = min(self.min_diff, node.val - self.prev_val)

            self.prev_val = node.val

            dfs(node.right)

        dfs(root)
        return self.min_diff
