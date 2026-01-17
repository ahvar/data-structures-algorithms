# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


from typing import Optional


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        seen = set()
        curr = head
        while curr:
            if curr in seen:
                return True
            seen.add(curr)
            curr = curr.next
        return False

    def link_list(self, input):
        if input == None or len(input) == 0 or input[0] == None:
            return None
        head = ListNode(input[0])
        curr = head
        for i in range(1, len(input)):
            nxt = ListNode(input[i])
            curr.next = nxt
            curr = curr.next
        return head


if __name__ == "__main__":
    input = [3, 2, 0, -4]
    pos = 1
    head = ListNode(input[0])
    curr = head
    for i in range(1, len(input)):
        curr.next = ListNode(input[i])
        curr = curr.next
    node = head
    for i in range(pos):
        node = node.next
    curr.next = node

    solution = Solution()
    solution.hasCycle(head)
