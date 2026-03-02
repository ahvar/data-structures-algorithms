from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        self.min_array = []
        for num in nums:
            heapq.heappush(self.min_array, num)
            while len(self.min_array) > k:
                heapq.heappop(self.min_array)
        return self.min_array[0]


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_find(self):
        assert self.solution.findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5
