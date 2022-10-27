"""
[leetcode] 787. Cheapest Flights Within K Stops
"""

from typing import List
class Solution:

    MAX_PRICE = 99999

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        self.graph = [[] for _ in range(n)]

        for f in flights:
            self.graph[f[0]].append((f[1], f[2]))

        costs = [Solution.MAX_PRICE] * n
        processed = [False] * n
        self.parents = [-1] * n

        costs[src] = 0
        v = src

        while v != -1:
            for neighbor in self.graph[v]:
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

        
        path = self.findPath(dst)

        # print(self.parents)
        # print(path)
        # print(costs)

        if path[0] != src:
            return -1
        
        stops = len(path) - 2

        while not stops <= k:
            min_diff_cost = Solution.MAX_PRICE
            new_path_cost = 0
            new_i = new_j = -1
            for i in range(len(path)):
                for j in range(i+2, len(path)):
                    # we can't just get price between i and j, need O(n) search
                    short_path_cost = self.getCost(i,j)
                    if short_path_cost == -1:
                        continue
                    
                    long_path_cost = costs[j] - costs[i]
                    new_cost = short_path_cost - long_path_cost
                    if new_cost < min_diff_cost:
                        min_diff_cost = new_cost
                        new_path_cost = short_path_cost
                        new_i, new_j = i, j
            
            if new_i == -1:
                return -1
            
            path = self.shortenPath(path, new_i, new_j)
            costs[new_j] = new_path_cost + costs[new_i]
            stops -= 1

            # print(new_i, new_j)
            # print(path)
            # print(costs)
            

        return costs[dst]
    
    def shortenPath(self, path: List[int], i: int, j: int):
        new_path = []
        for k in range(len(path)):
            if k > i and k < j:
                continue
            new_path.append(path[k])
        return new_path

    
    def getCost(self, i: int, j: int):
        for neighbor in self.graph[i]:
            if neighbor[0] == j:
                return neighbor[1]
        return -1
        
    def findPath(self, v: int) -> List[int]:

        if self.parents[v] == -1:
            return [v]

        path = self.findPath(self.parents[v])
        path.append(v)
        return path
    
def run_tests():

    solution = Solution()

    n = 3
    flights = [[0,1,100],[1,2,100],[0,2,500]]
    src = 0
    dst = 2
    k = 0
    result = solution.findCheapestPrice(n, flights, src, dst, k)
    assert(result==500)

    n = 3
    flights = [[0,1,100],[1,2,100],[0,2,500]]
    src = 0
    dst = 2
    k = 1
    result = solution.findCheapestPrice(n, flights, src, dst, k)
    assert(result==200)

    n = 4
    flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
    src = 0
    dst = 3
    k = 0
    result = solution.findCheapestPrice(n, flights, src, dst, k)
    assert(result==-1)

    n = 4
    flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
    src = 0
    dst = 3
    k = 1
    result = solution.findCheapestPrice(n, flights, src, dst, k)
    assert(result==700)

    n = 4
    flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
    src = 0
    dst = 3
    k = 2
    result = solution.findCheapestPrice(n, flights, src, dst, k)
    assert(result==400)

if __name__ == '__main__':

    run_tests()


    solution = Solution()

    n = 4
    flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
    src = 0
    dst = 3
    k = 1
    result = solution.findCheapestPrice(n, flights, src, dst, k)
    print(result)