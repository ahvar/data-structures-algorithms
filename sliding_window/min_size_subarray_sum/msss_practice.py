from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        min_len = float("inf")
        total = 0
        for right in range(n):
            total += nums[right]
            while total >= target:
                min_len = min(right - left + 1, min_len)
                total -= nums[left]
                left += 1
        return 0 if min_len == float("inf") else min_len


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_min(self):
        assert self.solution.minSubArrayLen(target=7, nums=[2, 3, 1, 2, 4, 3]) == 2
