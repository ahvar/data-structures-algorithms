def last_occurrence(pattern):
    last = {}
    for i in range(len(pattern) - 1):
        last[pattern[i]] = i
    return last


def character_jump(segment, pattern, last):
    i = 0
    while i < len(segment) - len(pattern):
        k = len(pattern) - 1
        while k >= 0:
            if segment[i + k] != pattern[k]:
                if segment[i + k] in pattern:
                    last = last.get(segment[i + k], -1)
                    i += len(pattern) - min(k, last + 1)
                    k = len(pattern) - 1
                else:
                    i += (len(pattern) - k) + 1
                    k = len(pattern) - 1
            elif segment[i + k] == pattern[k]:
                if k == 0:
                    return segment[i : len(pattern) - 1]
                k -= 1
        i += 1


def character_jump_alt(segment, pattern, last_occurrence):
    i = 0
    while i <= len(segment) - len(pattern):
        k = len(pattern) - 1
        while k >= 0:
            if pattern[k] != segment[i + k]:
                if segment[i + k] in last_occurrence:  # is mismatch char in pattern?
                    # if k < last_occurrence then < k - last_occurrence < 1
                    i += max(1, k - last_occurrence[segment[i + k]])
                else:
                    i += k + 1
                break
            k -= 1
        if k < 0:
            return i  # match found
    return -1  # no match found


if __name__ == "__main__":
    segment = "pizzapalplanewupop"
    pattern = "planet"
    last = last_occurrence(pattern)
