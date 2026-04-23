class Solution:
    def merge(self, nums1, m, nums2, n):
        for i in range(n - 1, -1, -1):
            j = m
            while j >= 0 and nums1[j - 1] > nums2[i]:
                nums1[j] = nums1[j - 1]
                j -= 1
            nums1[j] = nums2[i]
            m += 1
        return nums1

    def other_merge(self, nums1, m, nums2, n):
        i, j, k = m - 1, n - 1, m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_merge(self):
        assert self.solution.other_merge(
            nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3
        ) == [1, 2, 2, 3, 5, 6]
