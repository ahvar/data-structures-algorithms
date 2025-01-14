"""
For alignment of the pattern, if we find several matching characters but then detect a mismatch,
we ignore all the information gained by the successful comparisons after restarting with the
next incremental placement

the main idea of KMP is to precompute self-overlaps between portions of the pattern so
that when a mismatch occurs at one location, we know the max amount to shift the pattern
before continuing search
"""


def compute_kmp_fail(pattern):
    pattern_length = len(pattern)
    fail = [0] * pattern_length
    j = 1
    k = 0
    while j < pattern_length:
        if pattern[j] == pattern[k]:
            fail[j] = k + 1
            j += 1
            k += 1
        elif k > 0:
            k = fail[k - 1]
        else:
            j += 1
    return fail


def find_kmp(text, pattern):
    text_length, pattern_length = len(text), len(pattern)
    if pattern_length == 0:
        return 0
    fail = compute_kmp_fail(pattern)
    j = 0
    k = 0
    while j < text_length:
        if text[j] == pattern[k]:
            if k == pattern_length - 1:
                return j - pattern_length + 1
            j += 1
            k += 1
        elif k > 0:
            k = fail[k - 1]
        else:
            j += 1
    return -1
