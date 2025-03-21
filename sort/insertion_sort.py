def insertion_sort(arr):
    for k in range(1, len(arr)):
        cur = arr[k]
        j = k
        while j > 0 and arr[j - 1] > cur:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = cur
    return arr


def alt_sort(arr):
    for k in range(len(arr)):
        j = k
        while j > 0:
            if arr[k] < arr[j]:
                print("{} less than {}".format(arr[j], arr[k]))
                arr = arr[: j + 1] + [arr[k]] + arr[j + 1 :]
                arr.pop(k + 1)
            j -= 1
        print("")
    return arr


if __name__ == "__main__":
    arr = [99, 3, 5, 92, 22, 14, 7, 1, 56, 10, 9, 11, 10]
    print(arr)
    print(insertion_sort(arr))
