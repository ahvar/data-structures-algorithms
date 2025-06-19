"""
Given two integer arrays inorder and postorder where inorder is the inorder
traversal of a binary tree and postorder is the postorder traversal of the same
tree, construct and return the binary tree.
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
    def traverse_postorder(self, postorder):
        """
        recursively traverses the subtrees rooted at the children of the root
        first, and then visit the root
        """

    def traverse_inorder(self, p):
        """
        we visit the position between the recursive traversals of its left
        and right subtrees. For every position p, visit p after all the positions
        in the left subtree of p and before all positions in the right subtree.
        """
        while p.left:
            print(p.left.val)
            p = p.left
            self.traverse_inorder(p)

        print(p.val)
        
        while p.right:
            print(p.right.val)
            p = p.rith
            self.traverse_inorder(p)
        return p

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        root = TreeNode(postorder.pop())
        root_idx = inorder.index(root.val)
        root.right = self.buildTree(inorder[root_idx+1:], postorder[root_idx:])
        root.left = self.buildTree(inorder[:root_idx], postorder[:root_idx])
        return root


    def build_breadth_first(self, input):
        if input == None:
            return None
        root = TreeNode(input[0])
        index = 1
        fifo = Queue()
        fifo.put(root)
        while index < len(input) and not fifo.empty():
            node = fifo.get()
            if input[index] is not None:
                node.left = TreeNode(input[index])
                fifo.put(node.left)
            index += 1
            if index > len(input):
                break
            if input[index] is not None:
                node.right = TreeNode(input[index])
                fifo.put(node.right)
            index += 1
        return root

if __name__ == "__main__":
    inorder = [9,3,15,20,7]
    postorder = [9,15,7,20,3]
    solution = Solution()
    root = solution.build_breadth_first(inorder)
    node = root 
    #solution.traverse_inorder(root)
    #solution.buildTree()