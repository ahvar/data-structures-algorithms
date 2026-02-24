from typing import List


class Solution:
    def two_loop_solution(self, gas, cost):
        n = len(gas)
        tank = [0] * n
        for i in range(n):
            tank_after_leaving = tank[i] - cost[i]
            for j in range(i + 1, n):
                tank[j] = (gas[j] + tank[j - 1]) - cost[j]
                if tank[j] <= 0:
                    break
            if tank[n - 1] > 0:
                if i == 0:
                    return 0
                for k in range(i):
                    if k == 0:
                        tank[k] = (tank[n - 1] + tank[k]) - cost[n - 1]
                    else:
                        tank[k] = (tank[k - 1] + tank[k]) - cost[k]

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        net_gas = [gas[i] - cost[i] for i in range(n)]
        total_sum = 0
        tank = 0
        start_index = 0
        for i in range(n):
            tank += net_gas[i]
            total_sum += net_gas[i]
            if tank < 0:
                start_index = i + 1
                tank = 0
        if total_sum < 0:
            return -1
        return start_index


if __name__ == "__main__":
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    solution = Solution(gas, cost)
