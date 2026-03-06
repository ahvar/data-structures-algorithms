from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = nums[0]
        max_sum = nums[0]
        start = 0
        for i in range(len(nums) - 1):
            current_sum = max(current_sum + nums[i], nums[i])
            max_sum = max(max_sum, current_sum)
        return max_sum


class TestSolution:

    def setup_method(self):
        self.solution = Solution()

    def test_max(self):
        assert self.solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
