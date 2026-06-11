# Complexity Analysis

The current implementation uses two nested loops and checks pairs one by one until it finds a sum equal to the target.

- Time complexity: O(n^2) in the worst case. For each element, the algorithm may compare it with most of the remaining elements. If no valid pair exists, it ends up examining essentially all possible pairs.
- Space complexity: O(1). The algorithm does not allocate any extra data structure that grows with the input size; it only uses a few loop variables.

Because the input array is already sorted, there is a more efficient approach. A two-pointer solution can start with one pointer at the left end and one at the right end, then move inward depending on whether the current sum is too small or too large. That reduces the time complexity to O(n) while keeping the space complexity at O(1).