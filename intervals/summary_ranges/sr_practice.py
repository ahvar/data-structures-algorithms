from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []
        start = nums[0]
        n = len(nums)
        for i in range(1, n):
            if i == n or nums[i] != nums[i - 1] + 1:
                end = nums[i - 1]
                if start == end:
                    ranges.append(str(start))
                else:
                    ranges.append(f"{start}->{end}")
            if i < n:
                start = nums[i]
        return ranges
