from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        jumps = 0
        current_end = 0
        farthest = 0
        n = len(nums) - 1

        for i in range(n):
            farthest = max(farthest, i + nums[i])

            if i == current_end:
                jumps += 1
                current_end = farthest

                if current_end >= len(nums) - 1:
                    break

        return jumps
