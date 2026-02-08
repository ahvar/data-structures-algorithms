"""
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array.
Return 0 if there is no such subarray.

Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.
"""

from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if all(x == 1 for x in nums):
            return len(nums) - 1
        left = max_length = zero_count = length = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            length = right - left + 1
            if zero_count == 1:
                length -= 1
            if length > max_length:
                max_length = length
        return max_length


if __name__ == "__main__":
    nums = [1, 1, 0, 1]
    solution = Solution()
    print(solution.longestSubarray(nums))
