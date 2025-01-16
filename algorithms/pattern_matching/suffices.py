"""
R-13.1
List the prefixes of string P = "aaabbaaa" that are also suffixes of P.
"""


def prefixes_and_suffixes(s):
    prefixes = set([s[0:i] for i in range(1, len(s) + 1)])
    print(prefixes)
    suffixes = set([s[i:] for i in range(1, len(s))])
    print(suffixes)
    return prefixes.intersection(suffixes)


s = "aaabbaaa"
print(prefixes_and_suffixes(s))
