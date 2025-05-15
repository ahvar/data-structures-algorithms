"""
In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list
is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2.
These are the only nodes with twins for n = 4.

The twin sum is defined as the sum of a node and its twin.

Given the head of a linked list with even length, return the maximum twin sum of the linked list.

ith node
twin = n - 1 - i
0 <= i <= (n/2) - 1
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
class Solution:
    def _count(self, head):
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next
        return n
    
    def pairSum(self, head: Optional[ListNode]) -> int:
        mid = n // 2
        n = self._count(head) # number of nodes in list

        twin = head
        for _ in range(n-1): twin = twin.next
        max_sum = head.val + twin.val
        i = 0
        cur = head
        while i < mid: # 0 <= i <= (n/2) - 1
            twin = head
            for _ in range(n-1-i): twin = twin.next
            max_sum = max(max_sum, cur.val + twin.val)
            cur = cur.next
            i += 1
        return max_sum


    def _build_list(self, input):
        root = None
        if input[0] is not None:
            root = ListNode(input[0])
        curr = root
        for i in range(1,len(input)):
            if input[i] is not None: curr.next = ListNode(input[i])
            curr = curr.next
        return root


if __name__ == "__main__":
    input = [4,2,2,3]
    solution = Solution()
    head = solution._build_list(input)
    print(solution.pairSum(head))