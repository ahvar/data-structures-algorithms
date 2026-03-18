import random


class RandomizedSet:

    def __init__(self):
        self.values = []
        self.idx = {}

    def insert(self, val: int) -> bool:
        if val in self.idx:
            return False
        self.values.append(val)
        self.idx[val] = len(self.values) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.idx:
            return False
        last = self.values[-1]
        val_idx = self.idx[val]
        self.values[val_idx] = last
        self.idx[last] = val_idx
        self.values.pop()
        del self.idx[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.values)
