# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional
from queue import Queue


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == targetSum

        left = self.hasPathSum(root.left, targetSum - root.val)
        right = self.hasPathSum(root.right, targetSum - root.val)
        return left or right

    def build_tree(self, input):
        if not input or len(input) == 0 or not input[0]:
            return
        fifo = Queue()
        root = TreeNode(input[0])
        fifo.put(root)
        index = 1
        while index < len(input) and not fifo.empty():
            node = fifo.get()
            if input[index]:
                left = TreeNode(input[index])
                node.left = left
                fifo.put(left)
            index += 1
            if input[index]:
                right = TreeNode(input[index])
                node.right = right
                fifo.put(right)
            index += 1
        return root
