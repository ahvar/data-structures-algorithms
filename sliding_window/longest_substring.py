"""
Given a string s, find the length of the longest substring without
duplicate characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a
subsequence and not a substring.
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        if len(s) == 1: return 1
        maxx = 1
        for left in range(len(s)):
            right = left + 1
            while right < len(s):
                curr = s[right]
                if curr in s[left:right]: break
                right += 1
            if right - left > maxx: maxx = right - left
        return maxx


if __name__ == "__main__":
    s = "abcabcbb"
    s1 = "bbbbb"
    s2 = "pwwkew"
    solution = Solution()
    print(solution.lengthOfLongestSubstring(s2))
    

