def longest_common_subsequence(str1, str2):
    n, m = len(str1), len(str2)
    table = [[0] * (m + 1) for k in range(n + 1)]
    for j in range(n):
        for k in range(m):
            if str1[j] == str2[k]:
                table[j + 1][k + 1] = table[j][k] + 1
            else:
                table[j + 1][k + 1] = max(table[j][k + 1], table[j + 1][k])
    return table


def solution(str1, str2, table):
    solution = []
    j, k = len(str1), len(str2)
    while table[j][k] > 0:
        if str1[j - 1] == str2[k - 1]:
            solution.append(str1[j - 1])
            j -= 1
            k -= 1
        elif table[j - 1][k] >= table[j][k - 1]:
            j -= 1
        else:
            k -= 1
    return "".join(reversed(solution))
