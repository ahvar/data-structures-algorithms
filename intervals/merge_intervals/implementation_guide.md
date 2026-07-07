# Merge Intervals Implementation Guide

## Goal

Combine all overlapping intervals and return a list of disjoint intervals that covers the same ranges.

## Core Idea

Sort the intervals by start value, then scan from left to right.

Once the intervals are sorted, any overlap can only happen with the most recently merged interval.

## Logical Steps

### 1. Sort the intervals by start time

Sort with:

```python
intervals.sort(key=lambda interval: interval[0])
```

This puts possible overlaps next to each other.

### 2. Start the merged list with the first interval

Use the first interval as the initial merged range.

### 3. Scan the remaining intervals

For each interval `[start, end]`, compare it with the end of the last merged interval.

### 4. Merge when intervals overlap

If:

```python
start <= merged[-1][1]
```

then the two intervals overlap, so extend the end of the last merged interval:

```python
merged[-1][1] = max(merged[-1][1], end)
```

The `<=` matters because intervals like `[1, 4]` and `[4, 5]` are also considered overlapping.

### 5. Append when intervals do not overlap

If the current interval starts after the last merged interval ends, add it as a new separate interval.

## Why This Works

After sorting, every new interval only needs to be compared with the last merged interval. If they overlap, they must belong to the same merged block. If they do not overlap, the current interval begins a new block.

## Complexity

- Time: `O(n log n)`. Sorting the `n` intervals takes `O(n log n)`, then the single left-to-right merge pass takes `O(n)`. The sorting step is larger, so it determines the overall time complexity.
- Extra space: `O(n)`. In the worst case, no intervals overlap, so the output list stores all `n` intervals.

## Commented Solution

```python
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort intervals so overlapping ones appear next to each other.
        intervals.sort(key=lambda interval: interval[0])

        # Start with the first interval already merged.
        merged = [intervals[0]]

        # Process each remaining interval.
        for start, end in intervals[1:]:
            last_end = merged[-1][1]

            # If the current interval overlaps the last merged one,
            # extend the end boundary.
            if start <= last_end:
                merged[-1][1] = max(last_end, end)
            else:
                # Otherwise, this interval starts a new merged block.
                merged.append([start, end])

        return merged
```