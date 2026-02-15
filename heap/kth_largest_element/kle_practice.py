from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self._min_heap = []
        for num in nums:
            heapq.heappush(self._min_heap, num)
            if len(self._min_heap) > k:
                heapq.heappop()
        return self._min_heap[0]
