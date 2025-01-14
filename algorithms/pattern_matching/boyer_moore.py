def find_boyer_moore(text, pattern):
    text_length, pattern_length = len(text), len(pattern)
    if pattern_length == 0:
        return 0
    last = {}
    for k in range(pattern_length):  # dict of pattern chars and their indicies
        last[pattern[k]] = k
    i = pattern_length - 1
    k - pattern_length - 1
    while i < text_length:
        if text[i] == pattern[k]:  # chars match
            if k == 0:  # end of pattern; return starting index
                return i
            i -= 1
            k -= 1
        else:
            j = last.get(text[i], -1)  # index of next instance
            i += pattern_length - min(k, j + 1)  # case analysis for jump step
            k = pattern_length - 1  # restart at end of pattern
    return -1
