# Why This Is Not O(log n)

## Short Answer

This solution is **O(n)** time, not **O(log n)**, because it performs an **in-order traversal of the entire tree**.

A BST only gives you **O(log n)** behavior when an operation follows **one path from the root downward** in a balanced tree, such as search, insert, or delete. This algorithm does not do that. It visits every node.

## What the Code Actually Does

The recursive helper runs this pattern at every node:

1. Traverse the left subtree
2. Process the current node
3. Traverse the right subtree

That means the function touches all nodes in sorted order.

```python
def inorder(node):
    if not node:
        return

    inorder(node.left)

    if self.prev_val is not None:
        self.min_diff = min(self.min_diff, node.val - self.prev_val)
    self.prev_val = node.val

    inorder(node.right)
```

If the tree has `n` nodes, then `inorder` visits each node once, so the total time is `O(n)`.

## Why the BST Property Still Helps

The BST property matters because an in-order traversal produces values in sorted order.

For example, this BST:

```text
    4
   / \
  2   6
 / \
1   3
```

produces this sequence:

```text
1, 2, 3, 4, 6
```

Once the values are sorted, the minimum absolute difference must occur between **adjacent values** in that order.

So the BST helps reduce the problem from comparing all pairs (`O(n^2)`) to comparing only consecutive values during one traversal (`O(n)`).

## Why It Cannot Be O(log n)

To get the correct answer, the algorithm must confirm the minimum difference across the whole sorted sequence. That requires seeing every node.

Even in a balanced BST, you cannot stop after exploring one root-to-leaf path, because the smallest difference might be somewhere else in the tree.

So:

- Search in a balanced BST: `O(log n)`
- Full in-order traversal of a BST: `O(n)`
- This problem's solution: `O(n)`

## Space Complexity

The recursion stack uses space proportional to the height of the tree.

- Balanced BST: `O(log n)` space
- Skewed BST: `O(n)` space

So the full complexity is:

- **Time:** `O(n)`
- **Space:** `O(h)`

where `h` is the tree height.

## Implementation Note

In the current practice file, this line should compare against the current minimum:

```python
self.min_diff = min(self.min_diff, node.val - self.prev_val)
```

not:

```python
self.min_diff = min(self.prev_val, node.val - self.prev_val)
```

Using `self.prev_val` there mixes a node value with a difference, which gives the wrong result.
