class Solution:
    def min_window(self, s1: str, s2: str) -> str:
        m, n = len(s1), len(s2)
        dp = [-1] * n
        result = ""
        min_len = float("inf")

        for i in range(m):
            for j in range(n - 1, -1, -1):
                if s1[i] == s2[j]:
                    if j == 0:
                        dp[j] = i
                    else:
                        dp[j] = dp[j - 1]

            if dp[n - 1] != -1:
                start = dp[n - 1]
                length = i - start + 1

                if length < min_len:
                    min_len = length
                    result = s1[start : i + 1]

        return result
