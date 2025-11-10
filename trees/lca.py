"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q
as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
"""

# Definition for a binary tree node.
from queue import Queue


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.rigth, p, q)

        if left and right:
            return root
        return left if left else right

    def _build_tree(self, input):
        if input == None or len(input) == 0 or input[0] == None:
            return None

        fifo = Queue()
        root = TreeNode(input[0])
        fifo.put(root)
        index = 1
        while index < len(input) and not fifo.empty():
            node = fifo.get()
            if input[index] != None:
                left = TreeNode(input[index])
                node.left = left
                fifo.put(left)
            index += 1
            if index >= len(input):
                break
            if input[index] != None:
                right = TreeNode(input[index])
                fifo.right = right
                fifo.put(right)
            index += 1
        return root


if __name__ == "__main__":
    input = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    p = 5
    q = 1
    solution = Solution()
    root = solution._build_tree(input)
    pnode = solution._get_node(root, p)
    qnode = solution._get_node(root, q)
    solution.lowestCommonAncestor(root, pnode, qnode)
