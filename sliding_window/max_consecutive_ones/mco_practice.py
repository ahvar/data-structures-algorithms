from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        if not nums or len(nums) == 0:
            return 0

        left = 0
        zeros_count = 0
        maxx = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros_count += 1
            while zeros_count > k:
                if nums[left] == 0:
                    zeros_count -= 1
                left += 1
            maxx = max(maxx, right - left + 1)


if __name__ == "__main__":
    solution = Solution()
