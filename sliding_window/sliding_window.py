"""
The goal is to find the maximum sum of any subarray of size k.
A brute-force approach would involve calculating the sum of every subarray of size k, which would take O(n*k) time.
A sliding window approach reduces this to O(n) by maintaining the sum of the current window and "sliding" it across the array.
"""

from typing import List


def sliding_window_bad(nums: List, subarray_length: int) -> int:
    current_sum = 0
    max_sum = 0
    i = 0
    while i < len(nums):
        if i + subarray_length >= len(nums) - 1:
            current_sum = sum(nums[-subarray_length:])
            max_sum = max(current_sum, max_sum)
            break
        current_sum = sum(nums[i : subarray_length + i])
        max_sum = max(current_sum, max_sum)
        i += 1
    return max_sum


if __name__ == "__main__":
    print(sliding_window_bad([2, 5, 3, 6, 7], 2))
