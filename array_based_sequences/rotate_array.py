"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
"""
from typing import List
from queue import Queue
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        fifo = Queue()
        for _ in range(k):
            fifo.put(nums.pop())
            nums.insert(0, fifo.get())
        print(nums)

if __name__ == "__main__":
    nums = [-1,-100,3,99]
    k = 2
    solution = Solution()
    solution.rotate(nums, k)