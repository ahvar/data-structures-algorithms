"""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
"""
from typing import Optional, List
from queue import Queue
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:        
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        fifo = Queue()
        result = []
        fifo.put(root)
        while not fifo.empty():
            level_size = fifo.qsize()
            new = []
            for _ in range(level_size):
                node = fifo.get()
                new.append(node.val)
                if node.left: fifo.put(node.left)
                if node.right: fifo.put(node.right)
            result.append(new)
        return result


    def build_tree(self, input):
        if input == None or len(input) == 0:
            return None
        root = TreeNode(input[0])
        fifo = Queue()
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
    input = [3,9,20,None,None,15,7]
    solution = Solution()
    root = solution.build_tree(input)
    print(solution.levelOrder(root))
        