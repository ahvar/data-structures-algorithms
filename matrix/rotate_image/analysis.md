# Rotate Image Analysis

## Goal

Given an `n x n` matrix, rotate it 90 degrees clockwise **in place**.

Example:

```python
[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
```

Should become:

```python
[
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3],
]
```

The main constraint is that we cannot build a second matrix and copy values into it.

## Core Idea

A 90-degree clockwise rotation can be broken into two simpler in-place operations:

1. Transpose the matrix.
2. Reverse each row.

That is exactly what the solution in `ri_answer.py` does.

## Why This Works

### 1. Transpose the matrix

Transposing swaps rows and columns.

For every position `(i, j)`, swap:

```python
matrix[i][j] <-> matrix[j][i]
```

Starting matrix:

```python
[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
```

After transpose:

```python
[
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
]
```

### 2. Reverse each row

Now reverse every row from left to right:

```python
[1, 4, 7] -> [7, 4, 1]
[2, 5, 8] -> [8, 5, 2]
[3, 6, 9] -> [9, 6, 3]
```

Result:

```python
[
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3],
]
```

That matches the required clockwise rotation.

## Implementation Walkthrough

### Step 1: Get the matrix size

```python
n = len(matrix)
```

Since the matrix is square, `n` is both the number of rows and the number of columns.

### Step 2: Transpose in place

```python
for i in range(n):
    m = len(matrix[i])
    for j in range(i, m):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
```

Important detail:

- The inner loop starts at `j = i`, not `0`.
- This avoids swapping the same pair twice.

For example, if you swap `(0, 1)` with `(1, 0)`, you do not want to later swap `(1, 0)` with `(0, 1)` again.

So this loop only walks the diagonal and the upper-right triangle of the matrix.

### Step 3: Reverse each row

```python
for row in matrix:
    row.reverse()
```

After the transpose, reversing each row completes the clockwise rotation.

## Small Example Trace

Start:

```python
[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
```

After transpose swaps:

- swap `(0, 1)` and `(1, 0)` -> `2` and `4`
- swap `(0, 2)` and `(2, 0)` -> `3` and `7`
- swap `(1, 2)` and `(2, 1)` -> `6` and `8`

Matrix becomes:

```python
[
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
]
```

After reversing each row:

```python
[
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3],
]
```

## Time and Space Complexity

- Time: `O(n^2)`
  We visit matrix cells through the transpose and then reverse each row.
- Space: `O(1)` extra space
  All changes are made directly inside the input matrix.

## Common Pitfalls

### Swapping every pair twice

If the inner loop starts at `0`, many values will be swapped and then swapped back. Starting from `j = i` avoids that.

### Using an extra matrix

That would work logically, but it violates the in-place requirement.

### Reversing columns instead of rows

For a clockwise rotation using the transpose approach, you reverse each **row** after transposing.

If you transpose and then reverse each **column**, you get a different transformation.

## Mental Model

You can remember clockwise rotation as:

```python
transpose + reverse each row
```

And counterclockwise rotation as:

```python
transpose + reverse each column
```

## Reference Implementation

```python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        for i in range(n):
            for j in range(i, len(matrix[i])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for row in matrix:
            row.reverse()
```

## Summary

The solution works because a clockwise 90-degree rotation is equivalent to:

1. Reflecting the matrix across its main diagonal.
2. Reversing each row.

This satisfies the in-place requirement, is easy to reason about, and runs in `O(n^2)` time with `O(1)` extra space.