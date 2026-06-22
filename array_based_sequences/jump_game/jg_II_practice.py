from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        current_end = nums[0]
        farthest = nums[0]
        for i in range(n - 1):
            farthest = max(farthest, nums[i] + 1)

            if i == current_end:
                count += 1
                current_end = farthest

                if current_end >= len(nums) - 1:
                    break
        return count
