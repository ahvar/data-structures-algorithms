# K Smallest Pairs

## Reference Solution

```python
from typing import List
import heapq


class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        # If either array is empty, or k is not positive, there are no pairs to return.
        if not nums1 or not nums2 or k <= 0:
            return []

        # Store the final answer as pairs of values, not indices.
        result = []

        # Each heap entry is: (pair_sum, index_in_nums1, index_in_nums2).
        # Python's heapq is a min-heap, so the smallest sum stays on top.
        heap = []

        # Seed the heap with the first pair from each useful row.
        # Row i starts at (nums1[i], nums2[0]).
        # We only need up to k rows because we will return at most k pairs.
        for i in range(min(k, len(nums1))):
            heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))

        # Repeatedly extract the smallest available pair.
        while heap and len(result) < k:
            # Remove the current smallest-sum pair.
            _, i, j = heapq.heappop(heap)

            # Add the actual values to the answer.
            result.append([nums1[i], nums2[j]])

            # Move one step to the right in the same row.
            # If (i, j) was used, then (i, j + 1) is the next candidate from that row.
            if j + 1 < len(nums2):
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))

        return result
```

## Primary Data Structures And Logic

The main data structure is a min-heap. Each heap entry stores three values: the pair sum, the index in `nums1`, and the index in `nums2`. The sum lets the heap order candidates correctly. The indices let the algorithm recover the actual pair values and generate the next candidate.

The key logic is to treat the pairs like a sorted grid. Each row corresponds to a fixed value from `nums1`, and each column corresponds to a value from `nums2`. Since both arrays are sorted, the smallest pair in any row is always the first column. That means the heap only needs to start with `(i, 0)` for each useful row.

After removing the smallest pair `(i, j)`, the only new candidate that row can contribute is `(i, j + 1)`. There is no need to insert every pair ahead of time. This is what keeps the algorithm efficient: the heap always stores only the next smallest unseen candidate from each active row.

## Complexity

The heap holds at most `min(k, len(nums1))` entries at once, because only one active candidate per row is stored.

The algorithm performs at most `k` heap removals, and each removal may be followed by one insertion. Each heap operation costs `O(log(min(k, len(nums1))))`.

So the total complexity is:

- Time: `O(k log(min(k, len(nums1))))`
- Space: `O(min(k, len(nums1)))`