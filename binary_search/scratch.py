def binary_search(target, arr):
    high = len(arr) - 1
    low = 0
    mid = (high + low) // 2
    index = -1
    while low <= high or index < 0:
        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            high = mid
            mid = (high + low) // 2
        elif target > arr[mid]:
            low = mid
            mid = (high + low) // 2

    return index


if __name__ == "__main__":
    arr = [2, 3, 6, 7, 8, 13, 18, 21, 23, 24, 27, 30, 32, 40, 41]
    print(binary_search(27, arr))
