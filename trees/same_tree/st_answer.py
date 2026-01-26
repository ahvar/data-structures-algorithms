# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional, List
from queue import Queue


class Solution:

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True
        if p == None or q == None:
            return False
        if p.val != q.val:
            return False
        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)
        return left and right

    def build_tree(self, input):
        if input == None or len(input) == 0 or input[0] == None:
            return
        root = TreeNode(input[0])
        fifo = Queue()
        fifo.put(root)
        index = 1
        while index <= len(input) and not fifo.empty():
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
                node.right = right
                fifo.put(right)
            index += 1
        return root


if __name__ == "__main__":
    p = [1, 2, 3]
    q = [1, 2, 3]
    solution = Solution()
    proot = solution.build_tree(p)
    qroot = solution.build_tree(q)
    solution.isSameTree(proot, qroot)
