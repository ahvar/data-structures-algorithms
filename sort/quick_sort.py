from typing import List
from rich import print as rprint

class Solution:
    def quick_sort(self, arr: List[int]) -> List[int]:
        if len(arr) < 2:
            return arr
        pivot_index = len(arr) // 2
        pivot = arr[pivot_index]
        lesser = [i for i in arr if i < pivot]
        greater = [i for i in arr if i > pivot]
        equal = [i for i in arr if i ==  pivot]
        return self.quick_sort(lesser) + equal + self.quick_sort(greater)

if __name__ == "__main__":
    arr = [33,43,2,21,10,8,15,7]
    s = Solution()
    rprint(s.quick_sort(arr))