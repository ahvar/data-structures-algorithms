from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        N = [1] * n
        longest = 0
        for i in range(n):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    N[i] = max(N[j] + 1, N[i])
        return max(N)
