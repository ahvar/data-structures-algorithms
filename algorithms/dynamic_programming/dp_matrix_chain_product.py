from rich import print as rprint
import pprint
from pprint import PrettyPrinter

pp = PrettyPrinter(indent=4)


def make_dp_table(d):
    n = len(d) - 1
    N = [[0] * n for _ in range(n)]
    pp.pprint("starting table: {}".format(N))
    for b in range(1, len(d)):  # from two matrices up to len(d)
        rprint("b: {}".format(b))
        rprint("matrix chain: {}".format(d[b:]))
        for i in range(n - b):  # starting index
            rprint("i (starting index): {} in range {}: ".format(i, n - b))
            j = i + b  # ending index
            rprint("j (ending index): {}".format(j))
            rprint("subproblem matrices: {}".format(d[i:j]))
            N[i][j] = float("inf")
            for k in range(i, j):
                cost = N[i][k + 1] + N[k + 1][j] * d[i] * d[k + 1] * d[j + 1]
                N[i][j] = min(N[i][j], cost)
                rprint("DP Table: {}".format(N))


if __name__ == "__main__":
    d = [5, 15, 10, 20, 25, 30]
    make_dp_table(d)
