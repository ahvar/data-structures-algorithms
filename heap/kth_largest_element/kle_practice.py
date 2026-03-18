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
