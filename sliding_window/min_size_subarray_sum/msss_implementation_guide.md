# Minimum Size Subarray Sum Implementation Guide

## Idea

Use a sliding window. Since all numbers are positive, expanding the window increases the sum and shrinking it decreases the sum, so both pointers only move forward.

## Step-by-Step Operations

1. Start `left = 0`, `curr_sum = 0`, and `min_len = float("inf")`.
2. Move `right` across the array and add `nums[right]` to `curr_sum`.
3. Whenever `curr_sum >= target`, the current window is valid.
4. Record its length with `right - left + 1`.
5. Shrink the window by subtracting `nums[left]` and moving `left += 1`.
6. Keep shrinking while the window stays valid.
7. Return `0` if no valid window was found, otherwise return `min_len`.

## Why `right - left + 1` Is Correct

The window includes both ends, from index `left` through index `right`.
So its length is inclusive: `right - left + 1`.

Example:

- `left = 2`, `right = 4` means the window is `nums[2], nums[3], nums[4]`, which has length `3`.
- `4 - 2 + 1 = 3`

Without the `+ 1`, you count gaps between indices, not elements.

## Why This Works

Each time `right` moves, the window expands. Each time the sum is large enough, `left` moves to make the window as short as possible. This checks every valid window and keeps the minimum length.

## Complexity

- Time: `O(n)` because each pointer moves forward at most `n` times.
- Space: `O(1)` extra space.

## Commented Solution

```python
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        min_len = float("inf")
        curr_sum = 0

        for right in range(len(nums)):
            # Expand the window by including nums[right]
            curr_sum += nums[right]

            # Shrink the window while it still satisfies the target
            while curr_sum >= target:
                min_len = min(min_len, right - left + 1)
                curr_sum -= nums[left]
                left += 1

        return 0 if min_len == float("inf") else min_len
```
