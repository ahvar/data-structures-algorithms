"""
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the
array if you can flip at most k 0's.

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

"""

from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        if nums == None or len(nums) == 0:
            return 0
        zeroes_count = 0
        maxx = 0
        left = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeroes_count += 1
            while zeroes_count > k:
                if nums[left] == 0:
                    zeroes_count -= 1
                left += 1
            maxx = max(maxx, right - left + 1)
        return maxx


if __name__ == "__main__":
    nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    k = 2
    solution = Solution()
    print(solution.longestOnes(nums, k))
