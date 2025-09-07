"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
"""
from typing import List
from queue import Queue
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % (len(nums) - 1)
        temp = nums[-k:]
        for i in range(len(nums) - 1, k - 1, -1):
            nums[i] = nums[i-k]
        for i in range(k):
            nums[i] = temp[i]








if __name__ == "__main__":
    nums = [1,2,3,4,5]
    k = 2
    solution = Solution()
    solution.rotate(nums, k)