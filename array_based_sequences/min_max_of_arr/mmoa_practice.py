from typing import List
from math import ceil


class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:

        prefix_sum = 0
        answer = 0

        for idx, value in enumerate(nums):
            prefix_sum += value

            prefix_limit = (prefix_sum + idx) // (idx + 1)

            answer = max(answer, prefix_limit)
        return answer
