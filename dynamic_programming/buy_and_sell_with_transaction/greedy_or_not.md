# Is This a Greedy Approach?

**No, this is a dynamic programming (DP) approach, not greedy.**

## Greedy vs. DP Distinction

| Greedy | Dynamic Programming (This Solution) |
|--------|-------------------------------------|
| Makes locally optimal choice at each step without looking back | Considers all previous subproblem solutions |
| No state tracking across decisions | Maintains state via `hold[]` and `sell[]` arrays |
| Commits to decisions immediately | Defers commitment by tracking both "hold" and "sell" states |

The solution uses **two state transitions** that depend on previous optimal values:
```python
hold[i] = max(hold[i - 1], sell[i - 1] - prices[i - 1])  # best if holding stock
sell[i] = max(sell[i - 1], hold[i - 1] + prices[i - 1] - fee)  # best if not holding
```

This is the hallmark of DP: building optimal solutions from previously computed optimal subproblems.

---

## Why Return `sell[n]`?

`sell[n]` represents the **maximum profit at the end when you don't hold any stock**.

- **`hold[n]`** = max profit while still holding unrealized stock (money tied up in shares)
- **`sell[n]`** = max profit with all positions closed (actual cash in hand)

Since you can't "realize" profit until you sell, and you want maximum **actual profit** at the end, you must return the state where you've sold everything — that's `sell[n]`.

---

## "But We Only Look Back One Index..."

True — we only look back one index. But the values `hold[i-1]` and `sell[i-1]` **already encode all prior optimal decisions**. They're not just "what happened yesterday" — they represent "the best possible profit achievable up to day i-1."

Think of it like Fibonacci:
```python
fib[i] = fib[i-1] + fib[i-2]
```
We only look back 1-2 steps, but `fib[i-1]` contains the cumulative result of all prior computations.

### The Difference

| Aspect | This DP Solution | True Greedy |
|--------|------------------|-------------|
| `hold[i-1]` | Optimal profit across ALL ways to reach "holding" state by day i-1 | Would just track "am I currently holding?" |
| Decision basis | Compare against **accumulated optimal** | Compare against **immediate local** gain |

### Why Only i-1 Is Enough

This problem has the **Markov property**: the optimal decision at day `i` only depends on:
1. What state you're in (holding vs. not holding)
2. The optimal profit to reach that state

You don't need to know *which specific days* you bought/sold before — just the best profit achievable in each state. That's captured in `hold[i-1]` and `sell[i-1]`.

### What a Greedy Approach Would Look Like

A greedy approach would make immediate commit decisions like:
```python
if prices[i] - prices[i-1] > fee:
    profit += prices[i] - prices[i-1] - fee  # commit immediately
```

This fails because it doesn't account for "maybe I should hold longer for a bigger profit later" — which the DP handles by carrying forward both possibilities.
