from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for s in strs[1:]:
            i = 0
            while i < len(s) and s[i] == prefix[i]:
                i += 1
            prefix = s[:i]
            if prefix == "":
                break
        return prefix


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_longest(self):
        assert (
            self.solution.longestCommonPrefix(strs=["flower", "flow", "flight"]) == "fl"
        )
