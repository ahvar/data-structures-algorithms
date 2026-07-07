# Implementation Guide

Use two pointers plus a dummy node.

## Idea

Because the list is sorted, duplicates appear in one contiguous block. That means once you see the same value twice, you should skip the entire block instead of removing nodes one by one.

## Steps

1. Create a dummy node that points to `head`.
   This makes it easy to remove duplicates even when the first values must be deleted.

2. Keep two pointers:
   - `prev`: last node confirmed to be distinct
   - `curr`: node currently being inspected

3. For each node, check whether it starts a duplicate block.
   If `curr.next` exists and `curr.val == curr.next.val`, then `curr` belongs to a repeated value.

4. Skip the full duplicate block.
   Store the duplicated value, then move `curr` forward until that value disappears.

5. Reconnect the clean list.
   Point `prev.next` to the first node after the duplicate block.

6. If the current node is not duplicated, move both pointers forward normally.

7. Return `dummy.next`.

## Why The Dummy Node Matters

Without a dummy node, removing duplicates at the front of the list needs special-case logic. With it, every removal is handled the same way.

## Complexity

- Time: `O(n)` because each node is visited at most once
- Space: `O(1)` extra space

## Commented Solution

```python
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy node lets us remove duplicates at the head
        dummy = ListNode(0, head)
        prev = dummy
        curr = head

        while curr:
            # If the current value repeats, skip the whole block
            if curr.next and curr.val == curr.next.val:
                duplicate_value = curr.val

                while curr and curr.val == duplicate_value:
                    curr = curr.next

                prev.next = curr
            else:
                # Current node is distinct, so keep it
                prev = curr
                curr = curr.next

        return dummy.next
```
