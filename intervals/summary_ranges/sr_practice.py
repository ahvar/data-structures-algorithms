from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        n = len(nums)
        start = nums[0]
        for i in range(1, n + 1):
            if i == n or nums[i] != nums[i - 1] + 1:
                end = nums[i - 1]
                if end == start:
                    result.append(f"{start}")
                else:
                    result.append(f"{start}->{end}")
                if i < len(nums):
                    start = nums[i]
