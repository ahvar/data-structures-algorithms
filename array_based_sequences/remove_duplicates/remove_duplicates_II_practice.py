from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return -1

        write = 2
        n = len(nums)
        for read in range(2, n):
            if nums[read] != nums[write - 2]:
                nums[write] = nums[read]
                write += 1
        return write


if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    solution = Solution()
    solution.removeDuplicates(nums)
