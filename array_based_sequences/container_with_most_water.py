"""
You are given an integer array height of length n.
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container."
"""

from typing import List

class Solution:


    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return -1
        maxx = 0
        left = 0
        right = len(height) - 1
        while left < right:
            height = min(height[left], height[right])
            length = right - left
            maxx = max(maxx, height * length)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxx



if __name__ == "__main__":
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    s = Solution()