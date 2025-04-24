"""
The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

Example 1:

Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4

Example 2:
Input: n = 25
Output: 1389537
"""
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        t = [0 for _ in range(n)]
        t[1] = 1
        t[2] = 1
        for i in range(3,n):
            t[i] = t[i-1] + t[i-2] + t[i-3]
        last = len(t) - 1
        return t[last] + t[last-1] + t[last-2]



if __name__ == "__main__":
    n = 25
    solution = Solution()
    print(solution.tribonacci(n))

