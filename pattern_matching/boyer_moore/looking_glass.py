"""
start comparisons of pattern with segment from the end of pattern
"""


def start_from_end(segment, pattern):
    i = 0
    while i < len(segment) - len(pattern) + 1:
        k = len(pattern) - 1
        while k > 0 and segment[i + k] == pattern[k]:
            k -= 1
        if k == 0:
            return i
        i += 1
    return -1


if __name__ == "__main__":
    pattern = "lmn"
    segment = "rlnlmnolo"
    print(start_from_end(segment, pattern))
