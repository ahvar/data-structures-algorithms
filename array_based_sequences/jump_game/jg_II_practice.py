from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        n = len(nums)
        farthest = 0
        jumps = 0
        current_end = 0
        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])

            if i == current_end:
                current_end = farthest
                jumps += 1

                if current_end >= len(nums) - 1:
                    break
        return jumps


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_jump(self):
        assert self.solution.jump(nums=[2, 3, 1, 1, 4]) == 2
