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
    def _check(self, a, b):
        if a is None and b is None:
            return True
        if not a and b or a and not b:
            return False
        if a.val != b.val:
            return False
        asym = self._check(a.left, b.right)
        bsym = self._check(a.right, b.left)
        if asym and bsym:
            return True
        return False
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self._check(root.left, root.right)
        
    def build_tree(self, input_vals):
        if input_vals is None or input_vals[0] is None:
            return None
        root = TreeNode(input_vals[0])
        fifo = Queue()
        fifo.put(root)
        index = 1
        while index < len(input_vals) and not fifo.empty():
            node = fifo.get()
            # left
            if input_vals[index] is not None:
                new_left = TreeNode(input_vals[index])
                node.left = new_left
                fifo.put(new_left)

            index += 1
            
            if index <= len(input_vals) - 1 and input_vals[index] is not None:
                new_right = TreeNode(input_vals[index])
                node.right = new_right
                fifo.put(new_right)

            index += 1
        return root

if __name__ == "__main__":
    input_vals = [1,2,2,3,4,4,3]
    solution = Solution()
    root = solution.build_tree(input_vals)
    #result = solution.isSymmetric(root)