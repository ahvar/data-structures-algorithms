from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums == None:
            return -1
        if len(nums) < 2:
            return 1
        write = 2
        n = len(nums)
        for i in range(2, n):
            if nums[i] != nums[write - 2]:
                nums[write] = nums[i]
                write += 1
        return write


if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    solution = Solution()
    solution.removeDuplicates(nums)
