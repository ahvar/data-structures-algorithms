"""
We are given an array asteroids of integers representing asteroids in a row.

1. The indices of the asteriod in the array represent their relative position in space.

2. For each asteroid, the absolute value represents its size

3. the sign represents its direction (positive meaning right, negative meaning left). 

4. Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode.
If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

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
from typing import List
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        asteroid_stack = []
        for i in range(len(asteroids)):
            if not asteroid_stack:
                asteroid_stack.append(asteroids[i])
                continue

            if asteroid_stack[-1] < 0 and asteroids[i] > 0 or asteroid_stack[-1] > 0 and asteroids[i] < 0:
                last_asteroid = asteroid_stack.pop()
                asteroid_stack.append(max(abs(last_asteroid), abs(asteroids[i])))
            if abs(asteroid_stack[-1]) == abs(asteroids[i]):
                asteroid_stack.pop()
            else:
                asteroid_stack.append(asteroids[i])

        return asteroid_stack




if __name__ == "__main__":
    asteroids = [5,10,-5]
    solution = Solution()
    print(solution.asteroidCollision(asteroids))
