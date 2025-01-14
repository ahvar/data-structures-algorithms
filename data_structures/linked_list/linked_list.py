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
    
class AirportList:
    def __init__(self, airport: str) -> None:
        self._head = ListNode(airport)
        self._tail = None
        self._count = 1

    def remove_first(self) -> ListNode:
        if not self._head:
            raise Exception("List is empty")
        self._head = self._head.next
        self._count =- 1

    def remove_last(self) -> ListNode:
        pass

    def add_first(self, airport: str) -> None:
        if not self._head:
            self._head = ListNode(airport)
            self._count = 1
        else:
            new_node = ListNode(airport=airport)
            new_node.next = self._head
            self._head = new_node

    def add_last(self, airport: str) -> None:
        if not self._tail:
            self._tail = ListNode(airport)
            self._tail.next = None
            self._count += 1
        else:
            self._tail.next = ListNode(airport)
            self._tail = self._tail.next
            self._tail.next = None
            self._count += 1



    @property
    def head(self) -> ListNode:
        return self._head
    
    @property
    def tail(self) -> ListNode:
        return self._tail

    @property
    def count(self) -> int:
        return self._count
        

if __name__ == "__main__":
    lax = ListNode("LAX")
    msp = ListNode("MSP")
    atl = ListNode("ATL")
    bos = ListNode("BOS")
    linked_list = AirportList(lax)
    linked_list.add_node(msp)
    linked_list.add_node(atl)
    linked_list.add_node(bos)