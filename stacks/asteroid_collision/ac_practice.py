from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        arr = []
        for a in asteroids:
            if a > 0:
                arr.append(a)
                continue
            still_alive = True
            while still_alive and arr[-1] > 0:
                if arr[-1] < abs(a):
                    arr.pop()

                elif arr[-1] == abs(a):
                    still_alive = False

                else:
                    arr.pop()
                    still_alive = False
            if still_alive:
                arr.append(a)
        return arr
