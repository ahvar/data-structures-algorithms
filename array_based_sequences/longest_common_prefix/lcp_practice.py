from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]
        for s in strs[1:]:
            i = 0
            while i < len(prefix) and i < len(s) and prefix[i] == s[i]:
                i += 1
            prefix = s[:i]
            if not prefix:
                break
        return prefix


class TestSolution:

    def test_longest(self):
        s = Solution()
        strs = ["flower", "flow", "flight"]
        prefix = s.longestCommonPrefix(strs)
        assert prefix == "fl"
