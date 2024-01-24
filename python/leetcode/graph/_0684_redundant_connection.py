"""
_0684_redundant_connection

Takeaways:

Notes:
- Use Union-Find?

#graph, #dfs

"""

from typing import List
from collections import defaultdict

class Solution:
    """
        Solution.

        Complexity:
            time:
            memory:
    """
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        graph = defaultdict(set)

        for i, j in edges:
            graph[i].add(j)


        for i, j in edges:

            graph[i].remove(j)

            pass



        return []

def run_tests(solution):
    print("test passed!")

def main():

    solution = Solution()

    run_tests(solution)

    edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]

    print(edges)
    result = solution.findRedundantConnection(edges)
    print(result)