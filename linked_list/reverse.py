"""
Given the head of a singly linked list and two integers left and right where left <= right,
reverse the nodes of the list from position left to position right, and return the reversed list.
"""
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def __init__(self):
        self._head = None

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head is None:
            return 
        dummy = ListNode(0,head)
        before_start = dummy
        for _ in range(left-1):
            before_start = before_start.next
        start = before_start.next
        end = start
        for _ in range(right - left):
            end = end.next
        after_end = end.next
        end.next = None
        # --------------------------
        prev_sub = None
        curr = start
        while curr:
            nxt = curr.next
            curr.next = prev_sub # reverse node
            prev_sub = curr
            curr = nxt
        
        before_start.next = prev_sub
        start.next = after_end
        return dummy.next

    def link_list(self, input):
        head = ListNode(input[0])
        curr = head
        for i in range(1,len(input)):
            curr.next = ListNode(input[i])
            curr = curr.next
        self._head = head
        return head

    def __repr__(self):
        curr = self._head
        while curr:
            print(curr.val)
            curr = curr.next

    @property
    def head(self):
        return self._head
        

if __name__ == "__main__":
    head = [1,2,3,4,5]
    left = 2
    right = 4
    solution = Solution()
    head = solution.link_list(head)
    print(solution.reverseBetween(head, left, right))

        