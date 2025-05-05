"""
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed, the only constraint stopping you from robbing
each of them is that adjacent houses have security systems connected and it will automatically
contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum
amount of money you can rob tonight without alerting the police.
"""
from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)
        max_money = [0] * (n + 1)
        max_money[0] = 0
        max_money[1] = nums[0]
        for i in range(2,n+1):
            max_money[i] = max(max_money[i-1], max_money[i-2] + nums[i-1])
        return max_money[n]



if __name__ == "__main__":
    nums = [1,2,3,1]
    solution = Solution()
    print(solution.rob(nums))