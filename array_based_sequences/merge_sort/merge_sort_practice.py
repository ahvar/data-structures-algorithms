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
                nums1[k] = nums2[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1


if __name__ == "__main__":
    nums1 = [1, 2, 4, 5, 19, 0, 0, 0, 0]
    nums2 = [5, 7, 6, 20]
    solution = Solution()
    print(solution.merge(nums1, 5, nums2, 4))
