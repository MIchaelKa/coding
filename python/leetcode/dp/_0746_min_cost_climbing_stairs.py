"""
_0746_min_cost_climbing_stairs

#dp

"""

from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        cost += [0]

        for i in range(2, len(cost)):
            cost[i] = min(cost[i-1], cost[i-2]) + cost[i]

        return cost[-1]


def main():
    solution = Solution()

    cost = [1,100,1,1,1,100,1,1,100,1]
    # cost = [10,15,20]
    # cost = []

    result = solution.minCostClimbingStairs(cost)
    print(result)