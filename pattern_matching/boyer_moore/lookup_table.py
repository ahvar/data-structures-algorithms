def lookup_table(target, text):
    last = {}
    for i in range(len(text) - 1):
        last[text[i]] = i
    print(last)
    index = last.get(target, -1)
    print(index)


if __name__ == "__main__":

    text = "abefjslde"

    target = "b"
    print(lookup_table(target, text))
