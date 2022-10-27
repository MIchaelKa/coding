"""
[leetcode] 787. Cheapest Flights Within K Stops
"""

from typing import List
class Solution:

    MAX_PRICE = 99999

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        graph = [[] for _ in range(n)]

        for f in flights:
            graph[f[0]].append((f[1], f[2]))

        costs = [Solution.MAX_PRICE] * n
        processed = [False] * n
        self.parents = [-1] * n

        costs[src] = 0
        v = src

        while v != -1:
            for neighbor in graph[v]:
                cost_n = costs[v] + neighbor[1]
                if not processed[neighbor[0]] and cost_n < costs[neighbor[0]]:
                    costs[neighbor[0]] = cost_n
                    self.parents[neighbor[0]] = v

            min_cost = Solution.MAX_PRICE
            next_v = -1
            for i in range(n):
                if not processed[i] and costs[i] < min_cost:
                    min_cost = costs[i]
                    next_v = i

            processed[v] = True
            v = next_v


        return 0
    
def run_tests():

    solution = Solution()

    n = 3
    flights = [[0,1,100],[1,2,100],[0,2,500]]
    src = 0
    dst = 2
    k = 1
    result = solution.findCheapestPrice(n, flights, src, dst, k)

if __name__ == '__main__':


    solution = Solution()

    n = 4
    flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
    src = 0
    dst = 3
    k = 1
    result = solution.findCheapestPrice(n, flights, src, dst, k)
    print(solution.parents)