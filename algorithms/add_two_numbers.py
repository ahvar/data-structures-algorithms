"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""
from typing import Optional
from collections import deque 
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getListInt(self, linked_list):
        current = linked_list
        linked_list_digits = ""
        while current.next:
            linked_list_digits = linked_list_digits + str(current.val)
            current = current.next
        linked_list_digits = linked_list_digits + str(current.val)
        linked_list_int = linked_list_digits[::-1]
        return int(linked_list_int)
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_int = self.getListInt(l1)
        l2_int = self.getListInt(l2)
        l1_l2_sum = l1_int + l2_int
        l1_l2_string = str(l1_l2_sum)[::-1]
        head = ListNode(int(l1_l2_string[0]))
        current = head
        for val in l1_l2_string[1:]:
            current.next = ListNode(int(val))
            current = current.next
        return head
        



if __name__ == "__main__":
    l1 = ListNode(2,ListNode(4,ListNode(3)))
    l2 = ListNode(5,ListNode(6,ListNode(4)))
    s = Solution()
    s.addTwoNumbers(l1,l2)