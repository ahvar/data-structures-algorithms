"""
You are given an integer array nums. You are initially positioned at the array's first index,
and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.
"""

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_reach = 0
        for i in range(n):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])
            if max_reach >= n - 1:
                return True
        return False


if __name__ == "__main__":
    nums = [2, 3, 1, 1, 4]
    solution = Solution()
    solution.canJump(nums)
