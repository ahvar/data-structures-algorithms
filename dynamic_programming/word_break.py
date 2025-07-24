"""
Given a string s and a dictionary of strings wordDict, return true if s can
be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the
segmentation.

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
"""

from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [ False for _ in range(len(s) + 1)]
        dp[0] = True
        words = set(wordDict)
        for i in range(1,len(s) + 1):
            for j in range(i):
                if dp[j] == True and s[j:i] in wordDict:
                    dp[i] = True
        return dp[-1]


if __name__ == "__main__":
    solution = Solution()
