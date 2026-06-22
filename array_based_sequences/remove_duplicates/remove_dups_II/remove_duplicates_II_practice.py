from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        k = 2
        for i in range(2, n):
            if nums[i] != nums[k - 2]:
                nums[k] = nums[i]
                k += 1
        return k
