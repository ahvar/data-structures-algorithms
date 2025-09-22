def longest_common_subsequence(X, Y):
    """Return table such that L[j][k] is length LCS for X[0:j] and Y[0:k]"""
    n, m = len(X), len(Y)
    dp = [[0] * m + 1 for _ in range(len(n) + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if X[i-1] == Y[j-1]:
                dp[i][j] += dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    return dp[n][m]







def lcs_solution(X, Y, L):
    pass


X = "GTTCCTAATA"
Y = "CGATAATTGAGA"

L = longest_common_subsequence(X, Y)
lcs = lcs_solution(X, Y, L)
