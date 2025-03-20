"""
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].



Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2
"""

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        N = [float("inf")] * n
        N[0] = 0
        for i in range(1, n):
            for j in range(i):
                if j + nums[j] >= i:
                    N[i] = min(N[j] + 1, N[i])
        return N[n - 1]


if __name__ == "__main__":
    nums = [2, 3, 1, 1, 4]
    s = Solution()
    print(s.jump(nums))
