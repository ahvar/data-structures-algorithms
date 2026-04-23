from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n  # if k is longer than n
        temp = nums[-k:]  # the integers we're going to overwrite
        for i in range(n - 1, k - 1, -1):
            nums[i] = nums[i - k]
        for j in range(k):
            nums[j] = temp[j]

    def alt_slicing(self, nums: List[int], k: int) -> None:
        pass


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    k = 2
    solution = Solution()
    solution.rotate(nums, k)
