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
                if stack[-1] > abs(a):
                    alive = False
                elif stack[-1] < abs(a):
                    stack.pop()
                else:
                    stack.pop()
                    alive = False
            if alive:
                stack.append(a)
        return stack


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_asteroid(self):
        assert self.solution.asteroidCollision([5, 10, -5]) == [5, 10]
