string1 = "ado"
string2 = "abcdo"


def lcs(i, j):
    if i == len(string1) or j == len(string2):
        return 0
    elif string1[i] == string2[j]:
        return 1 + lcs(i + 1, j + 1)
    else:
        return max(lcs(i + 1, j), lcs(i, j + 1))


if __name__ == "__main__":
    i = j = 0
    print(lcs(i, j))
