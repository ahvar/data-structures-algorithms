# Longest Common Subsequence - Logic and Complexity

## Core Idea

Let `dp[i][j]` be the length of the longest common subsequence between:

- the first `i` characters of `text1`
- the first `j` characters of `text2`

The table has size `(n + 1) x (m + 1)` so the extra row and column handle empty prefixes.

## Transition

For each pair of positions:

```python
if text1[i - 1] == text2[j - 1]:
    dp[i][j] = dp[i - 1][j - 1] + 1
else:
    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
```

Why this works:

- If the current characters match, they can extend a common subsequence by `1`.
- If they do not match, the best answer must come from skipping one character from either `text1` or `text2`.

## Result

After filling the table, the final answer is:

```python
dp[n][m]
```

which is the LCS length for the full two strings.

## Example Intuition

If two characters match, move diagonally and add `1`.
If they do not match, take the larger value from above or left.

That builds the best LCS length for every prefix pair until the full strings are covered.

## Complexity

Let `n = len(text1)` and `m = len(text2)`.

- **Time:** `O(n * m)` because every table cell is computed once.
- **Space:** `O(n * m)` because the full DP table is stored.

This implementation returns only the LCS length, not the subsequence itself.
