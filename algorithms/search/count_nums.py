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



if __name__ == "__main__":
    nums = [3,3,3,9,23,2,98,2,1,435]
    rprint(get_max(nums))
