import random


class RandomizedSet:

    def __init__(self):
        self._values = []
        self._indexes = {}

    def insert(self, val: int) -> bool:
        if val in self._values:
            # item present
            return False
        self._values.append(val)
        self._indexes[val] = len(self._values) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self._indexes:
            return False
        # get the last value
        last = self._values.pop()
        # get the last value's index
        last_idx = self._indexes[last]
        # get the index of the value to remove
        val_idx = self._indexes[val]
        # overwrite the value to remove with the last value
        self._values[val_idx] = last
        #
        self._indexes[last] = val_idx
        del self._idexes[last_idx]

    def getRandom(self) -> int:
        return random(self._values)
