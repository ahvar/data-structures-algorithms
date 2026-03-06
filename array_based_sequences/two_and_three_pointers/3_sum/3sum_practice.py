from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        nums.sort()
        n = len(nums)
        triplets = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    triplets.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < 0:
                    left += 1

                else:
                    right -= 1
        return triplets


class TestSolution:
    def setup_method(self):
        self.nums = [-1, 0, 1, 2, -1, -4]
        self.solution = Solution()

    def test_3sum(self):
        assert self.solution.threeSum(self.nums) == [[-1, -1, 2], [-1, 0, 1]]
