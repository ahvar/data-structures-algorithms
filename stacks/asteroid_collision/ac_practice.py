from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            if a > 0:
                stack.append(a)
                continue
            alive = True
            while stack and alive and stack[-1] > 0:
                if stack[-1] > abs(a):
                    alive = False
                elif stack[-1] < abs(a):
                    stack.pop()
                else:
                    alive = False
                    stack.pop()
            if alive:
                stack.append(a)
        return stack
