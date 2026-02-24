from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self._min_array = []

        for num in nums:
            heapq.heappush(self._min_array, num)

            while len(self._min_array) > k:
                heapq.heappop(self._min_array)
        return self._min_array[0]


class TestSolution:

    def setup_method(self):
        self.solution = Solution()

    def test_find_largest(self):
        nums = [3, 2, 1, 5, 6, 4]
        k = 2
        assert self.solution.findKthLargest(nums, k) == 5
