# Minimum Window Subsequence Guide

## Implementation Steps

1. Measure the lengths of `s1` and `s2` so the loop bounds stay simple.
2. Handle the empty-pattern case immediately, since an empty subsequence is always satisfied.
3. Create a DP array where each position represents the start index of a window ending at the current character of `s1` that matches a prefix of `s2`.
4. Initialize every DP entry to `-1` to mean that prefix has not been matched yet.
5. Scan `s1` from left to right, treating each position as a possible window end.
6. For each character in `s1`, walk through `s2` from right to left so earlier DP states are not overwritten before they are reused.
7. When characters match:
   - Start a new window if this is the first character of `s2`.
   - Otherwise inherit the start index from the previous subsequence prefix.
8. After updating the DP array, check whether the full pattern has been matched.
9. If it has, compute the current window length and keep it only if it is strictly shorter than the best one seen so far.
10. Return the best window at the end, or an empty string if no full match was ever found.

## Coded And Commented Solution

```python
class Solution:
    def min_window(self, s1: str, s2: str) -> str:
        # Measure both strings once so the loop logic stays simple.
        m, n = len(s1), len(s2)

        # An empty pattern is always a valid subsequence.
        if n == 0:
            return ""

        # dp[j] stores the start index of a window ending at the current
        # position in s1 that contains s2[:j + 1] as a subsequence.
        # A value of -1 means that prefix has not been matched yet.
        dp = [-1] * n

        # Track the shortest valid window found so far.
        best_window = ""
        best_length = float("inf")

        # Treat each character in s1 as a possible window end.
        for i in range(m):
            # Update from right to left so dp[j - 1] is still from the
            # previous state when we need it.
            for j in range(n - 1, -1, -1):
                if s1[i] == s2[j]:
                    # Matching the first pattern character starts a new window.
                    if j == 0:
                        dp[j] = i
                    # Matching a later character extends a previously matched prefix.
                    else:
                        dp[j] = dp[j - 1]

            # If the last pattern position has a valid start, the full
            # subsequence has been matched in a window ending at i.
            if dp[n - 1] != -1:
                start = dp[n - 1]
                window_length = i - start + 1

                # Keep only a strictly shorter window so ties remain leftmost.
                if window_length < best_length:
                    best_length = window_length
                    best_window = s1[start:i + 1]

        # If no valid window exists, best_window will still be empty.
        return best_window
```

## Complexity Analysis

- Time: `O(len(s1) * len(s2))` because each character of `s1` scans all of `s2` once.
- Space: `O(len(s2))` for the DP array.