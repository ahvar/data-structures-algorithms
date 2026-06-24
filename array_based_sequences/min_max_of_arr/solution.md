# Minimum Maximum of Array

## Idea

Use a greedy prefix-sum observation.

You are only allowed to move `1` unit from index `i` to index `i - 1`, so values can move left but never right.

Because of that, for every prefix `nums[0..i]`, the total sum of that prefix can never decrease after any operations. If the final maximum value is `x`, then the first `i + 1` elements must be able to hold that prefix sum without any element exceeding `x`.

So for each prefix, `x` must be at least:

`ceil(prefix_sum / (i + 1))`

That means every prefix creates a lower bound on the answer. The minimum valid answer is the largest of those prefix bounds.

## Steps

1. Walk through the array from left to right.
2. Keep a running prefix sum.
3. At each index, compute the prefix average rounded up.
4. Track the largest rounded-up prefix average seen so far.
5. Return that largest value.

## Why It Works

Since values can only move left, no prefix can lose total value. So each prefix must still fit within its number of positions under the final maximum. The answer therefore has to satisfy every prefix, and the tightest requirement is the largest rounded-up prefix average.

## Code

```python
from typing import List


class Solution:
	def minimizeArrayValue(self, nums: List[int]) -> int:
		prefix_sum = 0
		answer = 0

		for index, value in enumerate(nums):
			# Add the current number into the running prefix total.
			prefix_sum += value

			# Compute the rounded-up average for this prefix.
			prefix_limit = (prefix_sum + index) // (index + 1)

			# The answer must satisfy every prefix, so keep the largest bound.
			answer = max(answer, prefix_limit)

		return answer
```

## Complexity

- Time: `O(n)`
- Space: `O(1)`
