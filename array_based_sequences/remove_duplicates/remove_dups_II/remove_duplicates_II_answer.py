from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums == None or len(nums) == 0:
            return -1
        if len(nums) <= 2:
            return len(nums)
        write = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[write - 2]:
                nums[write] = nums[i]
                write += 1
        return write


if __name__ == "__main__":
    nums = [2, 3, 3, 4, 4, 4, 5, 6, 6, 6, 7, 8]
    solution = Solution()
    solution.removeDuplicates(nums)
