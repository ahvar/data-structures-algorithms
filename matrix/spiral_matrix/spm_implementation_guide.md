# Spiral Matrix Implementation Guide

## Idea

Traverse the matrix layer by layer.

For each layer, keep four boundaries:

- `top`: first remaining row
- `bottom`: last remaining row
- `left`: first remaining column
- `right`: last remaining column

At each round, read:

1. the top row from left to right
2. the right column from top to bottom
3. the bottom row from right to left
4. the left column from bottom to top

After finishing one layer, move the boundaries inward.

## Step-by-Step Operations

1. Create an empty result list.
2. Handle an empty matrix early by returning `[]`.
3. Initialize four pointers:
   - `top = 0`
   - `bottom = len(matrix) - 1`
   - `left = 0`
   - `right = len(matrix[0]) - 1`
4. While the boundaries still define a valid rectangle (`top <= bottom` and `left <= right`), process one outer layer.
5. Traverse the top row from `left` to `right` and append each value.
6. Move `top` down by `1` because that row is finished.
7. Traverse the right column from `top` to `bottom` and append each value.
8. Move `right` left by `1` because that column is finished.
9. Before traversing the bottom row, check that `top <= bottom`.
   If true, traverse the bottom row from `right` to `left`.
10. Move `bottom` up by `1` after finishing that row.
11. Before traversing the left column, check that `left <= right`.
    If true, traverse the left column from `bottom` to `top`.
12. Move `left` right by `1` after finishing that column.
13. Repeat until all layers are consumed.
14. Return the result list.

## Why The Extra Checks Matter

The checks before the bottom-row and left-column traversals prevent duplicates when the remaining layer is only:

- one row
- one column

Without those checks, the algorithm could visit the same cells twice.

## Complexity

- Time: `O(m * n)` because every element is visited exactly once.
- Space: `O(1)` extra space, ignoring the output list.

## Commented Solution

```python
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        result = []
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # Traverse the top row
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1

            # Traverse the right column
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1

            # Traverse the bottom row if it still exists
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1

            # Traverse the left column if it still exists
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1

        return result
```
