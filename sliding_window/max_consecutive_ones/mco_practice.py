from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0

        maxx = 0
        zeroes = 0
        left = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeroes += 1
            while zeroes > k:
                if nums[left] == 0:
                    zeroes -= 1
                left += 1
            maxx = max(maxx, right - left + 1)
        return maxx


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_max_ones(self):
        assert self.solution.longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2) == 6
