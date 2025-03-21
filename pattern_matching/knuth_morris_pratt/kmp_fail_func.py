"""
Compute a table representing KMP failure function:

Specifically, the failure function f(k) is defined as the length of the longest pattern prefix P[:x]
that is also a pattern suffix P[1:k+1]

Intuitively, if we find a mismatch upon character P[k+1], the function f(k) determines how many of the
immediately preceding characters can be reused to restart the pattern
"""


def compute_kmp_fail(P):
    """
    bootstrapping process that compares the pattern to itself. Each time
    two characters match, we set f(j) = k + 1

    """
    j = 1
    k = 0
    fail = [0] * len(P)
    while j < len(P):
        if P[j] == P[k]:  # match
            fail[j] = k + 1  # k + 1 chars match so far
            j += 1
            k += 1
        elif k > 0:
            k = fail[k - 1]
        else:  # no match found starting at j
            j += 1
    return fail


def find_kmp(T, P):
    n, m = len(T), len(P)
    if m == 0:
        return 0
    fail = compute_kmp_fail(P)
    j = 0  # text
    k = 0  # pattern
    while j < n:
        if T[j] == P[k]:  # match
            if k == m - 1:  # end of pattern
                return j - m + 1  # current index in text - length of pattern
            j += 1
            k += 1
        elif k > 0:  # mismatch following match of preceeding char(s)
            k = fail[k - 1]
        else:
            j += 1
    return -1


if __name__ == "__main__":
    p = "amalgamation"
