"""
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf
path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.
root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # base case: empty tree
        if root == None:
            return False

        # check if we've reached a leaf with the target sum
        if root.left is None or root.right is None:
            return targetSum == root.val

        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(
            root.right, targetSum - root.val
        )

    def build_tree(self, input):
        if len(input) < 1:
            return None
        fifo = Queue()
        root = TreeNode(input[0])
        fifo.put(root)
        index = 1
        while index < len(input) and not fifo.empty():
            node = fifo.get()
            if input[index] is not None:
                left = TreeNode(input[index])
                node.left = left
                fifo.put(left)
            index += 1
            if index >= len(input):
                break
            if input[index] is not None:
                right = TreeNode(input[index])
                node.right = right
                fifo.put(right)
            index += 1
        return root


if __name__ == "__main__":
    input = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
    targetSum = 22
    solution = Solution()
    solution.hasPathSum()
