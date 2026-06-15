from typing import List


class Solution:
	def minimizeArrayValue(self, nums: List[int]) -> int:
		"""
		Greedy prefix-sum solution.

		Key idea:
		We are only allowed to move 1 unit from index i to index i - 1.
		That means values can move left, but never right.

		Because of that, for every prefix nums[0..i], the total sum of that
		prefix can never decrease after any operations. So if a final maximum
		value is x, then the first i + 1 elements must be able to hold the
		prefix sum without any element exceeding x.

		Therefore, x must be at least:
			ceil(prefix_sum / (i + 1))

		for every prefix. The minimum valid answer is the maximum of those
		prefix averages.

		Time: O(n)
		Space: O(1)
		"""
		prefix_sum = 0
		answer = 0

		for index, value in enumerate(nums):
			# Step 1: extend the current prefix sum.
			prefix_sum += value

			# Step 2: compute the ceiling of the average for this prefix.
			# ceil(a / b) can be written as (a + b - 1) // b for integers.
			prefix_limit = (prefix_sum + index) // (index + 1)

			# Step 3: the final answer must be large enough for every prefix,
			# so keep the largest required prefix limit seen so far.
			answer = max(answer, prefix_limit)

		return answer
