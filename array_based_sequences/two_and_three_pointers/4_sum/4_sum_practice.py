from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums:
            return []
        nums.sort()
        result = []
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i + 1]:
                continue
            for j in range(i + 1, n):
                if j >= i + 1 and nums[j] == nums[j - 1]:
                    continue

                left = j + 1
                right = n - 1
                while left < right:
                    s = nums[i] + nums[j] + nums[left] + nums[right]
                    if s == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])

                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1

                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

                    elif s < target:
                        left += 1
                    else:
                        right -= 1
        return result
