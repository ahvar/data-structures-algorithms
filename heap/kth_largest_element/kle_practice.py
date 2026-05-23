from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        for num in nums:
            heapq.heappush(min_heap, num)
            while k < len(min_heap):
                heapq.heappop(min_heap)
        return min_heap[0]


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_find(self):
        assert self.solution.findKthLargest(nums=[3, 2, 1, 5, 6, 4], k=2) == 5
