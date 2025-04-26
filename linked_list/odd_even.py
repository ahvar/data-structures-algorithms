"""
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        odd = head
        even = odd.next
        even_head = head.next
        while odd.next and even.next:
            odd.next = even.next
            even.next = odd.next.next
            odd = odd.next
            even = even.next
        odd.next = even_head
        return head



if __name__ == "__main__":
    input = [2,1,3,5,6,4,7]
    head = ListNode(input[0])
    current = head
    for i in range(1,len(input)):
        current.next = ListNode(input[i])
        current = current.next
    solution = Solution()
    head = solution.oddEvenList(head)
    current = head
    while current:
        print(current.val)
        current = current.next