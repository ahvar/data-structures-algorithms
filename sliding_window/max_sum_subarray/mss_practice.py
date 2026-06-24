from typing import List


class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        if not nums or k <= 0 or k > len(nums):
            return 0

        window_sum = sum(nums[:k])
        max_sum = window_sum

        for right in range(k, len(nums)):
            window_sum += nums[right]
            window_sum -= nums[right - k]
            max_sum = max(max_sum, window_sum)
        return max_sum
