import random


class RandomizedSet:

    def __init__(self):
        self._idx = {}
        self._vals = []

    def insert(self, val: int) -> bool:
        if val in self._vals:
            return True
        self._vals.append(val)
        self._idx[val] = len(self._vals) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self._idx:
            # no opp
            return True
        val_idx = self._idx[val]  # index of target val
        last_val = self._vals[-1]  # last val
        # ---------------------
        self._vals[val_idx] = last_val  # overwrite val with last_val
        self._idx[last_val] = val_idx
        # -------------------
        del self._idx[val]  # delete val
        self._vals.pop()

    def getRandom(self) -> int:
        return random(self._vals)
