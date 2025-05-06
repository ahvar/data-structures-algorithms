"""
Given an array nums of n integers, return an array of all the unique quadruplets
[nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n (indicies are >= 0 and < n)
a, b, c, and d are distinct (indicies are distinct)
nums[a] + nums[b] + nums[c] + nums[d] == target (values at indicies sum to target)

You may return the answer in any order.
"""
from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        unique_quads = []
        for left in range(n-3):
            if left > 0 and nums[left] == nums[left - 1]:
                continue

            right = left + 1
            unique_quad = [nums[left]]
            while right < n:
                if sum(unique_quad) < target and len(unique_quad) < 4:
                    unique_quad.append(nums[right])
                elif len(unique_quad) > 4 and sum(unique_quad) != target:
                    unique_quad = [nums[left]]
                elif len(unique_quad) == 4 and sum(unique_quad) == target:
                    unique_quads.append(unique_quad)
                    unique_quad = [nums[left]]
                right += 1
        return unique_quads

if __name__ == "__main__":
    nums = [1,0,-1,0,-2,2]
    target = 0
    solution = Solution()
    print(solution.fourSum(nums, target))