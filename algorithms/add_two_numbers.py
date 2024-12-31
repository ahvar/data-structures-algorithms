"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""
from typing import Optional
# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        pass

if __name__ == "__main__":
    l1 = [2,4,3]
    l1.reverse()
    l2 = [5,4,6]
    l2.reverse()
    list_node = ListNode(val=l1[len(l1) - 1], next=None)
    i = len(l1)
    j = len(l2)
    for num in l1:
        while list_node.next:
            if not list_node:
                list_node = ListNode(val=l1[i], next=None)
            elif not list_node.next:
                list_node.next = ListNode(val=l1[i], next=None)
                list_node.next = 


        

    s = Solution()