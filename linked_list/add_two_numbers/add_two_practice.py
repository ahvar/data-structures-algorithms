from typing import Optional
from collections import deque


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1
        dummy = ListNode()
        curr = dummy
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = carry + val1 + val2
            digit = total % 10
            carry = total // 10
            curr.next = ListNode(digit)
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next


class TestSolution:
    def setup_method(self):
        self.solution = Solution()
        self.l1 = self.link_list(243)
        self.l2 = self.link_list(564)

    def link_list(self, num):
        reverse_nums = list(reversed(str(num)))
        head = ListNode(int(reverse_nums[0]))
        curr = head
        for n in reverse_nums[1:]:
            nxt = ListNode(int(n))
            curr.next = nxt
            curr = curr.next
        return head

    def test_add(self):
        result = self.solution.addTwoNumbers(self.l1, self.l2)
        assert result.val == 7
        assert result.next.val == 0
        assert result.next.next.val == 8


if __name__ == "__main__":
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    s = Solution()
    s.addTwoNumbers(l1, l2)
