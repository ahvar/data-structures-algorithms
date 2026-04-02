from typing import List, Optional
from queue import Queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        root = TreeNode(preorder[0])
        inorder_index = inorder.index(preorder[0])
        left_size = inorder_index
        root.left = self.buildTree(preorder[1 : 1 + left_size], inorder[:inorder_index])
        root.right = self.buildTree(
            preorder[1 + left_size :], inorder[inorder_index + 1 :]
        )
        root
