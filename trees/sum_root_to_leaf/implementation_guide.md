# Sum Root to Leaf Implementation Guide

## Goal

Traverse every root-to-leaf path, treat each path as a number, and return the total sum of all such numbers.

## Core Idea

Use depth-first search to build each number as you move down the tree.

At each node, shift the current number one digit to the left by multiplying by `10`, then add the node's digit.

## Logical Operations

### 1. Start DFS from the root

Begin the traversal with a running value of `0`.

### 2. Stop on empty nodes

If the current node is `None`, return `0` because it contributes nothing to the final sum.

### 3. Update the current path value

For each visited node, compute:

```python
current = current * 10 + node.val
```

This appends the current digit to the number formed so far.

Example:

- Previous value: `12`
- Current node value: `3`
- New value: `123`

### 4. Check whether the node is a leaf

If the node has no left child and no right child, the current path is complete.
Return the built number.

### 5. Recurse into both children

If the node is not a leaf, continue the DFS on the left and right children.
Add the returned sums together.

## Why This Works

Each recursive call carries the number represented by the path from the root to the current node. When a leaf is reached, that number is complete and should be included in the total. Summing all leaf results gives the answer.

## Complexity

- Time: `O(n)` because each node is visited once.
- Extra space: `O(h)` for the recursion stack, where `h` is the height of the tree.

## Commented Solution

```python
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode], current: int) -> int:
            # An empty node contributes nothing.
            if not node:
                return 0

            # Append this node's digit to the current path value.
            current = current * 10 + node.val

            # If this is a leaf, return the completed number.
            if not node.left and not node.right:
                return current

            # Otherwise, sum the values from both subtrees.
            return dfs(node.left, current) + dfs(node.right, current)

        return dfs(root, 0)
```