# Apple Harvest

Bobby has an orchard of apple trees, and each tree has a certain number of apples on it.

He wants to collect all the apples by the end of the day by harvesting at a fixed rate of apples per hour.

He can only harvest apples from one tree per hour. If he finishes collecting apples from a tree before the hour is up, he must wait until the next hour before moving to the next tree.

## Example of the Hourly Rule

- If a tree has `3` apples and Bobby harvests `1` apple per hour, it takes `3` hours to finish that tree.
- If a tree has `3` apples and Bobby harvests `2` apples per hour, it takes `2` hours to finish that tree.
  He still waits for the hour to finish before moving on.

## Task

Write a function that determines the slowest harvest rate Bobby can use and still finish all the apples in at most `h` hours.

The input consists of:

- An array of integers where each value represents the number of apples on a tree.
- An integer `h` representing the total number of hours available.

## Example 1

**Input**

```text
apples = [3, 6, 7], h = 8
```

**Output**

```text
3
```

**Explanation**

- `1` apple per hour: `3 + 6 + 7 = 16` hours, which is more than `8`. Not valid.
- `2` apples per hour: `2 + 3 + 4 = 9` hours, which is more than `8`. Not valid.
- `3` apples per hour: `1 + 2 + 3 = 6` hours, which is within `8`. Valid.
- `4` apples per hour: `1 + 2 + 2 = 5` hours. Valid.
- `5` apples per hour: `1 + 2 + 2 = 5` hours. Valid.

Therefore, the minimum valid harvest rate is `3` apples per hour.

## Code

```python
from typing import List


class Solution:
  def minHarvestRate(self, apples: List[int], h: int) -> int:
    if not apples:
      return 0
    if h < len(apples):
      return -1

    left = 1
    right = max(apples)

    def hours_needed(rate):
      total = 0
      for apples_on_tree in apples:
        # Round up because finishing early still uses the full hour.
        total += (apples_on_tree + rate - 1) // rate
      return total

    while left < right:
      mid = (left + right) // 2
      needed = hours_needed(mid)

      # If this rate works, try a slower valid rate.
      if needed <= h:
        right = mid
      else:
        # If it does not work, Bobby must harvest faster.
        left = mid + 1

    return left
```
