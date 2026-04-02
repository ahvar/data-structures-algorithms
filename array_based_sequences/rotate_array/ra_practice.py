from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        temp = nums[-k:]
        for i in range(n - 1, k - 1, -1):
            nums[i] = nums[i - k]

        for i in range(k):
            nums[i] = temp[i]

    def alt_slicing(self, nums: List[int], k: int) -> None:
        pass


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_rotate(self):
        assert self.solution.rotate([1, 2, 3, 4, 5], 2) == [3, 4, 5, 1, 2]


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    k = 2
    solution = Solution()
    solution.rotate(nums, k)
