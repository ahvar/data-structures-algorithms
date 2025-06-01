"""
Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.


"""
import ctypes
class RandomizedSet:

    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._array = self._make_array(self._capacity)
        self._freq = {}
        
    def insert(self, val: int) -> bool:
        if val not in self._freq: # already exists
            if self._n == self._capacity: # resize ?
                self._resize(self._capacity * 2)
            self._array[self._n] = val # add to end of array
            self._freq[val] = self._n # add to freq map with array index as value
            self._n += 1 # bump count
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self._freq:
            for i in range(self._n):
                if self._array[i] == val:
                    for j in range(i, self._n - 1):
                        self._array[j] = self._array[j+1]
                    self._array[self._n - 1] = ctypes.py_object()
                    #del self._array[i]
            del self._freq[val]
            self._n -= 1
            return True
        return False
        
        
    def getRandom(self) -> int:
        pass
    
    def _resize(self, c):
        new = self._make_array(c)
        for i in range(self._n):
            new[i] = self._array[i]
        self._array = new
        self._capacity = c

    def _make_array(self,c):
        return (c * ctypes.py_object)()
    
    def __len__(self):
        return self._n

if __name__ == "__main__":
    randset = RandomizedSet()
