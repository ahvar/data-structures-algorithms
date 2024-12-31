from typing import Optional

class ListNode:
    def __init__(self, airport: str, next: Optional['ListNode'] = None) -> None:
        self._airport = airport
        self._next = next

    @property
    def airport(self) -> str:
        return self._airport
    
    @property
    def next(self) -> Optional['ListNode']:
        return self._next
    
class LinkedList:
    def __init__(self, head: ListNode) -> None:
        self._head = head
        self._count = 0

    def add_node(self, node: ListNode) -> None:
        if not self._head:
            self._head = node
        current_node = self._head
        while current_node.next:
            current_node = current_node.next
        current_node.next = node
        self._count += 1

    @property
    def head(self) -> ListNode:
        return self._head

    @property
    def count(self) -> int:
        return self._count
        

if __name__ == "__main__":
    lax = ListNode("LAX")
    msp = ListNode("MSP")
    atl = ListNode("ATL")
    bos = ListNode("BOS")
    linked_list = LinkedList(lax)
    linked_list.add_node(msp)
    linked_list.add_node(atl)
    linked_list.add_node(bos)