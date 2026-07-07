# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start = ListNode(0, head)
        prev = start
        curr = head
        while curr:
            if curr.next and curr.val == curr.next.val:
                duplicate_value = curr.val
                while curr and curr.val == duplicate_value:
                    curr = curr.next
                prev.next = curr
            else:
                prev = curr
                curr = curr.next
        return start.next
