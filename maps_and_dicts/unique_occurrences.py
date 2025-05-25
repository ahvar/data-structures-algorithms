"""
Given an array of integers arr, return true if the number of occurrences of each value in the
array is unique or false otherwise.

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

Input: arr = [1,2]
Output: false

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
"""
from typing import List
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        unique_freq = {}
        for i in range(len(arr)):
            if arr[i] in unique_freq:
                unique_freq[arr[i]] += 1
            else:
                unique_freq[arr[i]] = 1
        last = None
        for v in unique_freq.values():
            if last == v:
                return False
            last = v
        return True


if __name__ == "__main__":
    solution = Solution()
    arr = [-3,0,1,-3,1,1,1,-3,10,0]
    print(solution.uniqueOccurrences(arr))