class Solution:
    def min_window(self, s1: str, s2: str) -> str:
        if not s2 or len(s2) > len(s1):
            return ""
        m = len(s1)
        n = len(s2)
        dp = [-1] * n
        best_window = ""
        best_length = float("inf")
        for i in range(m):

            for j in range(m - 1, 1, -1):
                if s1[i] == s2[j]:
                    if j == 0:
                        dp[j] = i
                    else:
                        dp[j] = dp[j - 1]

            if dp[n - 1] != -1:
                start = dp[n - 1]
                window_length = i - start + 1

                if window_length < best_length:
                    best_length = window_length
                    best_window = s1[start : i + 1]

        return best_window
