"""
Given the root of a binary tree and an integer targetSum, return the
number of paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards
(i.e., traveling only from parent nodes to child nodes).
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
    def _find_paths(self, node, targetSum):
        if node is None: return 0
        paths = 0
        if node.val == targetSum:
            paths += 1
        paths += self._find_paths(node.left, targetSum - node.val)
        paths += self._find_paths(node.right, targetSum - node.val)
        return paths

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root is None: return 0
        root_path = self._find_paths(root, targetSum)
        left_paths = self._find_paths(root.left, targetSum)
        right_paths = self._find_paths(root.right, targetSum)

        return root_path + left_paths + right_paths
    
    def build_tree(self, input):
        fifo = Queue(len(input))
        root = TreeNode(input[0])
        fifo.put(root)
        i = 1
        while i < len(input) and not fifo.empty():
            node = fifo.get()
            if input[i] is not None:
                left_node = TreeNode(input[i])
                node.left = left_node
                fifo.put(left_node)
            i += 1
            if i > len(input) - 1:
                break
            if input[i] is not None:
                right_node = TreeNode(input[i])
                node.right = right_node
                fifo.put(right_node)
            i += 1
        return root



if __name__ == "__main__":
    input = [1,None,2,None,3,None,4,None,5]
    targetSum = 3
    solution = Solution()
    root = solution.build_tree(input)
    print(solution.pathSum(root, targetSum))