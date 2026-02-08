"""
Given an array of integers nums sorted in non-decreasing order (e.g. [2,4,4,5,5...]),
find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
"""

from typing import List


class Solution:
    def _find_end(self, nums, start, target):
        end = start
        for i in range(start + 1, len(nums)):
            if nums[i] == target:
                end = i
            else:
                break
        for i in range(start - 1, -1, -1):
            if nums[i] == target:
                start = i
            else:
                break
        return [start, end]

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        right, left = 0, len(nums) - 1
        while left < right:
            mid = ((right - left) // 2) + left
            guess = nums[mid]
            if guess < target:
                left = mid + 1
            elif guess > target:
                right = mid
            elif guess == target:
                return self._find_end(nums, mid, target)
        if nums[left] == target:
            return self._find_end(nums, left, target)
        return [-1, -1]


if __name__ == "__main__":
    nums = [1]
    target = 10
    solution = Solution()
    print(solution.searchRange(nums, target))
