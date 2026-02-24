import random


class RandomizedSet:

    def __init__(self):
        self._values = []
        self._indexes = {}

    def insert(self, val: int) -> bool:
        if val not in self._indexes:
            self._values.append(val)
            self._indexes[val] = len(self._values) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val not in self._indexes:
            return False
        idx = self._indexes[val]
        self._values[idx], self._values[len(self._values) - 1] = (
            self._values[len(self._values) - 1],
            self._values[idx],
        )
        self._values.pop(len(self._values) - 1)
        del self._indexes[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self._values)
