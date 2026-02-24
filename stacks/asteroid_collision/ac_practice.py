from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        output = []
        for asteroid in asteroids:
            if asteroid > 0:
                stack.append(asteroid)
                continue
            alive = True
            while alive and stack and stack[-1] > 0:
                if stack[-1] < abs(asteroid):
                    stack.pop()
                elif stack[-1] == abs(asteroid):
                    stack.pop()
                    alive = False
                else:
                    alive = False
            if alive:
                stack.append(asteroid)
        return output


class TestSolution:

    def setup_method(self):
        self.solution = Solution()

    def test_asteroid_collison(self):
        asteroids = [5, 10, -15]
        assert self.solution.asteroidCollision(asteroids) == [5, 10]
