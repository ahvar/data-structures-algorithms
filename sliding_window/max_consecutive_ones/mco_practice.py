from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        if nums == None or len(nums) == 0:
            return 0
        zero_count = 0
        left = 0
        maxx = 0
        n = len(nums)
        for right in range(n):
            if nums[right] == 0:
                zero_count += 1
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            maxx = max(maxx, right - left + 1)


if __name__ == "__main__":
    solution = Solution()
