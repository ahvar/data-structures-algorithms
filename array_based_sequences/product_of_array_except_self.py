"""
Given an integer array nums, return an array answer such that answer[i] is equal to the
product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""

from typing import List

import math


def alternate(nums):
    suffix_prod = 0
    prefix_prod = 0
    answer = [0 for i in range(len(nums))]
    i = 0
    j = len(nums) - 1
    while i < j:
        if i == j:
            prefix_prod = nums[:j]
            suffix_prod = nums[i + 1 :]
            answer[i] = prefix_prod * suffix_prod
        else:
            if i == 0:
                answer[i] = math.prod(nums[i + 1 :])
            else:
                suffix_prod = math.prod(nums[:i])
                prefix_prod = math.prod(nums[i + 1 :])
                answer[i] = suffix_prod * prefix_prod
            if j == len(nums) - 1:
                answer[j] = math.prod(nums[j - 1 :: -1])
            else:
                suffix_prod = math.prod(nums[j - 1 :: -1])
                prefix_prod = math.prod(nums[len(nums) - 1 : j : -1])
                answer[j] = suffix_prod * prefix_prod
        i += 1
        j -= 1
    return answer


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [0] * len(nums)
        for i in range(len(nums)):
            if i == 1:
                answer[i] = nums[i - 1]
            elif i > 1:
                answer[i] = answer[i - 1] * nums[i - 1]
        suffixes = [0] * len(nums)
        for j in range(len(nums) - 1, -1, -1):
            if j == len(nums) - 2:
                suffixes[j] = nums[j + 1]
                answer[j] = suffixes[j] * answer[j]
            elif j < len(nums) - 2:
                suffixes[j] = nums[j + 1] * suffixes[j + 1]
                if j == 0:
                    answer[j] = suffixes[j]
                else:
                    answer[j] = answer[j] * suffixes[j]
        return answer


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    s = Solution()
    print(s.productExceptSelf(nums))
