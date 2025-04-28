"""
You are given the root of a binary tree.

A ZigZag path for a binary tree is defined as follow:

Choose any node in the binary tree and a direction (right or left).
If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
Change the direction from right to left or from left to right.
Repeat the second and third steps until you can't move in the tree.
Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).

Return the longest ZigZag path contained in that tree.
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
    def __init__(self):
        self._longest = 0
    
    def _zig_zag(self, node, direction, length):
        if not node:
            return
        self._longest = max(self._longest, length)

        if direction == 0:
            self._zig_zag(node.right, 1, length + 1)
            self._zig_zag(node.left, 0, 1)
        else:
            self._zig_zag(node.left, 0, length + 1)
            self._zig_zag(node.right, 1, 1)

    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        self._longest = 0
        self._zig_zag(root.left, 0, 1)  # simulate one left edge from root
        self._zig_zag(root.right, 1, 1) # simulate one right edge from root
        return self._longest
        

    def _build_tree(self, input):
        root = TreeNode(input[0])
        fifo = Queue(len(input))
        fifo.put(root)
        i = 1
        while i < len(input) and not fifo.empty():
            node = fifo.get()
            if input[i] is not None:
                node.left = TreeNode(input[i])
                fifo.put(node.left)
            i += 1
            if i > len(input) - 1:
                break
            if input[i] is not None:
                node.right = TreeNode(input[i])
                fifo.put(node.right)
            i += 1
        return root


if __name__ == "__main__":
    input = [1,None,1,1,1,None,None,1,1,None,1,None,None,None,1]
    solution = Solution()
    root = solution._build_tree(input)
    print(solution.longestZigZag(root))
        