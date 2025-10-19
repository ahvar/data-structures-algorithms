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
        if root == None:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


    def build_tree(self, input):
        if input == None or len(input) == 0 or input[0] == None:
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
            if index >= len(input):
                break
            if input[index] != None:
                right = TreeNode(input[index])
                node.right = right
                fifo.put(right)
            index += 1
        return root




if __name__ == "__main__":
    input = [4,2,7,1,3,6,9]
    solution = Solution()
    root = solution.build_tree(input)
    root = solution.invertTree(root)

        