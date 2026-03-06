from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        left = 0
        n = len(nums)
        zeros = 0
        maxx = 0
        for right in range(n):
            if nums[right] == 0:
                zeros += 1
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            maxx = max(maxx, right - left + 1)
        return maxx


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_max_ones(self):
        assert self.solution.longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2) == 6
