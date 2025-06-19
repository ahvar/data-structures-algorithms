"""
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.

Example 1:

Input: nums = [10,2]
Output: "210"
Example 2:

Input: nums = [3,30,34,5,9]
Output: "9534330"

"""
from typing import List
class Solution:
    def _compare_ints(self, sa, sb):
        ab = sa + sb
        ba = sb + sa 
        return int(ab) < int(ba)

    def largestNumber(self, nums: List[int]) -> str:
        onlyzero = True
        for num in nums:
            if num > 0:
                onlyzero = False
                break
        if onlyzero:
            return "0"
        right = len(nums) - 1
        while right >= 0:
            for left in range(right):
                if self._compare_ints(str(nums[left]), str(nums[left+1])):
                    nums[left], nums[left+1] = nums[left+1], nums[left]
            right -= 1
        largest = ""
        for num in nums: largest += str(num)
        return largest

if __name__ == "__main__":
    nums = [3,30,34,5,9]
    solution = Solution()
    print(solution.largestNumber(nums))
