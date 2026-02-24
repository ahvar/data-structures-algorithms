from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        result = []

        def backtrack(permutation):
            if len(permutation) == len(nums):
                result.append(permutation[:])
                return
            for num in nums:
                if num not in permutation:
                    permutation.append(num)
                backtrack(permutation)
                permutation.pop()

        backtrack([])
        return result


if __name__ == "__main__":
    nums = [1, 2, 3]
    solution = Solution()
    print(solution.permute(nums))
