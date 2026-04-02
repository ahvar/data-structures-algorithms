from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def kadane(arr):
            max_sum = arr[0]
            curr_sum = arr[0]

            for i in range(1, len(arr)):
                curr_sum = max(arr[i], curr_sum + arr[i])
                max_sum = max(max_sum, curr_sum)
            return max_sum

        max_kadane = kadane(nums)

        total_sum = sum(nums)

        min_kadane = kadane([-num for num in nums])
        min_subarray = -min_kadane

        max_circular = total_sum - min_subarray

        if max_circular == 0:
            return max_kadane

        return max(max_kadane, max_circular)
