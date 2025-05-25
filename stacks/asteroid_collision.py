"""
We are given an array asteroids of integers representing asteroids in a row. The indices of the asteriod in the array
represent their relative position in space.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right,
negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are
the same size, both will explode. Two asteroids moving in the same direction will never meet.

Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
Example 2:

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.
Example 3:

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
"""
from typing import Optional, List
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        i = len(asteroids) - 1
        while i >= 0:
            if not (asteroids[i-1] > 0 and asteroids[i] < 0):
                i -= 2
                continue

            if abs(asteroids[i]) == abs(asteroids[i-1]): # both explode
                asteroids.pop()
                asteroids.pop()
                i -= 2
            elif abs(asteroids[i]) < abs(asteroids[i-1]): # penultimate asteroid explodes last asteroid
                asteroids.pop(i)
                i -= 1
            else: # last asteroid explodes penultimate asteroid
                winner = asteroids.pop(i)
                asteroids.pop(i-1)
                asteroids[i-1] = winner
                i -= 1
        return asteroids



if __name__ == "__main__":
    asteroids = [-2, -2, -2, 1]
    solution = Solution()
    print(solution.asteroidCollision(asteroids))