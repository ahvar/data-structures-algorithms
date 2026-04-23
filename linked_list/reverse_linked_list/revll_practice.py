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

        lnode = before_left.next  # left node
        curr = lnode
        prev = None
        for _ in range(right - left + 1):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        lnode.next = curr
        before_left.next = prev
        return dummy.next


def link_list(input):
    if not input:
        return
    head = ListNode(input[0])
    curr = head
    for i in range(len(input)):
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
