import random


class RandomizedSet:

    def __init__(self):
        self._idx = {}  # val to index map
        self._vals = []  # list of values

    def insert(self, val: int) -> bool:
        if val in self._idx:
            return False
        self._vals.append(val)
        self._idx[val] = len(self._vals) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self._idx:
            return False
        # get the val
        last = self._vals[-1]
        # index of last val
        idx = self._idx.get(val)
        # overwrite the val to remove
        self._idx[last] = idx
        self._vals.pop()
        del self._idx[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self._vals)
