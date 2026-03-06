from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.min_array = []

        for i in range(len(nums)):
            heapq.heappush(self.min_array, nums[i])

            while len(self.min_array) > k:
                heapq.heappop(self.min_array)

        return self.min_array[0]
