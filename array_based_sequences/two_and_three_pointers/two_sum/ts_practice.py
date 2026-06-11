from typing import List


class Solution:

    def twoSum(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return True
        return False


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_two(self):
        assert self.solution.twoSum([1, 3, 4, 6, 8, 10, 13], 13) is True
        assert self.solution.twoSum([1, 3, 4, 6, 8, 10, 13], 6) is False
