"""
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

 

Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
"""
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        dp = [0 for i in range(len(s))]
        for i in range(len(s)):
            r = k
            if i + k <= len(s) - 1:
                sub_end = i + k
            else:
                sub_end = len(s)
            for j in range(i, sub_end):
                if s[j] in vowels:
                    r -= 1
            if r == 0:
                return k
            elif i == 0:
                dp[i] = k - r
            else:
                dp[i] = max(dp[i-1], k-r)
        return dp[-1]
 

if __name__ == "__main__":
    s = "abciiidef"
    k = 3
    solution = Solution()
    print(solution.maxVowels(s, k))