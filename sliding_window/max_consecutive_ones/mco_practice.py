from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        zeroes = 0
        left = 0
        maxx = 0
        for right in range(n):
            if nums[right] == 0:
                zeroes += 1
            while zeroes > k:
                if nums[left] == 0:
                    zeroes -= 1
                left += 1
            maxx = max(maxx, right - left + 1)
        return maxx
