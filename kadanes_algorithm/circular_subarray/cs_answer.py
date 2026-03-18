from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        """
        Find the maximum sum of a subarray in a circular array.
        
        Approach:
        - Case 1: Max subarray doesn't wrap (standard Kadane's)
        - Case 2: Max subarray wraps (total_sum - min_subarray)
        - Return max of both cases, with edge case handling
        """
        def kadane(arr):
            """Helper function to find max subarray sum using Kadane's algorithm"""
            max_sum = arr[0]
            current_sum = arr[0]
            
            for i in range(1, len(arr)):
                current_sum = max(arr[i], current_sum + arr[i])
                max_sum = max(max_sum, current_sum)
            
            return max_sum
        
        # Case 1: Maximum subarray doesn't wrap around
        max_kadane = kadane(nums)
        
        # Case 2: Maximum subarray wraps around
        # This is equivalent to: total_sum - minimum_subarray_sum
        total_sum = sum(nums)
        
        # Find minimum subarray sum
        min_kadane = kadane([-num for num in nums])
        min_subarray = -min_kadane
        
        max_circular = total_sum - min_subarray
        
        # Edge case: if all numbers are negative, min_subarray = total_sum
        # In this case max_circular would be 0, but we need the max negative number
        if max_circular == 0:
            return max_kadane
        
        return max(max_kadane, max_circular)

