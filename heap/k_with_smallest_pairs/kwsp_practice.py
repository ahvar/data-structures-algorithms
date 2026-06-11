from typing import List
import heapq


class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        if not nums1 or not nums2 or k <= 0:
            return []
        result = []

        min_heap = []
        n = len(nums1)
        for i in range(min(k, n)):
            heapq.heappush(min_heap, (sum(nums1[i], nums2[0]), i, 0))

        while min_heap and len(result) < k:
            _, i, j = heapq.heappop()
            result.append([nums1[i], nums2[j]])
            if j + 1 < len(nums2):
                heapq.heappush(min_heap, (nums1[i] + nums2[j + 1], i, j + 1))
