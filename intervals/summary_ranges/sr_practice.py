from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        ranges = []
        start = prev = nums[0]
        for num in nums[1:]:
            if num != prev + 1:
                ranges.append(str(start) if start == prev else f"{start}->{prev}")
                start = num
            prev = num
        ranges.append(str(start) if start == prev else f"{start}->{prev}")
        return ranges
