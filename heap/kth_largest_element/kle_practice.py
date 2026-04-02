from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_array = []

        for num in nums:
            heapq.heappush(min_array, num)

            while len(min_array) > k:
                heapq.heappop(min_array)

        return min_array[0]


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example(self):
        assert self.solution.findKthLargest(nums=[3, 2, 1, 5, 6, 4], k=2) == 5
        assert self.solution.findKthLargest(nums=[3, 2, 3, 1, 2, 4, 5, 5, 6], k=4) == 4
