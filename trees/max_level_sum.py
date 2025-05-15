"""
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.
"""
from typing import Optional
from queue import Queue
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self._max_sum = float('-inf')
        self._fifo = Queue()
        
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return
        self._fifo.put(root)
        level = 1
        best_level = 1
        while not self._fifo.empty():
            level_size = self._fifo.qsize()
            level_sum = 0
            for _ in range(level_size):
                node = self._fifo.get()
                level_sum += node.val
                if node.left: self._fifo.put(node.left)
                if node.right: self._fifo.put(node.right)
            if level_sum > self._max_sum:
                self._max_sum = level_sum
                best_level = level
            level += 1
        return best_level

        

    def build_tree(self, input):
        if not input or input[0] is None:
            return None
        fifo = Queue()
        root = TreeNode(input[0])
        fifo.put(root)
        i = 1
        while i < len(input) and not fifo.empty():
            node = fifo.get()
            if input[i] is not None:
                left = TreeNode(input[i])
                node.left = left
                fifo.put(node.left)

            i += 1
            if i >= len(input):
                break

            if input[i] is not None:
                right = TreeNode(input[i])
                node.right = right
                fifo.put(node.right)
            i += 1
        return root

if __name__ == "__main__":
    input = [1,7,0,7,-8,None,None]
    solution = Solution()
    root = solution.build_tree(input)
    print(solution.maxLevelSum(root))