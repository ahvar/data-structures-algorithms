from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        write = 2
        for read in range(2, len(nums)):
            if nums[read] != nums[write - 2]:
                nums[write] = nums[read]
                write += 1
        return write


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_remove(self):
        assert self.solution.removeDuplicates([1, 1, 1, 2, 2, 3]) == 5
