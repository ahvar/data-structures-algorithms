"""
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the
next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
from queue import Queue, LifoQueue
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        lifo = LifoQueue()
        if root:
            lifo.put(root)
        prev = None
        while not lifo.empty():
            curr = lifo.get()
            if prev:
                prev.left = None
                prev.right = curr

            if curr.right:
                lifo.put(curr.right)
            if curr.left:
                lifo.put(curr.left)
            prev = curr

    def build_tree(self, input):
        if len(input) < 1:
            return None
        root = TreeNode(input[0])
        fifo = Queue()
        fifo.put(root)
        index = 1
        while index < len(input) and not fifo.empty():
            node = fifo.get()
            if input[index] != None:
                lnode = TreeNode(input[index])
                node.left = lnode
                fifo.put(lnode)
            index += 1
            if index >= len(input) - 1:
                break
            if input[index] != None:
                rnode = TreeNode(input[index])
                node.right = rnode
                fifo.put(rnode)
            index += 1
        return root
            

if __name__ == "__main__":
    input = [1,2,5,3,4,None,6]
    solution = Solution()
    root = solution.build_tree(input)
    solution.flatten()