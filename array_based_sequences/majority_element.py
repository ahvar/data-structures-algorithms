"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.
"""
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        element_count = {}
        for i in range(len(nums)):
            if nums[i] not in element_count:
                element_count[nums[i]] = 1
            else:
                element_count[nums[i]] += 1
        majority_val = max(element_count.values())
        for k,v in element_count.items():
            if v == majority_val and v > len(nums) // 2:
                return k


if __name__ == "__main__":
    nums = [2,2,1,1,1,2,2]
    solution = Solution()
    print(solution.majorityElement(nums))