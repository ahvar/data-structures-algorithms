from typing import Optional
from collections import deque


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1
        carry = 0
        head = ListNode()
        curr = head
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            digit = total % 10
            carry = total // 10
            new = ListNode(digit)
            curr.next = new
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return head.next


# 123 -> 321
# 345 -> 543
