from typing import List


class Solution:

    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n - 1
        maxx = 0
        while left < right:
            len = right - left
            h = min(height[left], height[right])
            curr_area = len * h
            maxx = max(curr_area, maxx)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxx
