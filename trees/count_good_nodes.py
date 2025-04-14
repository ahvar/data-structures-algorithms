"""
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are
no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.

Input: root = [3,3,null,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.
"""
from queue import Queue
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def _count_good(self, node, max_val, count):
        if not node:
            return 0
        if node.val >= max_val:
            max_val = node.val
        else: count += 1
        if node.left:
            max_val, lcount = self._count_good(node.left, max_val, count)
        if node.right:
            max_val, rcount = self._count_good(node.right, max_val, count)
        return max_val, lcount + rcount

    def goodNodes(self, node: TreeNode, max_val) -> int:
        if not node:
            return 0
        good_count = 1 if (node.val >= max_val) else 0
        new_max = max(max_val,node.val)
        max_val = node.val
        lcount = rcount = 0
        
        good_count += self._count_good(node.left, new_max)
        
        good_count += self._count_good(node.right, new_max)
        return good_count

def euler_tour(node):
    if not node:
        return 
    for child in (node.left, node.right):
        
        euler_tour(child)


        
def _build_tree(input):
    root = TreeNode(input[0])
    fifo = Queue(len(input))
    fifo.put(root)
    i = 1
    while i < len(input) and not fifo.empty():
        current_node = fifo.get()
        if input[i] is not None:
            left_node = TreeNode(input[i])
            current_node.left = left_node
            fifo.put(left_node)
        i += 1
        if i >= len(input):
            break
        if input[i] is not None:
            right_node = TreeNode(input[i])
            current_node.right = right_node
            fifo.put(right_node)
        i += 1
    return root


if __name__ == "__main__":
    input = [3,1,4,3,None,1,5]
    root = _build_tree(input)
    solution = Solution()
    print(solution.goodNodes(root))