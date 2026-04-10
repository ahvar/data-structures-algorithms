from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        left = 0
        curr_sum = 0
        min_len = float("inf")
        for right in range(n):
            curr_sum += nums[right]

            while curr_sum >= target:
                min_len = min(min_len, right - left + 1)
                curr_sum -= nums[left]
                left += 1
        return 0 if min_len == float("inf") else min_len


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_min_sub(self):
        assert self.solution.minSubArrayLen(target=7, nums=[2, 3, 1, 2, 4, 3]) == 2
