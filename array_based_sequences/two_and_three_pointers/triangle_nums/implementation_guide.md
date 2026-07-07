# Triangle Number Implementation Guide

Use sorting plus two pointers.

## Logical Steps

1. Sort the array in non-decreasing order.
2. Treat each index `k` from right to left as the largest side.
3. Set two pointers: `left = 0` and `right = k - 1`.
4. If `nums[left] + nums[right] > nums[k]`, then every value between `left` and `right` with `nums[right]` also works, so add `right - left` to the answer and move `right` left.
5. Otherwise, the sum is too small, so move `left` right.
6. Continue until `left >= right`.

## Why This Works

After sorting, if `nums[left] + nums[right] > nums[k]`, then any index between `left` and `right` paired with `right` will also satisfy the triangle condition. That lets us count many triplets at once instead of checking all combinations.

## Complexity

- Time complexity: O(n^2)
- Space complexity: O(1) extra space, ignoring the sort implementation

## Commented Solution

```python
from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # Sort so we can use the largest side fixed at index k.
        nums.sort()
        total = 0

        # Pick each position as the largest side of the triangle.
        for k in range(len(nums) - 1, 1, -1):
            left = 0
            right = k - 1

            while left < right:
                # If the two smaller sides can beat the largest side,
                # then every index from left to right - 1 also works with right.
                if nums[left] + nums[right] > nums[k]:
                    total += right - left
                    right -= 1
                else:
                    # Need a larger sum, so move the left pointer right.
                    left += 1

        return total
```