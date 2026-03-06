class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional, List
from collections import deque


class Solution:

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        queue = deque([root])
        values = []
        while queue:
            level_len = len(queue)
            for i in range(level_len):
                node = queue.popleft()
                if i == level_len - 1:

                    values.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return values
