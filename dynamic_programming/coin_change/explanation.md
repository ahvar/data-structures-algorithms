# Coin Change Implementation Guide

This solution uses bottom-up dynamic programming.

Let `dp[i]` mean: the minimum number of coins needed to make amount `i`.

## Core idea

To compute `dp[i]`, try treating each coin as the last coin used.

If the current coin is `coin`, then before using it we must already have formed the smaller amount `i - coin`.
That is why the transition is:

$$
dp[i] = \min(dp[i],\ dp[i - coin] + 1)
$$

This works because:
- `dp[i - coin]` is the fewest coins needed to make the remaining amount.
- `+ 1` counts the one extra coin we are using now.

So for every valid last coin, we ask:
"If I finish amount `i` with this coin, how many coins would that take in total?"
Then we keep the minimum.

## Why subtracting the coin makes sense

Suppose we want to make amount `11` and we try coin `5`.

If `5` is the last coin used, then the rest of the amount must be `11 - 5 = 6`.
So the problem becomes:
- solve amount `6` as efficiently as possible
- then add one more coin of value `5`

If `dp[6] = 2`, then using a final `5` gives:

$$
dp[11] = dp[6] + 1 = 3
$$

That means one possible construction is 3 coins total.
The algorithm tries all possible last coins and keeps the best result.

## Initialization

- Fill `dp` with `amount + 1`, which acts like an impossible value.
- Set `dp[0] = 0` because zero coins are needed to make amount `0`.

## Final check

If `dp[amount]` is still larger than `amount`, then no combination worked, so return `-1`.
Otherwise return `dp[amount]`.

## Complexity

Let `n` be the number of coin denominations.

- Time complexity: $O(n \cdot amount)$
  because for each amount from `1` to `amount`, we try every coin.
- Space complexity: $O(amount)$
  because the DP array stores one value for each amount from `0` to `amount`.
