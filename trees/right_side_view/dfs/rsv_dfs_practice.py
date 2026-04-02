# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional, List
from collections import deque
from queue import Queue


class Solution:

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        values = []

        def dfs(node, depth):
            if not node:
                return
            if depth == len(values):
                values.append(node.val)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)
        return values


def build_tree(input):
    if not input or input[0] == None:
        return

    root = TreeNode(input[0])
    fifo = Queue()
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
            node.right = right
            fifo.put(right)
        index += 1
    return root
