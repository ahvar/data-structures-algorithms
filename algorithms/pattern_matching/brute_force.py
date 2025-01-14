"""
Find all indicies at which a pattern substring begins

find()
index()
count()
partition()
split()
replace()
"""

text = "abadbabdbabcdbdaccdadcdba"
pattern = "ab"


def find_brute(text, pattern):
    n, m = len(text), len(pattern)
    for i in range(n - m + 1):  # try every potential starting index
        k = 0
        while k < m and text[i + k] == text[k]:  # the kth char of pattern matches
            k += 1
        if k == m:
            return i
    return -1


print(find_brute(text, pattern))
