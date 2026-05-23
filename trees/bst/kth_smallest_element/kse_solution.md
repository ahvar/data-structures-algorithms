# Kth Smallest Element in a BST

## Problem

Given the root of a binary search tree and an integer `k`, return the `k`th smallest value (1-indexed) among all node values.

## Core Idea

This solution uses an inorder traversal of a BST.

A binary search tree has this property:

- all values in the left subtree are smaller than the current node
- all values in the right subtree are larger than the current node

Because of that, an inorder traversal visits nodes in ascending sorted order:

1. traverse left
2. visit current node
3. traverse right

So if we walk the tree inorder and count visited nodes, the moment we visit the `k`th node, we have found the `k`th smallest value.

## Code

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.ans = None

        def inorder(node):
            if not node or self.ans is not None:
                return

            inorder(node.left)
            self.k -= 1
            if self.k == 0:
                self.ans = node.val
            inorder(node.right)

        inorder(root)
        return self.ans
```

## Why This Works

The key invariant is:

> During inorder traversal of a BST, nodes are visited from smallest to largest.

That means every time we process a node, we are seeing the next smallest value in sorted order.

### Step by Step

At the start:

- `self.k` stores how many more nodes we need to skip before reaching the answer
- `self.ans` is `None` because we have not found the answer yet

Inside `inorder(node)`:

1. If `node` is `None`, stop.
2. If `self.ans` is already set, stop early because the answer has been found.
3. Traverse the left subtree first.
4. Visit the current node:
   - decrement `self.k`
   - if `self.k == 0`, this node is the `k`th smallest
5. Traverse the right subtree.

## Why `self.k -= 1` Identifies the Answer

Since inorder traversal visits nodes in sorted order, each visited node corresponds to:

- 1st smallest
- 2nd smallest
- 3rd smallest
- and so on

So when we decrement `self.k`, we are counting down through that sorted order.

When `self.k` becomes `0`, the current node is exactly the `k`th smallest.

## Example

Suppose the BST contains:

`2, 3, 4, 5, 6, 7, 8`

and `k = 3`.

Inorder traversal visits:

`2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8`

Tracking `self.k`:

- visit `2`, `k` becomes `2`
- visit `3`, `k` becomes `1`
- visit `4`, `k` becomes `0`

So `4` is the 3rd smallest value.

## Why the Early Return Is Safe

This line stops unnecessary work:

```python
if not node or self.ans is not None:
    return
```

Once `self.ans` is found, there is no need to keep traversing. Since inorder traversal is already visiting values in sorted order, all later nodes would be larger and cannot change the answer.

## Why Use `self.k` and `self.ans`

The nested `inorder` function needs to update shared state across recursive calls.

- `self.k` lets the recursion keep track of how many nodes remain before the answer
- `self.ans` stores the answer once found and lets recursion stop early

## Complexity

- **Time:** `O(n)` in the worst case
- **Space:** `O(h)` for the recursion stack, where `h` is the height of the tree

In practice, it may finish earlier than visiting all nodes because it stops once the answer is found.

## Summary

This works because:

1. inorder traversal of a BST produces values in sorted order
2. the code counts visited nodes in that sorted order
3. when the count reaches `k`, the current node is the `k`th smallest