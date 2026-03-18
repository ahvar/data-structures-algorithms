# Factorial Trailing Zeroes - Analysis

## Problem
Given an integer n, return the number of trailing zeroes in n!.

## Key Insight

Trailing zeroes come from factors of **10**, and `10 = 2 × 5`.

In any factorial, there are **always more 2s than 5s** (every even number gives a 2, but only every 5th number gives a 5). So:

> **Trailing zeroes = count of factor 5 in n!**

## Counting Factors of 5

For `n = 25`, let's count 5s manually:
- 5 → one 5
- 10 → one 5  
- 15 → one 5
- 20 → one 5
- 25 → **two 5s** (25 = 5²)

Total = 6 trailing zeroes

## The Formula

```
count = n/5 + n/25 + n/125 + n/625 + ...
```

| Term | What it counts |
|------|----------------|
| n/5 | Numbers divisible by 5 (one factor of 5) |
| n/25 | Numbers divisible by 25 (extra factor of 5) |
| n/125 | Numbers divisible by 125 (yet another factor) |

For `n = 25`: `25/5 + 25/25 = 5 + 1 = 6` ✓

## Why O(log n)?

Each iteration divides by 5. The loop runs until `5^k > n`, meaning:
- `k = log₅(n)` iterations
- This is **O(log n)** time complexity

## Complexity
- **Time:** O(log₅ n) = O(log n)
- **Space:** O(1)

## Implementation

```python
class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        power_of_5 = 5
        while power_of_5 <= n:
            count += n // power_of_5
            power_of_5 *= 5
        return count
```

## Step-by-Step Trace for n = 100

| Iteration | power_of_5 | n // power_of_5 | count |
|-----------|------------|-----------------|-------|
| Start     | 5          | -               | 0     |
| 1         | 5          | 20              | 20    |
| 2         | 25         | 4               | 24    |
| 3         | 125        | 0               | 24    |
| Exit      | 125 > 100  | -               | 24    |

**Result: 24 trailing zeroes in 100!**
