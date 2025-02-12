def find_smallest(arr):
    n = len(arr)
    smallest = arr[0]
    index = 0
    for i in range(1, n):
        if arr[i] < smallest:
            smallest = arr[i]
            index = i
    return index


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        smallest_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr


if __name__ == "__main__":
    nums = [2, 3, 0, 4, 3, 6, 12, 123, 554]
    print(selection_sort(nums))
