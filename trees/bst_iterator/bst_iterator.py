from typing import Optional
from queue import Queue


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def _go_left(self, node):
        if not node:
            return
        self._stack.append(node)
        self._go_left(node.left)

    def __init__(self, root: Optional[TreeNode]):
        self._stack = []
        self._go_left(root)

    def next(self) -> int:
        node = self._stack.pop()
        val = node.val
        if node.right:
            self._go_left(node.right)
        return val

    def hasNext(self) -> bool:
        return len(self._stack) > 0


def build_tree(input):
    if not input or input[0] == None:
        return
    fifo = Queue()
    root = TreeNode(input[0])
    fifo.put(root)
    index = 1
    while index < len(input) and not fifo.empty():
        node = fifo.get()
        if input[index] != None:
            left = TreeNode(input[index])
            root.left = left
            fifo.put(left)
        index += 1
        if index >= len(input) - 1:
            break
        if input[index] != None:
            right = TreeNode(input[index])
            root.right = right
            fifo.put(right)
        index += 1
    return root


if __name__ == "__main__":
    input = [7, 3, 15, None, None, 9, 20]
    root = build_tree(input)
    bst_iterator = BSTIterator(root)
