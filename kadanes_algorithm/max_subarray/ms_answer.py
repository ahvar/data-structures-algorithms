from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = nums[0]
        maxx = nums[0]
        for i in range(1, len(nums) - 1):
            num = nums[i]
            current_sum = max(current_sum + num, num)
            maxx = max(maxx, current_sum)
        return maxx


class TestSolution:

    def setup_method(self):
        self.solution = Solution()

    def test_max(self):
        assert self.solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
