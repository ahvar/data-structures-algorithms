"""
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the
array if you can flip at most k 0's.

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

"""
from typing import List
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = right = zero_count = max_length = 0
        while right < len(nums):
            if nums[right] == 0:
                zero_count += 1
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            current_window_length = right - left + 1
            if current_window_length > max_length:
                max_length = current_window_length
            right += 1

        return max_length
            


if __name__ == "__main__":
    nums = [1,1,1,0,0,0,1,1,1,1,0]
    k = 2
    solution = Solution()
    print(solution.longestOnes(nums,k))