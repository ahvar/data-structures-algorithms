"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container."
"""

from typing import List
from rich import print as rprint


class Solution:
    def max_area_brute_force(self, height: List[int]) -> int:
        max_area = 0
        for left in range(len(height) - 1):
            for right in range(len(height) - 1, 0, -1):
                max_area = max(
                    max_area, (right - left) * min(height[left], height[right])
                )
        return max_area

    def max_area_optimal(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1
        while left < right:
            max_area = max(max_area, (right - left) * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
            else:
                left += 1
                right -= 1
        return max_area


if __name__ == "__main__":
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    s = Solution()
    rprint(s.max_area_brute_force(height))
