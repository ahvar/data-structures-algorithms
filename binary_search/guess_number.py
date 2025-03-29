"""
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:

-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
0: your guess is equal to the number I picked (i.e. num == pick).
Return the number that I picked.



Example 1:

Input: n = 10, pick = 6
Output: 6
Example 2:

Input: n = 1, pick = 1
Output: 1
Example 3:

Input: n = 2, pick = 1
Output: 1
"""


def guess(n):
    target = 32
    last = 45
    if n < target < last:
        return 1
    elif last > n > target:
        return -1
    elif n == target:
        return 0


class Solution:
    def guessNumber(self, n: int) -> int:
        left = 0
        right = n
        g = left + (right - left) // 2
        result = guess(g)
        while left < right and result != 0:
            if result == -1:
                right = g - 1
            elif result == 1:
                left = g + 1
            g = left + (right - left) // 2
            result = guess(g)
        return g


if __name__ == "__main__":
    n = 45
    s = Solution()
    print(s.guessNumber(n))
