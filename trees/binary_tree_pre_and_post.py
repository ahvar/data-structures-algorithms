"""
Given two integer arrays preorder and inorder where preorder is the preorder
traversal of a binary tree and inorder is the inorder traversal of the same tree,
construct and return the binary tree.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List, Optional
from queue import Queue
class Solution:
    def _build_level_order(self, level_order: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        fifo = Queue()
        root = TreeNode(preorder[0])
        fifo.put(root)
        index = 1
        while index < len(preorder) and not fifo.empty():
            node = fifo.get()
            if preorder[index] is not None:
                node.left = TreeNode(preorder[index])
                fifo.put(node.left)
            index += 1
            if index >= len(preorder):
                break
            if preorder[index] is not None:
                node.right = TreeNode(preorder[index])
                fifo.put(node.right)
            index += 1
        return root
    
    def _build_subtree(self, node, vals):
        if not vals:
            return
        
        if not node.right:
            while vals:
                new = TreeNode(vals.pop(0))
                node.right = new
                self._build_subtree(node, vals)
        if not node.left:
            while vals:
                new = TreeNode(vals.pop(0))
                node.left = new
                self._build_subtree(node, vals)
        return node
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root_val = preorder[0]
        root = TreeNode(root_val)
        inorder_index = inorder.index(root_val)
        left_size = inorder_index
        root.left = self.buildTree(preorder[1:1+left_size], inorder[:inorder_index])
        root.right = self.buildTree(preorder[1+left_size:], inorder[inorder_index+1:])
        return root

if __name__ == "__main__":
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    solution = Solution()
    solution.buildTree(preorder, inorder)
