def is_subsequence(str1: str, str2: str) -> bool:
    i, j = 0
    while i < len(str1) and j < len(str2):
        if str2[j] == str1[i]:
            j += 1
            continue
        i += 1
    if j == len(str2):
        return True
    return False