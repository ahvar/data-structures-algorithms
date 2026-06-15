from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Start with pointers at the two ends of the array.
        left = 0
        right = len(nums) - 1

        # Keep searching while there is still a valid range to inspect.
        while left <= right:
            # Compute the middle index of the current search range.
            mid = (left + right) // 2

            # If the middle value matches the target, return its index.
            if nums[mid] == target:
                return mid

            # Check whether the left half is sorted in ascending order.
            if nums[left] <= nums[mid]:
                # If the target falls inside the sorted left half, discard the right half.
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                # Otherwise, discard the left half and search the right half.
                else:
                    left = mid + 1
            # Otherwise, the right half must be the sorted half.
            else:
                # If the target falls inside the sorted right half, discard the left half.
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                # Otherwise, discard the right half and search the left half.
                else:
                    right = mid - 1

        # If the loop finishes, the target is not present in the array.
        return -1
