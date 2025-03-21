def generate_parenthesis(n):
    parens = []
    dp = [[] for _ in range(n)]
    dp[0] = [""]
    for i in range(1, n + 1):
        for left in range(i):
            pass


if __name__ == "__main__":
    n = 3
    generate_parenthesis(n)
