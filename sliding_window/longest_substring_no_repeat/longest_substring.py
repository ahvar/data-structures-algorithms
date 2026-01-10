class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == None or len(s) == 0:
            return 0
        seen = set()
        left = 0
        maxx = 0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            maxx = max(maxx, right - left + 1)
        return maxx


if __name__ == "__main__":
    s = "abcabcbb"
    s1 = "bbbbb"
    s2 = "pwwkew"
    solution = Solution()
    print(solution.lengthOfLongestSubstring(s2))
