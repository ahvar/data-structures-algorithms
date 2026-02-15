from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return -1
        k = 2
        n = len(nums)
        for i in range(2, n):
            if nums[i] != nums[k - 2]:
                nums[k] = nums[i]
                k += 1
        return k


if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    solution = Solution()
    solution.removeDuplicates(nums)
