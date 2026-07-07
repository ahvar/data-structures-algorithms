from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            if a > 0:
                stack.append(a)
                continue
            alive = True
            while stack and alive:
                if stack[-1] < abs(a):
                    stack.pop()
                elif stack[-1] > abs(a):
                    alive = False
                else:
                    stack.pop()
                    alive = False

            if alive:
                stack.append(a)
        return stack


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_collision(self):
        assert self.solution.asteroidCollision(asteroids=[5, 10, -5]) == [5, 10]
        assert self.solution.asteroidCollision(asteroids=[8, -8]) == []
        assert self.solution.asteroidCollision(asteroids=[10, 2, -5]) == [10]
