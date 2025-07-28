"""
Given the head of a linked list, remove the
nth node from the end of the list and return its head.
"""
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head == None: return head
        curr = head
        count = 0
        while curr:
            count += 1
            curr = curr.next
        if count < n: return None
        if count == n: return head.next
        
        curr = head
        for _ in range(count - n - 1):
            curr = curr.next
        curr.next = curr.next.next
        return head

        

    def link_list(self, input):
        if not input:
            return
        head = ListNode(input[0])
        curr = head
        for i in range(1,len(input)):
            new = ListNode(input[i])
            curr.next = new
            curr = curr.next
        return head

if __name__ == "__main__":
    input = [1,2,3,4,5]
    n = 2
    solution = Solution()
    head = solution.link_list(input)
    head = solution.removeNthFromEnd(head, n)
    while head:
        print(head.val)
        head = head.next
