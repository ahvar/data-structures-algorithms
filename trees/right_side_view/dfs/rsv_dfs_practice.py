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
            dfs(node.left, depth + 1)
            if len(values) == depth:
                values.append(node.val)
            dfs(node.right, depth + 1)

        dfs(root, 0)
        return values


def build_tree(input):
    root = TreeNode(input[0])
    fifo = Queue()
    fifo.put(root)
    index = 1
    while index < len(input) and not fifo.empty():
        node = fifo.get()
        if input[index] != None:
            node.left = TreeNode(input[index])
            fifo.put(node.left)
        index += 1
        if index >= len(input):
            break
        if input[index] != None:
            node.right = TreeNode(input[index])
            fifo.put(node.right)
        index += 1
    return root


class TestSolution:
    def setup_method(self):
        self.solution = Solution()
        self.root = build_tree([1, 2, 3, None, 5, None, 4])

    def test_right_side_view(self):
        expected = [1, 3, 4]
        assert expected == self.solution.rightSideView(self.root)
