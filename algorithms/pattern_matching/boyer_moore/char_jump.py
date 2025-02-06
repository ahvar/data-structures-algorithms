def char_jump_heuristic(segment, pattern):
    last = {}
    for i in range(len(pattern) - 1):
        last[pattern[i]] = i
    i = 0
    while i < len(segment):
        k = len(pattern) - 1
        while k >= 0:
            if k == 0:
                return segment[i : len(pattern)]  # match found
            if segment[i + k] != pattern[k]:  # mismatch
                if segment[i + k] in pattern:
                    index = last.get(
                        segment[i], -1
                    )  # index of the rightmost mismatched char
                    i += len(pattern) - min(
                        k, index + 1
                    )  # how much to move i to align it with
                    k = len(pattern) - 1
                else:
                    i += len(pattern) - k
            i -= 1
    return -1


if __name__ == "__main__":
    pattern = "redpantkswoplaneroofjkplantpitgopaplplanat"
    segment = "planet"
    print(char_jump_heuristic(segment, pattern))
