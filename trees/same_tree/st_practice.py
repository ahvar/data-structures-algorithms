class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional, List
from queue import Queue


class Solution:

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if neither node exists then they're the same
        if not p and not q:
            return True
        # but if just one node isn't there, these two
        # trees aren't identical
        if not p or not q:
            return False
        # values are different
        if p.val != q.val:
            return False
        # recurse both sides of the tree, checking that
        # corresponding nodes at each position are the same
        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)
        return left and right
