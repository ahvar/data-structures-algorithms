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
        if a == None and b == None:
            return True
        if a == None or b == None:
            return False
        if a.val != b.val:
            return False
        return self._check(a.left, b.right) and self._check(a.right, b.left)
        

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        return self._check(root.left, root.right)
        

        
    def build_tree(self, input_vals):
        if input_vals == None or len(input_vals) == 0 or input_vals[0] == None:
            return 
        root = TreeNode(input[0])
        fifo = Queue()
        fifo.put(root)
        index = 1
        while index < len(input_vals) and not fifo.empty():
            node = fifo.get()
            if input_vals[index] != None:
                nxt = TreeNode(input_vals[index])
                node.left = nxt
                fifo.put(nxt)
            index += 1
            if index >= len(input_vals):
                break
            if input_vals[index] != None:
                nxt = TreeNode(input_vals[index])
                node.right = nxt
                fifo.put(nxt)
            index += 1
        return root


if __name__ == "__main__":
    input_vals = [1,2,2,3,4,4,3]
    solution = Solution()
    root = solution.build_tree(input_vals)
    #result = solution.isSymmetric(root)