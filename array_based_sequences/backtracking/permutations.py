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
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) == 0:
            return []

        result = []

        def _backtrack(permutation):
            if len(permutation) == len(nums):
                result.append(permutation[:])
                return
            for num in nums:
                if num not in permutation:
                    permutation.append(num)
                    _backtrack(permutation)
                    permutation.pop()

        _backtrack([])
        return result


if __name__ == "__main__":
    nums = [1, 2, 3]
    solution = Solution()
    print(solution.permute(nums))
