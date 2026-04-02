from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr_sum = nums[0]
        for i in range(1, len(nums) - 1):
            num = nums[i]
            curr_sum = max(curr_sum + num, num)
            max_sum = max(curr_sum, max_sum)
        return max_sum
