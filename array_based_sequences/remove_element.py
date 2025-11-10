"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted,
you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are
not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.
"""

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if nums is None or len(nums) == 0:
            return 0
        k = 0
        for read in range(len(nums)):
            if nums[read] != val:
                nums[k] = nums[read]
                k += 1
        return k


if __name__ == "__main__":
    solution = Solution()
