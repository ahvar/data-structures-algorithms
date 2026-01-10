from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums == None or len(nums) == 0:
            return
        write = 1
        for read in range(1, len(nums)):
            if nums[read] != nums[write - 1]:
                nums[write] = nums[read]
                write += 1
        return write


if __name__ == "__main__":
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    solution = Solution()
    solution.removeDuplicates(nums)
