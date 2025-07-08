"""
LC117

Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no
next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A), your function should populate each
next pointer to point to its next right node, just like in Figure B. The serialized output
is in level order as connected by the next pointers, with '#' signifying the end of each level.
"""
# Definition for a Node.
from queue import Queue
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None:
            return None
        fifo = Queue()
        fifo.put(root)
        while not fifo.empty():
            size = fifo.qsize()
            prev_node = None
            for i in range(size):
                node = fifo.get()
                if node.left:
                    fifo.put(node.left)
                if node.right:
                    fifo.put(node.right)
                if prev_node:
                    prev_node.next = node
                prev_node = node
            if prev_node:
                prev_node.next = None
        return root

    def _build_tree(self, input):
        """
        Breadth-first construction of a binary tree from the input array.
        """
        n = len(input)
        if n == 0:
            return None
        fifo = Queue()
        root = Node(input[0])
        fifo.put(root)
        index = 1
        while index < n and not fifo.empty():
            node = fifo.get()
            if input[index] is not None:
                lnode = Node(input[index])
                node.left = lnode
                fifo.put(lnode)
            
            index += 1
            if index >= n:
                break

            if input[index] is not None:
                rnode = Node(input[index])
                node.right = rnode
                fifo.put(rnode)

            index += 1
        return root



if __name__ == "__main__":
    input = [1,2,3,4,5,None,7]
    solution = Solution()
    root = solution._build_tree(input)
