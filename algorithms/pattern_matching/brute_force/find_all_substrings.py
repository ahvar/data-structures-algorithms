"""
Find all indicies at which a pattern substring begins in text

for reference, some python functions that implement similar functionality:
find()
index()
count()
partition()
split()
replace()
"""


def find_all_substrings(text, pattern):
    subs = []
    txt_len, pat_len = len(text), len(pattern)
    if pat_len > txt_len:
        return subs
    for i in range(
        (len(text) - len(pattern)) + 1
    ):  # + 1 so we can slice at position immediately after the char we want
        k = 0
        while k < pat_len and text[i + k] == pattern[k]:
            k += 1
        if k == pat_len:
            subs.append(i)
    return subs


if __name__ == "__main__":
    text = "abadbabdbabcdbdaccdadcdba"
    pattern = "ab"
    print(find_all_substrings(text, pattern))
