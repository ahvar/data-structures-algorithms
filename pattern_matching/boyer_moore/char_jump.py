"""
1. walk back from the end of segment
2. if the char is in the adjust dict, replace the char and adjust
"""


def char_jump(segment, adjust):
    i = len(segment) - 1
    while i >= 0:
        if segment[i] in adjust:
            key = segment[i]
            segment = segment[:i] + "_" + segment[i + 1 :]
            i -= adjust[key]
        else:
            i -= 1
    return segment


if __name__ == "__main__":
    segment = "redpantkswoplaneroofjkplantpitgopaplplanat"
    adjust = {"a": 3, "l": 2, "o": 1}
    new_segment = char_jump(segment, adjust)
    print(new_segment)
