from typing import List
import heapq


class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        if not nums1 or not nums2 or k <= 0:
            return []
        n = len(nums1)
        heap = []
        pairs = []
        for i in range(min(k, len(nums1))):
            heapq.heappush(heap, (nums1[i] + nums2[i], i, 0))

        while heap and len(heap) < k:
            _, i, j = heapq.heappop()
            pairs.append([nums1[i], nums2[j]])
            if j + 1 < len(nums2):
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))

        return pairs
