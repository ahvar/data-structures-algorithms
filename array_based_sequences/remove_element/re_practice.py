from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        write = 0
        for left in range(len(nums)):
            if nums[left] != val:
                nums[write] = nums[left]
                write += 1
        return write


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_remove(self):
        result = self.solution.removeElement([3, 4, 1, 6, 3, 2, 10], 3)
        assert result == 5
