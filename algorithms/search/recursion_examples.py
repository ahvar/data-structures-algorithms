from typing import List
from rich import print as rprint

def get_max(nums: List) -> int:
    if not nums:
        return float('-inf')
    if len(nums) == 1:
        return nums[0]
    
    first = nums[0]
    rest_max = get_max(nums[1:])
    return first + rest_max

def count(nums: List) -> int:
    # base case
    if not nums:
        return 0
    # recursive case
    rest_count = count(nums[1:])
    print(rest_count)
    return 1 + rest_count

def quicksort(nums: List) -> List:
    if len(nums) < 2:
        return nums
    pivot = nums[0]
    less = [ num for num in nums[1:] if num < pivot]
    greater = [ num for num in nums[1:] if num > pivot]
    return quicksort(less) + pivot + quicksort(greater)



if __name__ == "__main__":
    nums = [3,3,3,9,23,2,98,2,1,435]
    rprint(count(nums))
