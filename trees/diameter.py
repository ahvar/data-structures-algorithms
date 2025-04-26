"""
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.
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
        self.diameter = 0
    def _depth(self, node):
        if not node:
            return  0
        left_height = self._depth(node.left)
        right_height = self._depth(node.right)
        current_path_length = left_height + right_height
        if current_path_length > self.diameter:
            self.diameter = current_path_length 
        return 1 + max(right_height, left_height)
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self._depth(root)
        return self.diameter



if __name__ == "__main__":
    input = [1,2,3,4,5]
    root = TreeNode(input[0])
    fifo = Queue(len(input))
    fifo.put(root)
    i = 1
    while i < len(input) and  not fifo.empty():
        node = fifo.get()
        if input[i] is not None:
            node.left = TreeNode(input[i])
            fifo.put(node)
        i += 1
        if i > len(input) - 1:
            break
        if input[i] is not None:
            node.right = TreeNode(input[i])
            fifo.put(node)
        i += 1

    solution = Solution()
    solution.diameterOfBinaryTree(root)