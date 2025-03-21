from rich import print as rprint
import pprint
from pprint import PrettyPrinter

pp = PrettyPrinter(indent=4)


def make_dp_table(d):
    n = len(d) - 1
    N = [[0] * n for n in range(n)]
    for b in range(n):
        for i in range(n - b):
            j = i + b
            for k in range(i, j):
                N[i][j] = min(N[i][k] + N[k + 1][j] + d[k] * d[k + 1])


if __name__ == "__main__":
    d = [10, 35, 15, 5, 50, 25, 10]
    make_dp_table(d)
