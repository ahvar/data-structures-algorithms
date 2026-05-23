# H-Index - Logic and Complexity

## Core Idea

The h-index is the largest value `h` such that the researcher has at least `h` papers with at least `h` citations each.

This solution sorts the citation counts in descending order so the most cited papers come first. Then it scans from left to right and checks how many papers seen so far still satisfy the h-index condition.

## Why the Sorted Order Helps

After sorting in descending order:

```python
c = sorted(citations, reverse=True)
```

the paper at index `i` is the `(i + 1)`th most-cited paper.

If `c[i] >= i + 1`, then there are at least `i + 1` papers with at least `i + 1` citations, so `i + 1` is a valid h-index candidate.

If `c[i] < i + 1`, then the current paper does not have enough citations to support a larger h-index, and no later paper can fix that because the array is sorted in descending order. So the scan can stop.

## Step-by-Step Logic

```python
c = sorted(citations, reverse=True)
hindex = 0
for i, cite in enumerate(c):
    if cite >= i + 1:
        hindex = i + 1
    else:
        break
return hindex
```

What each part does:

1. Sort citations from largest to smallest.
2. Iterate through the sorted array.
3. At each index `i`, check whether the current citation count is at least `i + 1`.
4. If it is, update `hindex` to `i + 1`.
5. If it is not, stop, because all remaining citation counts are smaller or equal.
6. Return the largest valid value found.

## Example

For:

```python
citations = [3, 0, 6, 1, 5]
```

sort descending:

```python
[6, 5, 3, 1, 0]
```

scan:

- `i = 0`, `cite = 6` -> `6 >= 1`, so `hindex = 1`
- `i = 1`, `cite = 5` -> `5 >= 2`, so `hindex = 2`
- `i = 2`, `cite = 3` -> `3 >= 3`, so `hindex = 3`
- `i = 3`, `cite = 1` -> `1 < 4`, stop

Final answer:

```python
3
```

## Time Complexity

```text
O(n log n)
```

where `n` is the number of papers.

Reason:

- Sorting takes `O(n log n)`.
- The single pass through the sorted list takes `O(n)`.
- The sorting step dominates.

## Space Complexity

```text
O(n)
```

Reason:

- `sorted(...)` creates a new list.
- The extra list stores `n` citation values.

If the array were sorted in place instead, the auxiliary space discussion would depend on the language and sorting implementation.

## Why This Works

The descending order guarantees that once `cite < i + 1`, every later citation count will also be less than `i + 1`.

So the largest valid `h` is exactly the last index where:

```python
cite >= i + 1
```

That is why this simple scan correctly returns the h-index.
