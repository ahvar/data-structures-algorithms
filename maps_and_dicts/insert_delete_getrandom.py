"""
Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present.
Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present.
Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of
elements (it's guaranteed that at least one element exists when this method is called).
Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in
average O(1) time complexity.


"""

import ctypes
import random


class RandomizedSet:

    def __init__(self):
        self._idx = {}
        self._vals = []

    def insert(self, val: int) -> bool:
        if val in self._idx:
            return False
        self._vals.append(val)
        self._idx[val] = len(self._vals) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self._idx:
            return False
        idx = self._idx[val]
        last_val = self._val[-1]
        self._vals[idx] = last_val
        self._idx[last_val] = idx
        self._vals.pop()
        del self._idx[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self._vals)


if __name__ == "__main__":
    randset = RandomizedSet()
