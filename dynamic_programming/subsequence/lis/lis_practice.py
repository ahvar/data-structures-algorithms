from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = [1] * len(nums)
        longest = 0
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    N[i] = max(N[j] + 1, N[i])
        return max(N)
