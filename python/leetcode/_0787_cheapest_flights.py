"""
[leetcode] 787. Cheapest Flights Within K Stops
"""

from typing import List
class Solution:

    MAX_PRICE = 99999

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        self.graph = [[] for _ in range(n)]
        self.n = n

        for f in flights:
            self.graph[f[0]].append((f[1], f[2]))

        self.costs = [Solution.MAX_PRICE] * n
        processed = [False] * n
        self.parents = [-1] * n
        self.num_vert = [-1] * n

        self.costs[src] = 0
        self.num_vert[src] = 0
        v = src

        while v != -1:
            for neighbor in self.graph[v]:
                cost_n = self.costs[v] + neighbor[1]
                if not processed[neighbor[0]] and cost_n < self.costs[neighbor[0]]:
                    self.costs[neighbor[0]] = cost_n
                    self.parents[neighbor[0]] = v
                    self.num_vert[neighbor[0]] = self.num_vert[v] + 1

            min_cost = Solution.MAX_PRICE
            next_v = -1
            for i in range(n):
                if not processed[i] and self.costs[i] < min_cost:
                    min_cost = self.costs[i]
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
            new_parent_for_j = new_j = -1
            for i in range(len(path)):
                for j in range(i+2, len(path)):
                    new_parent, new_cost, num_vert_diff = self.getCost(path[i],path[j])
                    if new_parent == -1:
                        continue
                    
                    # If we are here - we found new_parent for path[j] vert

                    old_cost = self.costs[path[j]] - self.costs[path[i]]
                    diff_cost = new_cost - old_cost
                    if diff_cost < min_diff_cost:
                        min_diff_cost = diff_cost
                        new_parent_for_j = new_parent
                        new_j = j
            
            if new_parent_for_j == -1:
                return -1
            
            self.updateCosts(dst, path[new_j], min_diff_cost, num_vert_diff)
            self.parents[path[new_j]] = new_parent_for_j
            path = self.updatePath(path, new_parent_for_j, new_j)
            stops -= 1

            # print(new_i, new_j)
            # print(path)
            # print(costs)
            

        return self.costs[dst]
    
    def updateCosts(self, v: int, start: int, addition: int, num_vert_diff: int):
        self.costs[v] += addition
        self.num_vert[v] -= num_vert_diff
        if v == start:
            return
        self.updateCosts(self.parents[v], start, addition, num_vert_diff)


    def updatePath(self, path: List[int], new_parent_for_j: int, j: int):
        new_path = self.findPath(new_parent_for_j)
        new_path.extend(path[j:])
        return new_path

    
    def getCost(self, i: int, j: int):
        """
        Поиск по всем потенциальным предкам вершины j
        Находим мнинимальную стоимость с меньшим чем было количеством вершин.
        """
        min_cost = Solution.MAX_PRICE
        new_parent = -1
        num_vert_diff = -1
        for v in range(self.n):
            for neighbor in self.graph[v]:
                if neighbor[0] == j:
                    new_cost = self.costs[v] + neighbor[1]
                    new_num_vert = self.num_vert[v] + 1
                    if new_cost < min_cost and new_num_vert < self.num_vert[j]:
                        min_cost = new_cost
                        num_vert_diff = self.num_vert[j] - new_num_vert
                        new_parent = v

        return new_parent, min_cost, num_vert_diff
        
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

    n = 4
    flights = [[0,1,1],[0,2,5],[1,2,1],[2,3,1]]
    src = 0
    dst = 3
    k = 1
    result = solution.findCheapestPrice(n, flights, src, dst, k)
    assert(result==6)

    n = 5
    flights = [[0,1,5],[1,2,5],[0,3,2],[3,1,2],[1,4,1],[4,2,1]]
    src = 0
    dst = 2
    k = 2
    result = solution.findCheapestPrice(n, flights, src, dst, k)
    assert(result==7)

    n = 11
    flights = [[0,3,3],[3,4,3],[4,1,3],[0,5,1],[5,1,100],[0,6,2],[6,1,100],[0,7,1],[7,8,1],[8,9,1],[9,1,1],[1,10,1],[10,2,1],[1,2,100]]
    src = 0
    dst = 2
    k = 4
    result = solution.findCheapestPrice(n, flights, src, dst, k)
    assert(result==11)

    print("tests passed")

if __name__ == '__main__':

    # run_tests()

    solution = Solution()

    n = 10
    flights = [[0,1,20],[1,2,20],[2,3,30],[3,4,30],[4,5,30],[5,6,30],[6,7,30],[7,8,30],[8,9,30],[0,2,9999],[2,4,9998],[4,7,9997]]
    src = 0
    dst = 9
    k = 4
    result = solution.findCheapestPrice(n, flights, src, dst, k)
    # assert(result==30054)
    print(result)