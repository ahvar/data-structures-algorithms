# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        if not head:
            return
        dummy = ListNode(0, head)
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
        prev.next = before_left
        before_left.next = curr
        return dummy.next


def link_list(input):
    if not input or input[0] == None:
        return
    head = ListNode(input[0])
    curr = head
    n = len(input)
    for i in range(1, n):
        nxt = ListNode(input[i])
        curr.next = nxt
        curr = curr.next
    return head


class TestSolution:

    def setup_method(self):
        self.solution = Solution()
        self.list = link_list([1, 2, 3, 4, 5])

    def test_reverse_between(self):
        expected = link_list([1, 4, 3, 2, 5])
        actual = self.solution.reverseBetween(self.list, 2, 4)

        while expected or actual:
            assert expected.val == actual.val
            expected = expected.next
            actual = actual.next


if __name__ == "__main__":

    input = [1, 2, 3, 4, 5]
    left = 2
    right = 4
    solution = Solution()
    head = solution.link_list(input)
    head = solution.reverseBetween(head, left, right)
