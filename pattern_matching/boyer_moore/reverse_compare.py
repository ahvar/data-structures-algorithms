"""
compare two strings from right to left
 - return 0 if segment matches pattern entirely when compared in reverse order
 - the starting index of pattern in segment, if it is found
 - the percentage of mismatched characters if pattern is not found
"""


def reverse_compare(segment, pattern):
    mismatch_count = 0
    if len(segment) == len(pattern):
        return 0 if segment == pattern[::-1] else 100.0
    for i in range(len(segment) - len(pattern), -1, -1):
        k = len(pattern) - 1
        while k >= 0:
            if segment[i] != pattern[k]:
                mismatch_count += 1
            k -= 1
        if k < 0:
            return i
    return mismatch_count / len(segment) * 100


if __name__ == "__main__":
    segment = "abdcbed"
    pattern = "bde"
    print(reverse_compare(segment, pattern))
