"""
Compute a map representing the `last` function used in the Boyer-Moore
pattern-matching algorithm for characters in the pattern string
"""

from rich import print as rprint


def last_fct(pattern):
    last = {}
    for i, char in enumerate(pattern):
        last[char] = i
    return last


def boyer_moore_fct(text, pattern):
    if not pattern:
        return 0  # trivial search for empty pattern
    last = last_fct(pattern)
    pattern_length = len(pattern)
    text_length = len(text)
    i = pattern_length - 1  # index of text
    k = pattern_length - 1  # index of pattern
    while i < text_length:
        if pattern[k] == text[i]:
            if i == 0:
                return i
            i -= 1
            k -= 1
        else:
            j = last.get(
                text[i], -1
            )  # the last instance of text[i] in pattern; -1 if not found
            i += pattern_length - min(
                k, j + 1
            )  # immediately after last instance of text[i] in pattern OR
            k = pattern_length - 1  # restart at end of the pattern


if __name__ == "__main__":
    text = "the quick brown fox jumped over a lazy cat"
    pattern = "ox jum"
    rprint(boyer_moore_fct(text, pattern))
