def longest_common_subsequence(text1, text2):
    if not text1 or not text2:
        return 0
    n, m = len(text1), len(text2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n):
        for j in range(1, m):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1], [j])
    return dp[n][m]


def lcs_solution(X, Y, L):
    pass


X = "GTTCCTAATA"
Y = "CGATAATTGAGA"

L = longest_common_subsequence(X, Y)
lcs = lcs_solution(X, Y, L)
