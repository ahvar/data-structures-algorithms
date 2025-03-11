from rich import print as rprint

X = "ABCBDAB"
Y = "BDCAB"
n, m = len(X), len(Y)
N = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(m):
        if X[i - 1] == Y[j - 1]:
            N[i][j] += (
                1 + N[i - 1][j - 1]
            )  # we extend LCS by 1, using the value from the previous diagonal entry
        elif X[i - 1] != Y[j - 1]:
            N[i][j] = max(
                N[i - 1][j], N[i][j - 1]
            )  # X[i-1] or Y[j-1] is in the LCS, take max

rprint(N)
