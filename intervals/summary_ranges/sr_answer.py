from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        result = []
        start = prev = nums[0]

        for num in nums[1:]:
            if num != prev + 1:
                result.append(str(start) if start == prev else f"{start}->{prev}")
                start = num
            prev = num

        result.append(str(start) if start == prev else f"{start}->{prev}")
        return result
