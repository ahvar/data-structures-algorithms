# Minimum Absolute Difference in BST - Analysis

## The Critical BST Property

In a BST, an **in-order traversal** (left → node → right) visits nodes in **sorted ascending order**. This is the most important property to understand for this solution.

### Example

For a BST like this:
```
      4
     / \
    2   6
   / \
  1   3
```

An in-order traversal gives you: `1 → 2 → 3 → 4 → 6` (sorted!)

## Why This Matters for Minimum Absolute Difference

Since in-order traversal produces a sorted sequence:
- The minimum difference between ANY two nodes must occur between **consecutive nodes** in this sorted sequence
- You never need to compare non-adjacent values (e.g., comparing 1 and 6 when 2, 3, 4 exist between them won't give you a minimum)

So instead of comparing all pairs of nodes (O(n²)), you only need to:
1. Do an in-order traversal
2. Compare each node with the previous node
3. Track the minimum difference found

This reduces the problem to O(n) time with O(h) space (recursion stack).

## Common Implementation Issues

When implementing this solution, watch out for:

1. **Initialize `min_diff` correctly**: Use `float("inf")` not `float("-inf")` - you want to find the minimum, so start with infinity
2. **Variable scope**: When using nested functions, `prev_val` and `min_diff` need to be declared as `nonlocal` inside the `inorder` function to modify the outer scope variables

## Why BST Structure Matters

The logic is sound for BSTs specifically because it leverages the sorted property of in-order traversal. This approach wouldn't work as efficiently on a regular binary tree where in-order traversal doesn't guarantee sorted order.

## Time and Space Complexity

- **Time**: O(n) - visit each node once
- **Space**: O(h) - recursion stack depth, where h is the height of the tree
