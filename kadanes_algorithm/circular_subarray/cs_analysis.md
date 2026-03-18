# Circular Subarray Maximum Sum - Analysis

## Problem Statement

Given a circular integer array `nums` of length `n`, return the maximum possible sum of a non-empty subarray. A circular array means the end of the array connects to the beginning. Each element can be included at most once per subarray.

## Solution Logic

### Key Insight

For a circular array, there are exactly **two possible cases** for the maximum subarray:

1. **Non-wrapping case**: The maximum subarray lies within the array without wrapping around
2. **Wrapping case**: The maximum subarray wraps around the circular boundary

Mathematically, if the maximum subarray wraps, it represents the "outside" of a contiguous minimum subarray. Therefore:

```
max_circular_subarray = total_sum - min_subarray
```

### Step-by-Step Logic

#### Step 1: Find Maximum Subarray (Non-wrapping)
Apply **Kadane's Algorithm** to find the maximum subarray sum without considering circularity:

```python
def kadane(arr):
    max_sum = arr[0]
    current_sum = arr[0]
    
    for i in range(1, len(arr)):
        # Either extend the current subarray or start fresh
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)
    
    return max_sum
```

**Logic**: At each position, decide whether to:
- Add the current element to the existing subarray
- Start a new subarray from the current element

Track the maximum sum seen so far.

#### Step 2: Find Minimum Subarray
To find the wrapping maximum, we need the minimum subarray. Use Kadane's algorithm on negated values:

```python
# Convert problem: find min = find max of negated values
min_kadane = kadane([-num for num in nums])
min_subarray = -min_kadane
```

#### Step 3: Calculate Circular Maximum
The maximum subarray that wraps equals the total sum minus the minimum subarray:

```python
total_sum = sum(nums)
max_circular = total_sum - min_subarray
```

#### Step 4: Handle Edge Case
If all elements are negative:
- `min_subarray = total_sum` (we'd exclude everything)
- `max_circular = 0`, which is invalid
- Return the single least-negative element instead (the `max_kadane` result)

```python
if max_circular == 0:
    return max_kadane
```

#### Step 5: Return Result
Return the maximum of both cases:

```python
return max(max_kadane, max_circular)
```

## Example Walkthrough

### Example 1: `nums = [1, -2, 3, -2]`

- **Total sum**: 1 - 2 + 3 - 2 = 0

**Case 1 - Non-wrapping (Kadane's):**
- Position 0: current = 1, max = 1
- Position 1: current = max(-2, 1-2) = -1, max = 1
- Position 2: current = max(3, -1+3) = 3, max = 3
- Position 3: current = max(-2, 3-2) = 1, max = 3
- **Result**: 3

**Case 2 - Wrapping:**
- Negate array: [-1, 2, -3, 2]
- Kadane result: max subarray = 2, so min_subarray = -2
- max_circular = 0 - (-2) = 2

**Final answer**: max(3, 2) = **3** ✓

### Example 2: `nums = [5, -3, 5]`

- **Total sum**: 5 - 3 + 5 = 7

**Case 1 - Non-wrapping:**
- Position 0: current = 5, max = 5
- Position 1: current = max(-3, 5-3) = 2, max = 5
- Position 2: current = max(5, 2+5) = 7, max = 7
- **Result**: 7

**Case 2 - Wrapping:**
- Negate array: [-5, 3, -5]
- Kadane result: max of negated = 3, so min_subarray = -3
- max_circular = 7 - (-3) = 10

**Final answer**: max(7, 10) = **10** ✓

The subarray [5, 5] wraps around by excluding the middle element -3.

### Example 3: `nums = [-3, -2, -3]`

- **Total sum**: -8

**Case 1 - Non-wrapping:**
- Kadane result: -2 (single element)

**Case 2 - Wrapping:**
- min_subarray = -8 (entire array)
- max_circular = -8 - (-8) = 0

**Edge case**: max_circular = 0, so return max_kadane = **-2** ✓

All negative numbers, so the best we can do is take the single least-negative element.

## Complexity Analysis

### Time Complexity: **O(n)**

- **Kadane's algorithm for max**: O(n) - single pass through array
- **Kadane's algorithm for min**: O(n) - single pass through negated array
- **Computing total sum**: O(n) - single pass
- **Array negation**: O(n) - single pass
- **Overall**: O(n) + O(n) + O(n) + O(n) = **O(n)**

### Space Complexity: **O(n)**

- **Negated array creation**: O(n) - stores `-nums` as a new list
- **Other variables**: O(1) - scalars only
- **Overall**: **O(n)**

#### Space Optimization Note
If space is critical, you can compute the minimum subarray directly without creating a negated array by modifying Kadane's slightly. This would reduce space to **O(1)**.

## Key Takeaways

1. **Circular arrays** require considering two cases: wrapping and non-wrapping
2. **Wrapping max = Total sum - Minimum subarray** is the key mathematical insight
3. **Kadane's algorithm** is fundamental and applicable to both max and min subarray problems
4. **Edge case handling** is crucial when all elements are negative
5. The solution elegantly reduces a complex problem to two applications of a simpler algorithm

## Related Problems

- Maximum Subarray (Kadane's Algorithm)
- Maximum Product Subarray
- Minimum Subarray Sum
- Longest Subarray with Sum K
