from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        if head is None:
            return None
        dummy = ListNode(0, head)
        before_left = dummy
        for _ in range(left - 1):
            before_left = before_left.next

        lnode = before_left.next
        prev = None
        curr = lnode
        for _ in range(right - left + 1):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        before_left.next = prev
        lnode.next = curr
        return dummy.next
