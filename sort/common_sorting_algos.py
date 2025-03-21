def bubble_sort(nums):
    j = len(nums) - 1
    while j >= 0:
        for i in range(j):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
        j -= 1
    return nums


def get_min(nums):
    min_idx = 0
    min = nums[0]
    for i in range(len(nums)):
        if nums[i] < min:
            min_idx = i
            min = nums[i]
    return min_idx


def selection_sort(nums):
    for i in range(len(nums) - 1):
        min_idx = get_min(nums[i:])
        nums[i], nums[min_idx + i] = nums[min_idx + i], nums[i]
    return nums


def insertion_sort(nums):
    for i in range(1, len(nums)):
        curr = nums[i]
        j = i
        while j > 0 and curr < nums[j - 1]:
            nums[j] = nums[j - 1]
            j -= 1
        nums[j] = curr
    return nums


if __name__ == "__main__":
    nums = [2, 7, 8, 4, 1, 9, 5, 6, 3]
    print(insertion_sort(nums))
