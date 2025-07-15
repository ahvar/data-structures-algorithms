"""
Given the root of a binary tree, return the average value of the nodes on each level
in the form of an array. Answers within 10-5 of the actual answer will be accepted.
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


    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root is None:
            return
        avgs = [root.val]
        fifo = Queue()
        if root.left:
            fifo.put(root.left)
        if root.right:
            fifo.put(root.right)

        while not fifo.empty():
            level_size = fifo.qsize()
            level_sum = 0
            for i in range(level_size):
                node = fifo.get()
                level_sum += node.val

                if node.left:
                    fifo.put(node.left)
                if node.right:
                    fifo.put(node.right)
            avgs.append(level_sum / level_size)
        return avgs
            
            

    def build_tree(self, input):
        if not input:
            return 
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
    print(solution.averageOfLevels(root))
    

