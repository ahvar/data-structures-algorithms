# What is an Inductive Proof
Inductive proofs are one way to prove an algorithm works. Each inductive proof has two steps:
 - the base case
 - the inductive case

## Base Case
In `quick_sort.py` the base case is arrays of size 0 and 1.

## Inductive Case
We showed that if `quick_sort` works for arrays of size 1, it will work for an array of size 2. And if it works for an array of size 2, it will work for arrays of size 3, and so on. We can then state that `quicksort` will work for arrays of any size. Inductive proofs go hand-in-hand with the general divide & conquer strategy

## Steps in the Quicksort Algorithm
1. Check for the "base case"
2. Calculate and assign the pivot index and the pivot value
3. Compute the subarrays of lesser, greater, and equivalent values
4. Recursively call `quick_sort` on the subarrays of lesser and greater values
5. Concatenate and return sorted subarrays

## Time Complexity
 - Best: `O(n log n)`
 - Average: `O(n log n)`
 - Worse: `O(n^2)`

## References
 - Grokking Algorithms, 2nd ed