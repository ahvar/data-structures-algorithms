from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_first():
            left, right = 0, len(nums) - 1
            first = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    first = mid
                    right = mid - 1
            return first

        def find_last():
            left, right = 0, len(nums) - 1
            last = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    last = mid
                    left = mid + 1
            return last

        first = find_first()
        last = find_last()
        return [first, last] if first != -1 else [-1, -1]


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example(self):
        assert self.solution.searchRange(nums=[5, 7, 7, 8, 8, 10], target=8) == [3, 4]
