from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]
        for s in strs:
            i = 0
            while i < len(s) and i < len(prefix) and s[i] == prefix[i]:
                i += 1
            prefix = s[:i]
            if not prefix:
                break
        return prefix


class TestSolution:

    def setup_method(self):
        self.solution = Solution()

    def test_longest(self):
        expected = "fl"
        strs = ["dog", "flower", "flow", "flight"]
        assert self.solution.longestCommonPrefix(strs) == expected
