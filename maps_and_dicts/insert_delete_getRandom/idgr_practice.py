import random


class RandomizedSet:

    def __init__(self):
        self._values = []
        self._idx = {}

    def insert(self, val: int) -> bool:
        if val in self._idx:
            return False
        self._values.append(val)
        idx = len(self._values) - 1
        self._idx[val] = idx
        return True

    def remove(self, val: int) -> bool:
        idx = self._idx.get(val, None)
        if idx is None:
            return False
        last = self._values[-1]
        self._values[idx] = last
        self._idx[last] = idx
        self._values.pop()
        del self._idx[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self._values)
