"""
Given an array of positive integers nums and a positive integer target, return the
minimal length of a subarray whose sum is greater than or equal to target. If there
is no such subarray, return 0 instead.

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
"""
from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        min_len = n + 1
        curr_sum = 0
        left, right = 0, 0
        while right < n:
            curr_sum += nums[right]
            while curr_sum >= target:
                min_len = min(min_len, right - left + 1)
                curr_sum -= nums[left]
                left += 1
            right += 1
        if min_len == n + 1:
            return 0
        return min_len


if __name__ == "__main__":
    nums = [1,2,3,4,5]
    target = 15
    solution = Solution()
    print(solution.minSubArrayLen(target, nums))