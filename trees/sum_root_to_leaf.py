"""
You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.
"""
from queue import Queue
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def helper(self, node, num):
        # we hit a null child, it contributes 0 to the total sum
        if node is None:
            return 0

        current_num = num * 10 + node.val
        if node.left is None and node.right is None:
            return current_num
        subtotal = 0
        if node.left:
            subtotal += self.helper(node.left, current_num)
        if node.right:
            subtotal += self.helper(node.right, current_num)
        return subtotal


    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if root.left is None and root.right is None:
            return root.val
        total = 0
        if root.left:
            total += self.helper(root.left, root.val)
        if root.right:
            total += self.helper(root.right, root.val)
        return total

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
    input = [1,2,3]
    solution = Solution()
    root = solution.build_tree(input)
    print(solution.sumNumbers(root))


