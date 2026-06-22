from typing import List


class Solution:

    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        maxx = 0
        left = 0
        right = n - 1
        while left < right:
            area = (right - left) * min(height[left], height[right])
            maxx = max(area, maxx)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxx
