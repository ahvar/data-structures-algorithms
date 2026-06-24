from typing import List


class Solution:

    def longestOnes(self, nums: List[int], k: int) -> int:
        pass


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_longest(self):
        assert (
            self.solution.longestOnes(nums=[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k=2) == 6
        )
