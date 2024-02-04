"""
_1584_min_cost_connect_all_points

Takeaways:

TODO: Implement prim's algorithm using heappop

#graph

"""

from typing import List

class Solution:
    """
        Prim's algorithm.

        Complexity:
            time: O(n^2)
            memory: O(n)
    """
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        intree = [False] * len(points)
        distance = [float('inf')] * len(points)
        total = 0

        v = 0

        while not intree[v]:

            # handle adding new v, update distances

            intree[v] = True

            for i in range(len(points)):
                if not intree[i]:
                    new_dist = abs(points[v][0] - points[i][0]) + abs(points[v][1] - points[i][1])
                    distance[i] = min(distance[i], new_dist)

            # select next v
            
            min_dist = float('inf')

            for i in range(len(points)):
                if not intree[i] and distance[i] < min_dist:
                    min_dist = distance[i]
                    v = i

            if not intree[v]:
                total += min_dist

        return total

def run_tests(solution):
    print("test passed!")

def main():

    solution = Solution()

    run_tests(solution)

    # points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
    points = [[3,12],[-2,5],[-4,1]]

    print(points)
    result = solution.minCostConnectPoints(points)
    print(result)