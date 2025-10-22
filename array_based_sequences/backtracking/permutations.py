"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
""" 
from typing import List
class Solution:
    def _something(self, perm):
        pass
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums[:]]
        permutes: List[List[int]] = []
        for i in range(len(nums)):
            current = nums[i]
            rest = nums[:i] + nums[i+1:]
            for tail_perm in self.permute(rest):
                permutes.append([current] + tail_perm)
                
        return permutes




if __name__ == "__main__":
    nums = [1,2,3]
    solution = Solution()
    print(solution.permute(nums))
    
