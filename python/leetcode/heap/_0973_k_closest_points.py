"""
_0973_k_closest_points

#heap

"""

from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        min_heap = [((p[0]**2+p[1]**2), p) for p in points]
        result = [p for _, p in heapq.nsmallest(k, min_heap)]

        return result
    

def main():

    solution = Solution()

    # points = [[1,3],[-2,2]]
    # k = 1

    points = [[3,3],[5,-1],[-2,4]]
    k = 2

    result = solution.kClosest(points, k)
    print(result)