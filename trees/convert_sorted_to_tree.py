"""
Given an integer array nums where the elements are sorted in ascending order,
convert it to a height-balanced binary search tree.
"""
from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # Base Case
        if len(nums) == 0: return None
        if len(nums) == 1: return TreeNode(nums[0])
        # Middle element becomes root of current subtree
        left = 0
        right = len(nums) - 1
        mid = (left + right) // 2
        root = TreeNode(nums[mid])
        # recursively build sub-trees
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root

if __name__ == "__main__":
    nums = [-10,-3,0,5,9]
    solution = Solution()
    solution.sortedArrayToBST(nums)