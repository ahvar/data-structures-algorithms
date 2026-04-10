# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


from typing import Optional


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        seen = set()
        while curr:
            if curr in seen:
                return True
            seen.add(curr)
            curr = curr.next
        return False

    def link_list(self, input):
        if not input:
            return

        head = ListNode(input[0])
        curr = head
        for i in range(1, len(input)):
            nxt = ListNode(input[i])
            curr.next = nxt
            curr = curr.next
        return head


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_cycle(self):
        assert self.solution.hasCycle(head=[3, 2, 0, -4]) == True
        assert self.solution.hasCycle(head=[1, 2]) == True


if __name__ == "__main__":
    solution = Solution()
    input = [1, 5, 8, 1, 9]
    head = solution.link_list(input)
    curr = head
    while curr:
        print(curr.val)
        curr = curr.next
