l1 = [2, 4, 6, 8]
l2 = [3, 5, 7, 9]


def merge_sorted_lists(a, b):
    i = j = 0
    merged = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1
    # append any leftover items
    if i < len(a):
        merged.extend(a[i:])
    if j < len(b):
        merged.extend(b[j:])
    return merged
