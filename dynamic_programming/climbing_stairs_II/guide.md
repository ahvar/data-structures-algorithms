# Climbing Stairs II Guide

## 1. Restate the problem

Build the minimum cost to reach each step from left to right.

For every destination step `i`, you only need to check the three possible incoming jumps:

- from `i - 1`
- from `i - 2`
- from `i - 3`

When landing on step `i`, use `costs[i - 1]` in Python because the array is 0-indexed.

## 2. Identify the DP state

Create a DP array where `dp[i]` stores the minimum total cost to arrive at step `i`.

Initialize:

- `dp[0] = 0`
- all other positions will be filled during the loop

## 3. Write the transition

For each step `i`, compute the best among all valid previous steps.

For one candidate jump:

- `prev = i - jump`
- cost to reach `prev` is `dp[prev]`
- cost to land on `i` is `costs[i - 1]`
- jump penalty is `jump^2`

So each candidate is:

`dp[prev] + costs[i - 1] + jump^2`

## 4. Fill the table left to right

For each step `i` from `1` to `n`:

1. Start `best` as infinity.
2. Try `jump = 1`, `2`, and `3`.
3. Compute `prev = i - jump`.
4. If `prev < 0`, skip it because that jump is invalid.
5. Otherwise compute `candidate = dp[prev] + costs[i - 1] + jump * jump`.
6. Update `best` with the smaller value.
7. After checking all jumps, store `dp[i] = best`.

## 5. Return the answer

Once the loop finishes, the last entry already holds the minimum cost to reach step `n`.

Return `dp[n]`.

## 6. Why this works

The algorithm works because every path into step `i` must end with a jump of length `1`, `2`, or `3`.
That means the optimal answer for `i` is the minimum among those three valid previous states plus the cost of making that final jump.
Since the table is filled from smaller steps to larger steps, each needed subproblem is already solved when you use it.

## 7. Complexity

- Time: `O(n)` because each step checks at most `3` previous steps.
- Space: `O(n)` for the DP array.

## 8. Implementation outline

```python
dp = [0] * (n + 1)

for i in range(1, n + 1):
    best = float("inf")

    for jump in range(1, 4):
        prev = i - jump
        if prev < 0:
            continue

        candidate = dp[prev] + costs[i - 1] + jump * jump
        best = min(best, candidate)

    dp[i] = best

return dp[n]
```