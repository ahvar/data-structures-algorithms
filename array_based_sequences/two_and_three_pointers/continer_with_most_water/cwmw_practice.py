from typing import List


class Solution:

    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxx = 0
        while left < right:
            area = (right - left) * min(height[left], height[right])
            maxx = max(maxx, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxx


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_max_area(self):
        assert self.solution.maxArea([1, 3, 2, 2, 6])
