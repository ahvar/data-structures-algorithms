# What is an Inductive Proof
Inductive proofs are one way to prove an algorithm works. Each inductive proof has two steps:
 - the base case
 - the inductive case

## Base Case
In `quick_sort.py` the base case is arrays of size 0 and 1.

## Inductive Case
We showed that if `quick_sort` works for arrays of size 1, it will work for an array of size 2. And if it works for an array of size 2, it will work for arrays of size 3, and so on. We can then state that `quicksort` will work for arrays of any size. Inductive proofs go hand-in-hand with the general divide & conquer strategy

## References
 - Grokking Algorithms, 2nd ed