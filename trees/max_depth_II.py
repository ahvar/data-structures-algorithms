"""

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
    def maxDepth(self, root: Optional[TreeNode]):
        if not root: return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return 1 + max(left_depth, right_depth)

    def build_tree(self, input):
        if not input or input[0] == None: return 
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
            if index >= len(input) - 1: break
            if input[index] != None:
                right = TreeNode(input[index])
                node.right = right
                fifo.put(right)
            index += 1
        return root

if __name__ == "__main__":
    input = [3,9,20,None,None,15,7]
    solution = Solution()
    root = solution.build_tree(input)
    print(solution.maxDepth(root))