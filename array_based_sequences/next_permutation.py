"""
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.
"""

from typing import List


class Solution:
    def next_permutation(self, nums: List[int]) -> None:
        i = len(nums) - 2
        # Identify from the end of the list the first position i where nums[i] < nums[i+1].
        while nums[i] >= nums[i + 1] and i >= 0:
            i -= 1
        if i == -1:
            nums.reverse()
            return
        # From the end again, find an index j such that nums[j] > nums[i].
        j = len(nums) - 1
        while nums[j] <= nums[i] and j >= 0:
            j -= 1
        if j == -1:
            # what to do?
            pass
        # Swap nums[i] and nums[j], then reverse the sub-array to the right of i.
        nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1 :] = reversed(nums[i + 1 :])
        return


if __name__ == "__main__":
    nums = [1, 2, 3]
    s = Solution()
    s.next_permutation(nums)
    print(nums)
