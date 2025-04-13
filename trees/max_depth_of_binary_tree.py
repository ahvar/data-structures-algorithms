"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node
down to the farthest leaf node.

"""
from typing import Optional
from queue import Queue
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    class Position:
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node.val
        
        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

    def _make_position(self, node):
        return self.Position(self, node) if node is not None else None
    
    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise ValueError('p must be proper Position')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._parent is p._node:
            raise ValueError('p is no longer valid')
        return p._node
    
    def left(self, p):
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self, p):
        node = self._validate(p)
        return self._make_position(node._right)
    
    def parent(self, p):
        node = self._validate(p)
        return self._make_position(node._parent)
    
    def sibling(self, p):
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)
            
    def is_root(self, p):
        return self.root() == p
    
    def is_leaf(self, p):
        return self.num_children(p) == 0
    
    def is_empty(self):
        return len(self) == 0
    
    def __len__(self):
        return self._size
    
    def num_children(self, p):
        node = self._validate(p)
        count = 0
        if node.left is not None:
            count += 1
        if node.right is not None:
            count += 1
        return count

    def root(self):
        return self._make_position(self._root)
    
    def _add_root(self, node):
        if self._root is not None: raise ValueError('Root Exists')
        self._size = 1
        self._root = node
        return self._make_position(self._root)
    
    def __init__(self):
        self._root = None
        self._size = 0

    def maxDepth(self, node) -> int:
        if not node:
            return 0
        left_depth = self.maxDepth(node.left)
        right_depth = self.maxDepth(node.right)
        return 1 + max(left_depth, right_depth)

    def depth(self, p):
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))  

if __name__ == "__main__":
    solution = Solution()
    input = [3,9,20,None,None,15,7]
    fifo = Queue(len(input))
    root_node = TreeNode(input[0])
    root_position = solution._add_root(root_node)
    fifo.put(root_position)
    i = 1
    while not fifo.empty() and i < len(input):
        current_position = fifo.get()
        current_node = current_position._node
        if i < len(input) and input[i] is not None:
            left_node = TreeNode(val=input[i])
            current_node.left = left_node
            solution._size += 1

            left_position = solution._make_position(left_node)
            fifo.put(left_position)
        i += 1
        if i < len(input) and input[i] is not None:
            right_node = TreeNode(val=input[i])
            current_node.right = right_node
            solution._size += 1
            right_position = solution._make_position(right_node)
            fifo.put(right_position)
        i += 1
    root_position = solution.root()
    root_node = root_position._node
    print(solution.maxDepth(root_node))




        

        

    

