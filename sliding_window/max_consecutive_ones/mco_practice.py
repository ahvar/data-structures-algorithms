from typing import List


class Solution:

    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        zeroes = 0
        longest = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeroes += 1
            while zeroes > k:
                if nums[left] == 0:
                    zeroes -= 1
                left += 1
            longest = max(longest, right - left + 1)
        return longest


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_longest(self):
        assert (
            self.solution.longestOnes(nums=[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k=2) == 6
        )
