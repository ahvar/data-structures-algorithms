# Vowels In Substring Guide

## Implementation Steps

1. Create a set containing the five lowercase vowels so vowel checks are fast.
2. Build a prefix-sum array with one extra slot at the front to represent zero characters processed.
3. Walk through the string from left to right and record, at each position, how many vowels have appeared so far.
4. For each query, use the prefix totals at the right boundary and the left boundary to get the vowel count in that substring.
5. Append each query result to an output list in the same order as the queries.
6. Return the completed list.

## Key Idea

Precompute vowel counts once, then answer each query by subtraction instead of recounting characters inside every substring.