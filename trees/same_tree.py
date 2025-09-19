"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional, List
from queue import Queue

class Solution:

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True
        if p == None or q == None:
            return False
        if p.val != q.val:
            return False
        right_sides = self.isSameTree(p.right, q.right)
        left_sides = self.isSameTree(p.left, q.left)
        if right_sides == left_sides:
            return True
        return False

            

    def build_tree(self, input):
        if not input or not input:
            return None
        root = TreeNode(input[0])
        fifo = Queue()
        fifo.put(root)
        i = 1
        while i < len(input) and not fifo.empty():
            node = fifo.get()
            if i < len(input) and input[i] is not None:
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
    p = [1,2,3]
    q = [1,2,3]
    solution = Solution()
    proot = solution.build_tree(p)
    qroot = solution.build_tree(q)
    solution.isSameTree(proot, qroot)