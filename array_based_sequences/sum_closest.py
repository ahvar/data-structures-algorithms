"""
Given an integer array nums of length n and an integer target, find
three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).

notes:
1. We're looking for a value that is the closest to our target; it could be of greater or lesser value. Our target is somewhere
in the range of 
"""
from typing import List
class Solution:
    def _target_index(self, sorted_nums, target):
        right = len(sorted_nums) - 1
        left = 0
        # partition nums with target + 1
        while left < right:
            mid = (len(sorted_nums) // 2) + left
            guess = sorted_nums[mid]
            if guess == target:
                return mid
                #return min(target - sorted_nums[mid + 1], target - sorted_nums[mid - 1])
            if guess < target:
                left = mid
            elif guess > target:
                right = mid + 1
        return None

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # sort nums
        nums.sort()
        closest_sum = self._target_index(nums)

    def _another_way(self, nums):
        # sort nums
        nums.sort
        # get all integers from 0 to the largest value in nums
        all_nums = [ _ for _ in range(nums[-1])]
        # get the index of the target value
        target_index = self._target_index(all_nums)
        # the closest value to target is the minimum difference between neighbors
        if (all_nums[target_index + 1] - target) < (target - all_nums[target_index - 1]):
            pass

    def _and_another_way(self, nums, target):
        nums.sorted()
        target_greater = target
        target_lesser = target
        target_greater_index = None
        target_lesser_index = None
        while target_greater_index is None and target_lesser_index is None:
            target_greater += 1
            target_lesser -= 1
            target_lesser_index = self._target_index(nums, target_greater)
            target_greater_index = self._target_index(nums, target_lesser)
            

        
        

        
            
            



if __name__ == "__main__":
    nums = [-1,2,1,-4]
    target = 1
    solution = Solution()
    print(solution.threeSumClosest(nums, target))