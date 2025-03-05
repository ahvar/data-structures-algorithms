import ctypes


class DynamicArray:
    def __init__(self):
        self._n = 0  # number of items in the array
        self._capacity = 2  # current capacity
        self._array = self._make_array(
            self._capacity
        )  # elements of the DyanmicArray class

    def __getitem__(self, k):
        if not 0 <= k < self._n:
            raise IndexError("Invalid index")
        return self._array[k]

    def _resize(self, c):
        """
        Resize the underlying array with additional capacity
        """
        new_arr = self._make_array(c)
        for i in self._n:
            new_arr[i] = self._array[i]
        self._array = new_arr
        self._capacity = c

    def _append(self, element):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._array[self._n] = element
        self._n += 1

    def insert(self, k, element):
        """Insert value at index k, shifting subsequent values rightward"""
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        j = self._n  # index of last value + 1
        while j > k:
            self._array[j] = self._array[j - 1]
            j -= 1
        self._array[j] = element
        self._n += 1

    def remove_by_location(self, k):
        """
        Return and remove the element at k
        1. shift objects leftward
        2. handle leftward shift of last object
        3. decrement count
        """
        if not 0 <= k < self._n:
            raise IndexError("Invalid index")
        element = self._array[k]
        while k < self._n:
            self._array[k] = self._array[k + 1]
            k += 1
        self._array[self._n - 1] = None
        self._n -= 1
        return element

    def remove(self, value):
        """Return and remove
        1. find value
        2. shift objects leftward
        3. handle leftward shift of last value
        4. decrement count
        """
        target = None
        for j in range(self._n - 1):
            if self._array[j] == value:
                target = self._array[j]
                k = j
                while k < self._n - 1:
                    self._array[k] = self._array[k + 1]
                    k += 1
                self._array[self._n - 1] = None
                return target
        raise ValueError("Not Found: %s".format(value))

    def retrieve(self, index):
        """Return but do not remove the element at this index"""

    def __len__(self):
        return self._n

    def _make_array(self, c):
        return (c * ctypes.py_object)()
