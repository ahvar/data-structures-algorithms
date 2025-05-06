"""
Given the root of a binary tree, imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.


"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional, List
from queue import Queue
class Solution:
    def __init__(self):
        self._result = []
    def _go_right(self, node, level):
        if node is None:
            return
        if level == len(self._result):
            self._result.append(node.val)
        self._go_right(node.right, level+1)
        self._go_right(node.left, level+1)

        
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self._go_right(root,0)
        return self._result
        
        

    def _build_tree(self, input):
        if not input:
            return None
        root = TreeNode(input[0])
        fifo = Queue()
        fifo.put(root)
        i = 1
        while i < len(input) and not fifo.empty():
            node = fifo.get()
            if i < len(input):
                if input[i] is not None:
                    node.left = TreeNode(input[i])
                    fifo.put(node.left)
                i += 1
            
            if i < len(input):
                if input[i] is not None:
                    node.right = TreeNode(input[i])
                    fifo.put(node.right)    
            i += 1
        return root

if __name__ == "__main__":
    input = [1,2,3,None,5,None,4]
    solution = Solution()
    root = solution._build_tree(input)
    print(solution.rightSideView(root))
    

