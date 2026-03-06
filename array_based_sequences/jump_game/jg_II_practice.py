from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        farthest = 0
        current_end = 0
        count = 0
        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])

            if i == current_end:
                count += 1
                current_end = farthest

                if current_end >= len(nums) - 1:
                    break
        return count
