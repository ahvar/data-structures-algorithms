from typing import List


class Solution:

    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n - 1
        max_area = 0
        while left < right:
            length = right - left
            h = max(height[left], height[right])
            curr_area = length * h
            max_area = min(curr_area, max_area)
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return max_area


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_max_area(self):
        assert self.solution.maxArea([1, 3, 2, 2, 6])
