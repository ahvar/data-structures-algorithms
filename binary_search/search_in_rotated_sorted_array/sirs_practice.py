from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        while left <= right:
            mid = (right + left) // 2
            val = nums[mid]
            if val == target:
                return mid

            if nums[left] <= nums[mid]:
                if nums[left] <= target < val:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if val < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
