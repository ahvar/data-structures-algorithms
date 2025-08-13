"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged,
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
"""
from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Step 1: walk nums2 largest to smallest
        for i in range(n-1,-1,-1):
            # Step 2: pointer to the right edge of nums1
            right = m
            # Step 3: walk left until nums2[i] >= nums1[right-1]
            while right > 0 and nums2[i] < nums1[right-1]:
                right -= 1
            # Step 4: Shift elements rightward
            j = m
            while j > right:
                nums1[j] = nums1[j-1]
                j -= 1
            # Step 5: Insert nums2[i] at the correct position
            nums1[right] = nums2[i]

            # Step 6: Update m to reflect the addition of a new element to
            # the array's valid portion
            m += 1

            
            
            


if __name__ == "__main__":
    solution = Solution()

