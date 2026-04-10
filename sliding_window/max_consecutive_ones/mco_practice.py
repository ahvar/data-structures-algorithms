from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeroes = 0
        maxx = 0
        left = 0
        n = len(nums)
        for right in range(n):
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

    def test_longest(self):
        assert (
            self.solution.longestOnes(nums=[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k=2) == 6
        )
