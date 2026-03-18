from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        current_end = 0
        farthest = 0
        jumps = 0
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == current_end:
                jumps += 1
                current_end = farthest

                if current_end >= len(nums) - 1:
                    break
        return jumps


class TestJumps:

    def setup_method(self):
        self.solution = Solution()

    def test_jumps(self):
        assert self.solution.jump([2, 3, 1, 1, 4]) == 2
