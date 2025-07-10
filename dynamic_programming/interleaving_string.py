"""
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where s and t are divided into
n and m substrings respectively, such that:
"""
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n = len(s1)
        m = len(s2)
        if n + m != len(s3): return False
        dp = [ [False] * (m + 1) for _ in range(n + 1) ]
        dp[0][0] = True
        for i in range(1, n+1): dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
        for i in range(1, m+1): dp[0][i] = dp[0][i-1] and s2[i-1] == s3[i-1]
        for i in range(1,n + 1):
            for j in range(i, m+1):
                dp[i][j] = (
                    (dp[i-1][j] and s1[i-1] == s3[i+j - 1]) or
                    (dp[i][j-1] and s2[j-1] == s3[i+j - 1])
                )
        return dp[n][m]


if __name__ == "__main__":
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    solution = Solution()
    solution.isInterleave(s1,s2,s3)
