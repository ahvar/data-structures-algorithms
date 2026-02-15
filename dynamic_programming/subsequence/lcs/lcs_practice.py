def longest_common_subsequence(text1, text2):
    n, m = len(text1), len(text2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[n][m]


def lcs_solution(X, Y, L):
    pass


X = "GTTCCTAATA"
Y = "CGATAATTGAGA"

L = longest_common_subsequence(X, Y)
lcs = lcs_solution(X, Y, L)
