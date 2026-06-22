from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        N = [1] * n
        for i in range(1, n):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    N[i] = max(N[j] + 1, N[i])
        return max(N)
