"""
R-13.2
What is the longest (proper) prefix of the string S that is also
a suffix of this string
"""


def longest_prefix(stringa):
    longest = ""
    sfx = [stringa[i:] for i in range(1, len(stringa))]
    pfx_in_sfx = [stringa[0:i] for i in range(len(stringa) + 1) if stringa[0:i] in sfx]
    for p in pfx_in_sfx:
        if len(p) > len(longest):
            longest = p
    return longest


if __name__ == "__main__":
    stringa = "cgtacgttcgtacg"
    print(longest_prefix(stringa))
