from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return
        k = 0
        n = len(nums)
        for read in range(n):
            if nums[read] != val:
                nums[k] = nums[read]
                k += 1
        return k
