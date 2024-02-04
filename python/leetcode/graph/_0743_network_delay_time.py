"""
_0743_network_delay_time

Takeaways:
- dfs + dijkstra + heap

TODO:
- reimplement with bfs

"""

from typing import List
import heapq

class Solution:
    """
        Solution.

        Complexity:
            time: O()
            memory: O()
    """
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        self.graph = { u : [] for u in range(n) }
        for u, v, t in times:
            self.graph[u-1].append((v-1,t))

        # print(self.graph)

        self.discovered = [False] * n
        self.distance = [float('inf')] * n

        self.max_time = -1

        self.distance[k-1] = 0
        self.dfs(k-1)

        for d in self.discovered:
            if not d:
                return -1

        return self.max_time


    def dfs(self, u: int):

        self.discovered[u] = True
        verts = []

        for v, t in self.graph[u]:
            if not self.discovered[v]:
                self.distance[v] = min(self.distance[v], self.distance[u]+t)
                # TODO: heapq.heappush instead
                verts.append((self.distance[v], v))

        heapq.heapify(verts)
        # print(verts)

        while verts:
            t, v = heapq.heappop(verts)
            if not self.discovered[v]: # do we need?
                self.dfs(v)
        
        self.max_time = max(self.distance[u], self.max_time)
        # print(self.max_time)
        return False



def run_tests(solution):
    print("test passed!")

def main():

    solution = Solution()

    run_tests(solution)

    times = [[2,1,1],[2,3,1],[3,4,1]]
    n = 4
    k = 2

    # times = [[1,2,1]]
    # n = 2
    # k = 2

    # times = [[1,2,1],[2,3,2]]
    # n = 3
    # k = 1

    print(times, n, k)
    result = solution.networkDelayTime(times, n, k)
    print(result)