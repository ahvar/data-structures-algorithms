from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if nums == None or len(nums) == 0:
            return 0
        write = 0
        n = len(nums)
        for i in range(n):
            if nums[i] != val:
                nums[write] = nums[i]
                write += 1
        return write
