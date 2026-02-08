class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        left = 0
        seen = set()
        maxx = 0
        for right in range(n):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            maxx = max(maxx, right - left + 1)
        return maxx
