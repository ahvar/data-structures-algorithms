# Gas Station Analysis

## Problem Summary

We are given two arrays:

- `gas[i]`: how much gas is available at station `i`
- `cost[i]`: how much gas it takes to travel from station `i` to station `i + 1`

The stations form a circle, so after the last station we return to the first one.

The goal is to find the index of the station where we can start with an empty tank, travel around the entire circle once, and never let the gas in the tank go below `0`.

If no such starting station exists, we return `-1`.

## Solution Idea

The solution in [gs_answer.py](./gs_answer.py) is a greedy algorithm.

Instead of trying every possible starting station, it makes one pass through the arrays and keeps track of:

- `tank`: the gas currently available while testing the current starting point
- `total`: the total net gas across the whole route
- `start`: the current candidate starting index

It is called greedy because at the moment the current starting station fails, the algorithm immediately makes the locally optimal choice: discard that entire failed range and move `start` forward to the next station. It never goes back to reconsider earlier stations.

## Step-by-Step Logic

### 1. Initialize tracking variables

```python
tank = 0
total = 0
start = 0
```

- `tank` stores how much gas we have while simulating travel from the current candidate start.
- `total` stores the total gas surplus or deficit across all stations.
- `start` stores the station index we are currently testing as the answer.

### 2. Visit each station once

```python
for i in range(len(gas)):
    diff = gas[i] - cost[i]
```

At each station, we compute:

- `diff = gas[i] - cost[i]`

This is the net gain or loss after filling at station `i` and traveling to the next station.

### 3. Update the running tank and total

```python
    tank += diff
    total += diff
```

- `tank += diff` means: if we started from `start`, how much gas would we have after reaching this point?
- `total += diff` means: across the entire route, are we gaining enough gas overall to complete the circuit?

### 4. If the tank becomes negative, the current start fails

```python
    if tank < 0:
        start = i + 1
        tank = 0
```

If `tank < 0`, it means we cannot reach the next station when starting from the current `start`.

So:

- the current candidate start is invalid
- every station between the old `start` and `i` is also invalid
- the next possible candidate is `i + 1`

Why can we skip all those stations?

Because if starting at `start` fails by the time we get to `i`, then any station between `start` and `i` would have even less gas available before reaching the failure point. So none of them can be valid starting positions.

Resetting `tank = 0` means we start a fresh simulation from the new candidate station.

This is the greedy step in the algorithm: once a candidate start fails, we greedily choose the next station as the only worthwhile candidate to try.

### 5. Check whether a solution exists at all

```python
if total < 0:
    return -1
return start
```

This is the final decision:

- If `total < 0`, the total amount of gas is less than the total travel cost, so no solution exists.
- Otherwise, a solution exists, and the greedy scan has already identified the correct starting index in `start`.

## Why This Works

The algorithm relies on two facts:

1. If total gas is less than total cost, completing the circuit is impossible from any station.
2. If the current candidate start fails at station `i`, then none of the stations from the current `start` through `i` can be a valid start.

That second fact is what makes the greedy method efficient. It lets us skip many impossible starting positions at once instead of checking them one by one.

So yes, this algorithm is greedy. Its greedy choice is: as soon as the running tank becomes negative, abandon the current candidate and jump directly to `i + 1`.

## Example Walkthrough

Example:

```python
gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
```

Compute the net differences:

```python
[-2, -2, -2, 3, 3]
```

Walk through them:

- At index `0`, `tank = -2`, so start cannot be `0`. Move start to `1`.
- At index `1`, `tank = -2`, so start cannot be `1`. Move start to `2`.
- At index `2`, `tank = -2`, so start cannot be `2`. Move start to `3`.
- At index `3`, `tank = 3`.
- At index `4`, `tank = 6`.

The total is positive, so a solution exists, and the valid start is index `3`.

## Complexity

### Time Complexity

`O(n)`

We loop through the arrays exactly once.

### Space Complexity

`O(1)`

We only use a constant amount of extra space: `tank`, `total`, and `start`.

## Final Takeaway

This solution is efficient because it avoids testing every station as a starting point.

It uses:

- one pass to determine whether the trip is possible overall
- a greedy reset rule to identify the only valid starting station

That gives us an optimal solution with linear time and constant extra space.