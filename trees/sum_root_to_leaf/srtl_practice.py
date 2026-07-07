from queue import Queue
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, total):
            if not node:
                return
            total = total * 10 + node.val
            if not node.left and not node.right:
                return total

            return dfs(node.left, total) + dfs(node.right, total)

        dfs(root, 0)

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
    input = [1, 2, 3]
    solution = Solution()
    root = solution.build_tree(input)
    print(solution.sumNumbers(root))
