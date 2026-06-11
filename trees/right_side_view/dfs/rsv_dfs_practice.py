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
        if not root:
            return
        values = []

        def dfs(node, depth):
            if not node:
                return

            if depth == len(values):
                values.append(node.val)

            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        dfs(root, 0)


def build_tree(input):
    if not input or input[0] == None:
        return
    queue = Queue()
    root = TreeNode(input[0])
    queue.put(root)
    index = 1
    while index < len(input) and not queue.empty():
        node = queue.get()
        if input[index] != None:
            left = TreeNode(input[index])
            node.left = left
            queue.put(left)
        index += 1
        if index >= len(input):
            break
        if input[index] != None:
            right = TreeNode(input[index])
            node.right = right
            queue.put(right)
        index += 1
    return root
