"""
Given the head of a sorted linked list, delete all nodes that have duplicate numbers,
leaving only distinct numbers from the original list. Return the linked list sorted as well.
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return
        dummy = ListNode(0)
        dummy.next = head
        curr = head
        prev = dummy
        while curr:
            if curr.next and curr.val == curr.next.val:
                dup_val = curr.val
                while curr and curr.val == dup_val:
                    curr = curr.next
                prev.next = curr
            else:
                prev = prev.next
                curr = curr.next
        return dummy.next


    def build_list(self, input):
        if not input: return None
        root = ListNode(input[0])
        node = root
        for i in range(1,len(input)):
            new = ListNode(input[i])
            node.next = new
            node = node.next
        return root


if __name__ == "__main__":
    input = [1,2,3,3,3,3,4,4,5]
    solution = Solution()
    head = solution.build_list(input)
    head = solution.deleteDuplicates(head)
    curr = head
    while curr:
        print(curr.val)
        curr = curr.next