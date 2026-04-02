from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            if a > 0:
                stack.append(a)
                continue
            alive = True
            while alive and stack and stack[-1] > 0:
                if stack[-1] < abs(a):
                    stack.pop()
                elif stack[-1] == abs(a):
                    alive = not alive
                else:
                    stack.pop()
                    alive = not alive
            if alive:
                stack.append(a)
        return stack
