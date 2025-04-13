"""
Consider all the leaves of a binary tree, from left to right order, the values of those leaves
form a leaf value sequence.

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.
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
        self._size1 = 0
        self._size2 = 0

    def _collect_leaves(self, node):
        if node is None:
            return []
        if not node.left and not node.right:
            return [node.val]
        left = self._collect_leaves(node.left)
        right = self._collect_leaves(node.right)
        return left + right

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaf1_sequence = self._collect_leaves(root1)
        leaf2_sequence = self._collect_leaves(root2)
        return leaf1_sequence == leaf2_sequence



        

def build_tree(input):
    fifo = Queue(TreeNode(len(input)))
    root_node = input[0]
    fifo.put(root_node)
    i = 1
    while i < len(input) and not fifo.empty():
        node = fifo.get()
        # left child
        if input[i] is not None:
            node_left = TreeNode(input[i])
            node.left = node_left
            solution._size1 += 1
            fifo.put(node_left)
        i += 1

        if i >= len(input):
            break
        # right child
        if i < len(input) and input[i] is not None:
            node_right = TreeNode(input[i])
            node.right = node_right
            solution._size1 += 1
            fifo.put(node_right)
        i += 1
    return fifo


if __name__ == "__main__":
    solution = Solution()
    input1 = [3,5,1,6,2,9,8,None,None,7,4]
    input2 = [3,5,1,6,7,4,2,None,None,None,None,None,None,9,8]
    root1 = build_tree(input1).get()
    root2 = build_tree(input2).get()
    solution.leafSimilar(root1, root2)
    
    
