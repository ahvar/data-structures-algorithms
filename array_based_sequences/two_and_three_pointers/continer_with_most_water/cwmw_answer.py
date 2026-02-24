from typing import List


class Solution:

    def maxArea(self, height: List[int]) -> int:
        if not height:
            return 0
        n = len(height)
        left = 0
        right = n - 1
        maxx = 0
        while left < right:
            area = (right - left) * min(height[left], height[right])
            maxx = max(maxx, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxx


if __name__ == "__main__":
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    s = Solution()
