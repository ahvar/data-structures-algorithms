from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        write = 0
        for read in range(len(nums)):
            if nums[read] != val:
                nums[write] = nums[read]
                write += 1
        return write


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_remove(self):
        self.solution.removeElement([2, 4, 1, 3, 2, 1], 1)
