"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
and two integers m and n, representing the number of elements in nums1 and nums2
respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be
stored inside the array nums1. To accommodate this, nums1 has a length of m + n,
where the first m elements denote the elements that should be merged, and the last
n elements are set to 0 and should be ignored. nums2 has a length of n.

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
"""

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(n - 1, -1, -1):
            j = m
            while j > 0 and nums2[i] > nums1[j - 1]:
                nums1[j] = nums1[j - 1]
                j -= 1
            nums1[j] = nums2[i]
            m += 1


if __name__ == "__main__":
    nums1 = [1, 2, 3, 5, 0, 0, 0, 0, 0]
    nums2 = [3, 4]
    m = 4
    n = 5
    solution = Solution()
    print(solution.merge(nums1, m, nums2, n))
