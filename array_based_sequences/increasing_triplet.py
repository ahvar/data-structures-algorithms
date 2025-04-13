"""
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such
that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
Example 2:

Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.
Example 3:

Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.

"""
from typing import List
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = None
        second = None
        for i in range(len(nums)):
            if not first:
                first = nums[i]
            elif nums[i] < first:
                first = nums[i]
            for j in range(i, len(nums)):
                if not second:
                    second = nums[j]
                elif nums[j] < second and first < second:
                    second = nums[j]
                    k = j + 1
                    while k <= len(nums) - 1 and nums[k] <= second:
                        k += 1
                    if k == len(nums) - 1:
                        return False            
        return False
                    
                

    
if __name__ == "__main__":
    nums = [0,4,2,1,0,-1,-3]
    solution = Solution()
    print(solution.increasingTriplet(nums))