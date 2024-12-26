from typing import List
from rich import print as rprint

class Solution:
    def quick_sort(self, arr: List[int]) -> List[int]:
        if len(arr) < 2:
            return arr
        pivot_index = len(arr) - 1 // 2
        pivot = arr[pivot_index]
        subarr_left = [i for i in arr if i < pivot]
        subarr_right = [i for i in arr if i > pivot]
        return self.quick_sort(subarr_left) + [pivot] + self.quick_sort(subarr_right)

if __name__ == "__main__":
    arr = [33,10,15,7]
    s = Solution()
    rprint(s.quick_sort(arr))