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
        dummy = ListNode()
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

    def link_list(self, input):
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


if __name__ == "__main__":

    input = [1, 2, 3, 4, 5]
    left = 2
    right = 4
    solution = Solution()
    head = solution.link_list(input)
    head = solution.reverseBetween(head, left, right)
