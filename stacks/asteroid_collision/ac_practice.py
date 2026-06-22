from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = []
        for asteroid in asteroids:
            if asteroid > 0:
                stack.append(asteroid)
                continue
            alive = True
            while alive and stack and stack[-1] > 0:
                if stack[-1] < abs(asteroid):
                    stack.pop()
                elif stack[-1] > abs(asteroid):
                    alive = False
                else:
                    stack.pop()
                    alive = False
            if alive:
                stack.append(asteroid)
        return stack


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_collision(self):
        assert self.solution.asteroidCollision(asteroids=[5, 10, -5]) == [5, 10]
