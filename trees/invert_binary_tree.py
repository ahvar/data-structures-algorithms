"""
Given the root of a binary tree, invert the tree, and return its root.
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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        fifo = Queue()
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

    def build_tree(self, input):
        if not input or input[0] is None:
            return None
        fifo = Queue()
        root = TreeNode(input[0])
        fifo.put(root)
        i = 1
        while i < len(input) and not fifo.empty():
            node = fifo.get()
            if input[i] is not None:
                node.left = TreeNode(input[i])
                fifo.put(node.left)
            i += 1
            if i >= len(input):
                break
            if input[i] is not None:
                node.right = TreeNode(input[i])
                fifo.put(node.right)
            i += 1
        return root

if __name__ == "__main__":
    input = [4,2,7,1,3,6,9]
    solution = Solution()
    root = solution.build_tree(input)
    root = solution.invertTree(root)
    left = right = None
    if root.left:
        left = root.left
    if root.right:
        rith = root.right
    while left or right:
        print(root.left.val)
        print(root.right.val)
        left = left.left
        right = right.right
        