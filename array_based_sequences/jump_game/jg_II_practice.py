from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        start = 0
        current_end = 0
        farthest = 0
        jump_count = 0
        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])

            if i == current_end:
                jump_count += 1
                current_end = farthest

                if current_end >= n - 1:
                    break

        return jump_count
