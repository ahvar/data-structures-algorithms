from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        left = 0
        minn = float("inf")
        curr_sum = 0
        for right in range(len(nums)):
            curr_sum += nums[right]
            while curr_sum >= target:
                minn = min(minn, right - left + 1)
                curr_sum -= nums[left]
                left += 1
        return 0 if minn == float("inf") else minn
