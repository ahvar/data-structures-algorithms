"""
You are given the head of a linked list. Delete the middle node, and return the head
of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing,
where ⌊x⌋ denotes the largest integer less than or equal to x.

For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def __init__(self):
        self._size = 0

    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if head and not head.next:
            head = None
            return head
        curr = head
        while curr:
            self._size += 1
            curr = curr.next
        curr = head
        prev = None
        mid = self._size // 2
        count = 0
        while count < mid:
            prev = curr
            curr = curr.next
            count += 1
        prev.next = curr.next
        return head

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size


if __name__ == "__main__":
    vals = [1, 3, 4, 7, 1, 2, 6]
    head = ListNode(vals[0])
    for i in range(1, len(vals)):
        curr = head
        while curr.next:
            curr = curr.next
        curr.next = ListNode(vals[i])
    s = Solution()
    s.size = len(vals)
    head = s.deleteMiddle(head)
    curr = head
    while curr.next:
        print(curr.val)
        curr = curr.next
