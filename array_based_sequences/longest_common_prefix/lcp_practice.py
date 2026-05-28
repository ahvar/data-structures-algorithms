from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for s in strs[1:]:
            i = 0
            while i < len(s) and i < len(prefix) and s[i] == prefix[i]:
                i += 1
            prefix = s[:i]
            if not prefix:
                break
        return prefix
