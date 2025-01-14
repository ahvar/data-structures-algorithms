import ctypes


class DynamicArray:
    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        if not 0 <= k < self._n:
            raise IndexError("invalid index")
        return self._A[k]

    def append(self, obj):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def insert(self, k, value):
        """Insert value at index k, shifting subsequent values rightward"""
        if self._n == self._capacity:
            self._resize(self._capacity * 2)
        for j in range(self._n, k, -1):
            self._A[j] = self._A[j - 1]
        self._A[k] = value

    def _resize(self, capacity):
        B = self._make_array(capacity)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = capacity

    def _make_array(self, capacity):
        return (capacity * ctypes.py_object)()
