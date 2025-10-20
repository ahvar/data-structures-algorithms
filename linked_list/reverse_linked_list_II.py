"""
Given the head of a singly linked list and two integers left
and right where left <= right, reverse the nodes of the list
from position left to position right, and return the reversed list.
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head == None:
            return
        dummy = ListNode(0,head)
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




    def link_list(self, input):
        if input == None or len(input) == 0 or input[0] == None:
            return
        head = ListNode(input[0])
        curr = head
        for i in range(1,len(input)):
            nxt = ListNode(input[i])
            curr.next = nxt
            curr = curr.next
        return head



   
if __name__ == "__main__":

    input = [1,2,3,4,5]
    left = 2
    right = 4
    solution = Solution()
    head = solution.link_list(input)
    head = solution.reverseBetween(head, left, right)

