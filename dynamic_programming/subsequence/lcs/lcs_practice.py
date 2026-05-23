def longest_common_subsequence(text1, text2):
    m, n = len(text1), len(text2)
    board = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                board[i][j] = board[i - 1][j - 1] + 1
            else:
                board[i][j] = max(board[i - 1][j], board[i][j - 1])
    return board[m][n]


def lcs_solution(X, Y, L):
    pass


X = "GTTCCTAATA"
Y = "CGATAATTGAGA"

L = longest_common_subsequence(X, Y)
lcs = lcs_solution(X, Y, L)
