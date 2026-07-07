DESCRIPTION (inspired by Leetcode.com)
Write a function to modify an m x n integer matrix matrix directly, such that if any element in the matrix is 0, its entire corresponding row and column are set to 0. This transformation should be done in place, without using any additional data structures for storage.

Input:

matrix = [
    [0,2,3],
    [4,5,6],
    [7,8,9]
]
Output:

[
    [0,0,0],
    [0,5,6],
    [0,8,9]
]
Explanation: Since the element at the first row and first column is 0, set all elements in the first row and first column to 0.