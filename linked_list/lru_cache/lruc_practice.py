class Node:
    def __init__(self, key: int = 0, value: int = 0):
        # Store the cache entry's key and value.
        self.key = key
        self.value = value

        # Pointers for the doubly linked list.
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        nxt = node.next
        prv = node.prev
        prv.next = nxt
        nxt.prev = prv

    def _insert_at_end(self, node):
        prv = self.tail.prev
        prv.next = node
        node.prev = prv
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._insert_at_end(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            old_node = self.cache[key]
            self._remove(old_node)
            del self.cache[key]
        new_node = Node(key, value)
        self.cache[key] = new_node
        self._insert_at_end(new_node)
        if len(self.cache) > self.capacity:
            lru = self.head.next
            self._remove(lru)
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
