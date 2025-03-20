from typing import List
from rich import print as rprint
"""
Given a sorted array of distinct integers and a target value,
return the index if the target is found. If not, return the index where
it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        high = len(nums) - 1
        low = 0
        mid = (high + low) // 2
        guess = nums[mid]
        while low <= high: 
            if guess == target:
                return nums.index(guess)
            if guess < target:
                low = mid + 1
            elif guess > target:
                high = mid - 1
            mid = (high + low) // 2
            guess = nums[mid]
        return low


if __name__ == "__main__":
    nums = [1,3,5,6]
    target = 7
    s = Solution()
    rprint(s.searchInsert(nums, target))