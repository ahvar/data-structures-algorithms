class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if nums == None or len(nums) == 0:
            return
        n = len(nums)
        k %= n
        if k == 0:
            return
        temp = nums[-k:]
        for i in range(n - 1, k - 1, -1):
            nums[i] = nums[i - k]
        for j in range(k):
            nums[j] = temp[j]

    def alt_slicing(self, nums: List[int], k: int) -> None:
        if not nums:
            return
        n = len(nums)
        k %= n
        if k == 0:
            return
        nums[:] = nums[-k:] + nums[:-k]
