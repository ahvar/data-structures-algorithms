from collections import defaultdict
from typing import DefaultDict, List, Tuple


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            # Count how many times each lowercase letter appears.
            counts = [0] * 26
            for char in word:
                counts[ord(char) - ord("a")] += 1

            # Use the letter-frequency pattern as the anagram signature.
            groups[tuple(counts)].append(word)

        # Each dictionary value is one anagram group.
        return list(groups.values())
