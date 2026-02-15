from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        zero_count = 0
        left = 0
        n = len(nums)
        maxx = 0
        for i in range(n):
            if nums[i] == 0:
                zero_count += 1
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            maxx = max(maxx, i - left + 1)


if __name__ == "__main__":
    solution = Solution()
