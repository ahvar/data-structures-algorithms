# Kth Largest Element Analysis

## Problem

Given an integer array `nums` and an integer `k`, return the `k`th largest element in the array.

This means:

- `k = 1` gives the largest element.
- `k = 2` gives the second largest element.
- We care about sorted position, not distinct values.

The prompt also asks for a solution without sorting the whole array.

## Correct Approach

The clean heap-based solution is to maintain a **min-heap of size `k`**.

### Why a min-heap works

We want the `k` largest values seen so far.

If we keep exactly those `k` values in a min-heap:

- The smallest value in that heap is the `k`th largest overall.
- Any value smaller than the heap minimum is not useful once the heap already contains `k` larger candidates.

So the heap stores the top `k` elements seen so far, and the root of the heap is the answer.

## Implementation Steps

### Step 1: Start with an empty min-heap

```python
min_heap = []
```

Python's `heapq` implements a min-heap, which is exactly what we need.

### Step 2: Push each number into the heap

```python
for num in nums:
    heapq.heappush(min_heap, num)
```

Each new number is added to the heap.

### Step 3: Trim the heap back to size `k`

```python
while len(min_heap) > k:
    heapq.heappop(min_heap)
```

If the heap grows larger than `k`, remove the smallest value.

That removal is safe because:

- once we have more than `k` values,
- the smallest one cannot be the `k`th largest anymore,
- so we discard it.

### Step 4: Return the heap root

```python
return min_heap[0]
```

At the end:

- the heap contains the `k` largest elements in the array,
- and the smallest among them is the `k`th largest element.

## Corrected Implementation

```python
from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []

        for num in nums:
            heapq.heappush(min_heap, num)

            while len(min_heap) > k:
                heapq.heappop(min_heap)

        return min_heap[0]
```

## What Was Wrong in the Original Implementation

The original code used:

```python
heapq.heappush(num, min_heap)
```

But `heapq.heappush` expects arguments in this order:

```python
heapq.heappush(heap, item)
```

So the correct line is:

```python
heapq.heappush(min_heap, num)
```

That was the only logic bug in the implementation.

## Example Walkthrough

Example:

```python
nums = [3, 2, 1, 5, 6, 4]
k = 2
```

We keep only the 2 largest values seen so far.

### Process each number

1. Add `3` -> heap = `[3]`
2. Add `2` -> heap = `[2, 3]`
3. Add `1` -> heap = `[1, 3, 2]`, size is 3, pop smallest -> heap = `[2, 3]`
4. Add `5` -> heap = `[2, 3, 5]`, pop smallest -> heap = `[3, 5]`
5. Add `6` -> heap = `[3, 5, 6]`, pop smallest -> heap = `[5, 6]`
6. Add `4` -> heap = `[4, 6, 5]`, pop smallest -> heap = `[5, 6]`

Now the heap contains the 2 largest elements: `[5, 6]`.

The smallest of those is `5`, so the answer is:

```python
5
```

## Why This Is Better Than Sorting

Sorting the whole array would take:

- `O(n log n)` time

This heap solution takes:

- `O(n log k)` time

That is better when `k` is much smaller than `n`.

## Complexity

### Time Complexity

`O(n log k)`

Reason:

- We process each of the `n` numbers once.
- Each push or pop costs `O(log k)` because the heap never grows beyond size `k + 1`.

### Space Complexity

`O(k)`

Reason:

- The heap stores at most `k` elements.

## Key Insight to Remember

For "kth largest" problems:

- use a **min-heap of size `k`**
- keep only the `k` largest values seen so far
- the heap root is the answer

## Summary

The corrected implementation works by maintaining a min-heap of the top `k` elements. Every time the heap grows too large, it removes the smallest element. After processing all numbers, the heap root is the `k`th largest value.

This gives an efficient solution with `O(n log k)` time and `O(k)` space.