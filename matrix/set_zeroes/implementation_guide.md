# Set Matrix Zeroes Implementation Guide

## Goal

Modify the matrix in place so that every row and column containing a `0` becomes all zeroes.

## Core Idea

Use the first row and first column as marker storage instead of allocating extra sets or arrays.

## Logical Steps

### 1. Check the first row

Before using the first row as markers, determine whether it already contains a zero.

### 2. Check the first column

Before using the first column as markers, determine whether it already contains a zero.

### 3. Mark rows and columns that must be zeroed

Loop through the matrix starting at row `1`, column `1`.
If `matrix[i][j] == 0`, mark:

```python
matrix[i][0] = 0
matrix[0][j] = 0
```

That means row `i` and column `j` must be cleared later.

### 4. Zero the inner part of the matrix

Scan the matrix again from row `1`, column `1`.
If either the row marker or column marker is zero, set the current cell to zero.

### 5. Zero the first row if needed

If the first row originally had a zero, set the whole first row to zero.

### 6. Zero the first column if needed

If the first column originally had a zero, set the whole first column to zero.

## Why This Approach Works

Every zero records its effect in the first cell of its row and the first cell of its column. After all markers are placed, a second pass applies the zeroing without losing information.

## Complexity

- Time: `O(m * n)`
- Extra space: `O(1)`

## Commented Solution

```python
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # Store the matrix dimensions.
        m, n = len(matrix), len(matrix[0])

        # Remember whether the first row or first column
        # must be zeroed at the end.
        first_row = any(matrix[0][j] == 0 for j in range(n))
        first_col = any(matrix[i][0] == 0 for i in range(m))

        # Use the first row and first column as markers.
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Zero cells whose row or column was marked.
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Zero the first row if it originally contained a zero.
        if first_row:
            for j in range(n):
                matrix[0][j] = 0

        # Zero the first column if it originally contained a zero.
        if first_col:
            for i in range(m):
                matrix[i][0] = 0
```