"""
Given an integer array nums, return the length of the longest strictly increasing subsequence.

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1

"""

from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        N = [1] * n
        longest = 0
        for i in range(1, n):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    N[i] = max(N[j] + 1, N[i])
        return max(N)


if __name__ == "__main__":
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    s = Solution()
    print(s.lengthOfLIS(nums))
