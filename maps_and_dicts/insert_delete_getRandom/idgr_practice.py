import random


class RandomizedSet:

    def __init__(self):
        self._values = []
        self._idx = {}

    def insert(self, val: int) -> bool:
        if val in self._idx:
            return False
        self._values.append(val)
        self._idx[val] = len(self._values) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self._idx:
            return False
        idx = self._idx[val]
        last_val = self._values[-1]
        self._values[idx] = last_val
        self._idx[last_val] = idx
        self._values.pop()
        del self._idx[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self._values)
