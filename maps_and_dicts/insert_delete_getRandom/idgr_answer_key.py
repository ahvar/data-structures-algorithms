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
        # get the index of the val to remove
        idx = self._idx[val]
        # get last value in _values
        last_val = self._vals[-1]
        # overwrite val to remove with last_val
        self._vals[idx] = last_val
        # set index of formerly last val to index of remove val
        self._idx[last_val] = idx
        # pop the last val
        self._vals.pop()
        # delete remove val index
        del self._idx[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self._vals)


if __name__ == "__main__":
    randset = RandomizedSet()
