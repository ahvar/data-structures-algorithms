from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        p = []

        def backtrack(permutation):
            if len(permutation) == len(nums):
                p.append(permutation[:])
                return
            for n in nums:
                if n not in permutation:
                    permutation.append(n)
                    backtrack(permutation)
                    permutation.pop()

        backtrack([])
        return p


if __name__ == "__main__":
    nums = [1, 2, 3]
    solution = Solution()
    print(solution.permute(nums))
