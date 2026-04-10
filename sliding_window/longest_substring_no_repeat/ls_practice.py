class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        left = 0
        seen = set()
        n = len(s)
        maxx = 0
        for right in range(n):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            maxx = max(maxx, right - left + 1)
        return maxx


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_length(self):
        assert self.solution.lengthOfLongestSubstring(s="abcabcbb") == 3
