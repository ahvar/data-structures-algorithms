from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        ans = []

        def backtrack(permutation):
            if len(permutation) == len(nums):
                ans.append(permutation[:])
                return
            for i in range(len(nums)):
                if nums[i] not in permutation:
                    permutation.append(nums[i])
                    permutation(permutation)
                    permutation.pop()

        backtrack([])
        return ans


if __name__ == "__main__":
    nums = [1, 2, 3]
    solution = Solution()
    print(solution.permute(nums))
