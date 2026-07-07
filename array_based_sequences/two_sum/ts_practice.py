from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        left = 0
        right = len(nums) - 1
        output = None
        while left < right:
            total = nums[left] + nums[right]
            if total == target:
                output = [left, right]
                return output
            elif total < target:
                left += 1
            else:
                right -= 1
        return output


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_two_sum(self):
        assert self.solution.twoSum(nums=[2, 7, 11, 15], target=9) == [0, 1]
