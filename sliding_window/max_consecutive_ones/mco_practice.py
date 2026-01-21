from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        zeros = 0
        maxx = 0
        n = len(nums)
        for right in range(n):
            if nums[right] == 0:
                zeros += 1
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            maxx = max(maxx, right - left + 1)
        return maxx


if __name__ == "__main__":
    solution = Solution()
