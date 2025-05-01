"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
1. 
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        prev = None
        curr = head
        while curr.next:
            after = curr.next
            curr.next = prev
            prev = curr
            curr = after
        curr.next = prev
        return curr

if __name__ == "__main__":
    input = [1,2,3,4,5]
    head = ListNode(input[0])
    curr = head
    for i in range(1,len(input)):
        curr.next = ListNode(input[i])
        curr = curr.next
    solution = Solution()
    solution.reverseList(head)