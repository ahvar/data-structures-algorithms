# Two Strings Close Guide

## Implementation Steps

1. Compare the sets of characters in both strings.
2. If the sets differ, return `False` immediately because operation 2 can only swap identities of characters that already exist.
3. Use `Counter` to count the frequency of each character in `word1`.
4. Use `Counter` to count the frequency of each character in `word2`.
5. Extract the frequency counts from both dictionaries.
6. Sort both frequency lists.
7. Compare the sorted frequency lists.
8. Return `True` if they match, otherwise return `False`.

## Why This Works

Swapping characters can rearrange positions freely, so order does not matter.
The character set must match because you cannot introduce a brand-new character.
The frequency counts must also match as a multiset, because operation 2 lets you swap which character owns a given count.

## Coded, Commented Solution

```python
from collections import Counter


class Solution:

    def closeStrings(self, word1: str, word2: str) -> bool:
        # The strings must use the same set of characters.
        # If one string has a character the other does not, it can never be created.
        if set(word1) != set(word2):
            return False

        # Count how many times each character appears in each string.
        word1_count = Counter(word1)
        word2_count = Counter(word2)

        # Operation 2 allows characters to exchange identities,
        # so only the multiset of frequencies has to match.
        vals1 = sorted(word1_count.values())
        vals2 = sorted(word2_count.values())

        # If the sorted frequency lists match, the strings are close.
        return vals1 == vals2
```

## Complexity Analysis

- Time: `O(n + k log k)` where `n` is the length of the strings and `k` is the number of distinct characters.
- Building the two sets takes linear time in the size of the inputs.
- Building the two `Counter` objects also takes linear time because each character is processed once.
- Sorting the frequency lists costs `O(k log k)` for each string, which is why the total time is written as `O(n + k log k)`.
- If the alphabet is fixed and small, such as lowercase English letters, then `k` is bounded by a constant and the runtime behaves like `O(n)` in practice.
- Space: `O(k)` because the sets, counters, and frequency lists only store information for distinct characters.