from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        n = len(nums)
        intervals = []
        start = nums[0]
        for i in range(1, n + 1):
            if i == len(nums) or nums[i] != nums[i - 1] + 1:
                end = nums[i - 1]
                if start == end:
                    intervals.append(str(start))
                else:
                    intervals.append(f"{start}->{end}")
            if i < len(nums):
                start = nums[i]
        return intervals
