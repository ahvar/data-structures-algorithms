"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q
as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
"""
#Definition for a binary tree node.
from queue import Queue
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:

    def _parent_and_depth(self, root):
        if not root:
            return
        stack = [(root,None,0)] # (current, parent, depth)
        parent_map = {root: None}
        depth_map = {root:0}
        while stack:
            node, par, dep = stack.pop()
            parent_map[node] = par
            depth_map[node] = dep
            if node.left:
                stack.append((node.left,node,dep+1))
            if node.right:
                stack.append((node.right,node,dep + 1))
        return parent_map, depth_map

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        (parent_map, depth_map) = self._parent_and_depth(root)

        while depth_map[p] > depth_map[q]:
            p = parent_map[p]
        while depth_map[q] > depth_map[p]:
            q = parent_map[q]

        while p != q:
            p = parent_map[p]
            q = parent_map[q]

        return p


    def _build_tree(self, input):
        root = TreeNode(input[0])
        fifo = Queue(len(input))
        fifo.put(root)
        i = 1
        while i < len(input) and not fifo.empty():
            if input[i] is not None:
                node = fifo.get()
                node.left = TreeNode(input[i])
                fifo.put(node.left)
            i += 1
            if i > len(input) - 1:
                break
            if input[i] is not None:
                node = fifo.get()
                node.right = TreeNode(input[i])
                fifo.put(node.right)
            i += 1
        return root
    
    def _get_node(self, node, target):
        if not node:
            return None
        if node.val == target:
            return node
        left = self._get_node(node.left, target)
        if left:
            return left
        return self._get_node(node.right, target)


if __name__ == "__main__":
    input = [3,5,1,6,2,0,8,None,None,7,4]
    p = 5
    q = 1
    solution = Solution()
    root = solution._build_tree(input)
    pnode = solution._get_node(root, p)
    qnode = solution._get_node(root, q)
    solution.lowestCommonAncestor(root, pnode, qnode)
    