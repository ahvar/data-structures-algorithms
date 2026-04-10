from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_sum = 0

        def kadane(arr):
            max_sum = arr[0]
            current_sum = arr[0]

            for i in range(1, len(arr)):
                current_sum = max(arr[i], current_sum + arr[i])
                max_sum = max(max_sum, current_sum)
            return max_sum

        max_kadane = kadane(nums)  # no wrap

        total_sum = sum(nums)

        min_kadane = kadane([-num for num in nums])
        min_subarray = -min_kadane

        max_circular = total_sum - min_subarray

        if max_circular == 0:
            return max_kadane

        return max(max_kadane, max_circular)
