"""
Implement the BSTIterator class that represents an iterator over the in-order traversal of a
binary search tree (BST):

BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the
BST is given as part of the constructor. The pointer should be initialized to a non-existent
number smaller than any element in the BST.

boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer,
otherwise returns false.
int next() Moves the pointer to the right, then returns the number at the pointer.
Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will
return the smallest element in the BST.

You may assume that next() calls will always be valid. That is, there will be at least a next number
in the in-order traversal when next() is called.


"""
from typing import Optional
from queue import Queue
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator:

    def _push_left(self, node):
        if node == None:
            return
        self._stack.append(node)
        self._push_left(node.left)

        
    def __init__(self, root):
        self._stack = []
        self._push_left(root)
        
    def next(self):
        node = self._stack.pop()
        val = node.val
        if node.right:
            self._push_left(node.right)
        return val

    def hasNext(self):
        return len(self._stack) > 0



    
def build_tree(input):
    if input == None or len(input) == 0 or input[0] == None:
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




if __name__ == "__main__":
    input = [7, 3, 15, None, None, 9, 20]
    root = build_tree(input)
    bst_iterator = BSTIterator(root)