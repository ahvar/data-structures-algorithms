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
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def _insert_at_end(self, node):
        end = self.tail.prev
        end.next = node
        node.prev = end
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache.get(key)
        self._remove(node)
        self._insert_at_end(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            old_node = self.cache[key]
            self._remove(old_node)
            del self.cache[key]
        new_node = Node(key, value)
        self.cache[key] = new_node
        self._insert_at_end(new_node)

        if len(self.cache) > self.capacity:
            lru_node = self.head.next
            self._remove(lru_node)
            del self.cache[lru_node.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
